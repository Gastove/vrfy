from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from . import models
from .table_models import ProblemSetResultTable, define_ps_table
from django_tables2 import A

def max_len(ps_sets):
  #get all of the problem sets and return that (should be for a section... to do)
  cols = 0
  for ps in ps_sets:
    if len(ps.problems.all()) > cols:
      cols = len(ps.problems.all())

  column_headers = ["problem{!r}".format(x) for x in range(1, (cols+1))]
  return column_headers

def ps_problem_headers(ps):
  #get all of the problem sets and return that (should be for a section... to do)
  column_headers = ['user']
  for problem in ps.problems.all():
    column_headers.append(problem.title)
  return column_headers

def sps_problem_headers(sps):
  #get all of the problem sets and return that (should be for a section... to do)
  column_headers = []
  for problem in sps.problem_set.problems.all():
    column_headers.append(problem.title)
  return column_headers

@admin.site.register_view('tables/')
def tables(request):

  ps_sets = models.ProblemSet.objects.all()
  problem_cols = max_len(ps_sets)
  cols = ['title','cs_sections']
  table = define_ps_table(cols, problem_cols)(ps_sets)
  context = {'problems':table}
  return render(request, 'admin/admin_tables.html', context)

@admin.site.register_view('section_results/')
def section_results(request):
  problems = models.Problem.objects.all()
  context = {'problems':problems}
  return render(request, 'admin/admin_tables.html', context)

def ps_results_getdata(ps):
  '''
  given a problem set, return a data set where the columns are the problems
  and the rows are the student is and their latest score
  '''
  data = []
  sps_sets = models.StudentProblemSet.objects.filter(problem_set=ps)
  print (ps.cs_section.all())
  #get all users in this section
  in_section = models.Reedie.objects.filter(enrolled__contains=ps.cs_section.all())
  print("did it work?")
  #for every user enrolled in this section, get the lastest for each problem in the set
  for user in in_section:
    print(user)
    scores = {}
    user_data = {'user':user}
    try:
      sps_set = models.StudentProblemSet.objects.get(user=user, problem_set=ps)
      for problem in ps.problems.all():
        try:
         sps_sol = models.StudentProblemSolution.objects.get(problem=problem, student_problem_set=sps_set)
         scores[problem.title] = (sps_sol.latest_score())
        except models.StudentProblemSolution.DoesNotExist:
          scores[problem.title] = "Problem Not (Yet) Attempted"
    #if the problem solution set doesn't exist, all the problem columns should be null
    except models.StudentProblemSet.DoesNotExist:
      scores = {problem.title: "Set Not (Yet) Attempted" for problem in ps.problems.all()}

    user_row = user_data.copy()
    user_row.update(scores)
    data.append(user_row)
  print(data)
  # for problem in ps.problems.all()
  #   #get student solutions
  #   sps_sets = models.StudentProblemSet.objects.filter(problem_set=ps)
  #   sps_sol = models.StudentProblemSolution.objects.get(problem=problem, student_problem_set=sps_set)

  return data

@admin.site.register_view('problemset_results/(?P<ps_id>[0-9]+)/')
def problemset_results(request, ps_id):
  ps = get_object_or_404(models.ProblemSet, pk=ps_id)
  data = ps_results_getdata(ps)
  column_headers = ps_problem_headers(ps)
  table = define_ps_table(column_headers)(data) 
  # sps_set = models.StudentProblemSet.objects.filter(problem_set=ps)
  # sps_sol = models.StudentProblemSolution.objects.filter()
  # cols = ['title']
  # column_headers = sps_problem_headers(sps_set[0])
  # table = define_table(column_headers)(sps_set) 
  context = {'problems':table}
  return render(request, 'admin/admin_tables.html', context)

