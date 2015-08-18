from django.contrib import admin
from catalog.models import Reedie, Course, Section
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class ReedieInline(admin.StackedInline):
  model = Reedie
  can_delete = False

# class EnrollmentInline(admin.TabularInline):
#   model = Enrollment
#   extra = 1
#   verbose_name_plural = "Enrolled"

@admin.register(Reedie, site=admin.site)
class ReedieAdmin(admin.ModelAdmin):
  readonly_fields = ('first_name', 'last_name', 'email', 'last_updated')
  fieldsets = [
    ('Reed Profile Info', {'fields': ['user', 'first_name', 'last_name', 'last_updated', 'email', 'role']}),
  ]

# admin.site.unregister(User)
# @admin.register(User)
# class UserAdmin(UserAdmin):
#   inlines = (ReedieInline, )

@admin.register(Course, site=admin.site)
class CourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'sections')

  def sections(self, obj):
    sections = obj.section_set.all()
    if len(sections) is 0:
      return None
    else:
      return ", ".join([str(section) for section in obj.section_set.all()]) 

@admin.register(Section, site=admin.site)
class SectionAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Course Info', {'fields': ['course', 'section_id', 'prof', 'start_date', 'end_date']}),
    ('Enrolled Students', {'fields': ['enrolled']}),
  ]
  filter_vertical = ['enrolled']