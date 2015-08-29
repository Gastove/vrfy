from django_tables2 import A
import django_tables2 as tables
from . import models
import itertools


def define_ps_table(columns):
  attrs = dict((c, tables.Column(empty_values=())) for c in columns)
  # attrs['user'] = tables.Column(empty_values=()))
  klass = type('DynamicTable', (ProblemSetResultTable,), attrs)
  return klass


class ProblemSetResultTable(tables.Table):
  row = tables.Column()
  def render_row_number(self):
    return 'Row %d' % next(self.counter)

  # class Meta:
  #   model = models.ProblemSet
  #   fields = ('problems',)
    # exclude = ('description', 'id')

  def __init__(self, *args, **kwargs):
    # print('hi')
    super(ProblemSetResultTable, self).__init__(*args, **kwargs)
    self.counter = itertools.count()

  def render_row_number(self):
    return '%d' % next(self.counter)
