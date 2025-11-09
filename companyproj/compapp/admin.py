from django.contrib import admin
from .models import Employee , project

# Register your models here.
class ProjectInline(admin.TabularInline):
    model = project
    extra = 1
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')
    inlines = [ProjectInline]
