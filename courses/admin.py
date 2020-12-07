from django.contrib import admin
from .models import Subject, Course, Module
from django.contrib import admin
admin.site.index_template = 'memcache_status/admin_index.html'

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module
    # admin.StackedInline, will not create a seperate tab for Module but will include the form for including the data of the module into Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    # This lines adds the input of the ModuleInline class into the CourseAdmin interface.