# user.set_password('admin123')
from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'contacts')

admin.site.register(Company, CompanyAdmin)

class SeekerAdmin(admin.ModelAdmin):
    list_display = ('user', 'education', 'experience')

admin.site.register(Seeker, SeekerAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('university', 'degree_name', 'start_date', 'completion_date')

admin.site.register(Education, EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'job_title', 'description')

admin.site.register(Experience, ExperienceAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_type', 'created_by_user', 'job_description')

admin.site.register(Job, JobAdmin)

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('job_name',)

admin.site.register(JobType, JobTypeAdmin)

class SeekerJobAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'job')

admin.site.register(SeekerJob, SeekerJobAdmin)




