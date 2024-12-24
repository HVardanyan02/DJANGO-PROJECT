from django.contrib import admin
from .models import Company, Seeker, Education, Experience, Job, JobType, SeekerJob

# Registering the Company model
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'description', 'company_website_url', 'contacts')
    search_fields = ('company_name', 'location', 'contacts')
    list_filter = ('location',)

# Registering the Seeker model
@admin.register(Seeker)
class SeekerAdmin(admin.ModelAdmin):
    list_display = ('user', 'education', 'experience')
    search_fields = ('user__username', 'education__university', 'experience__job_title')

# Registering the Education model
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('university', 'degree_name', 'start_date', 'completion_date')
    search_fields = ('university', 'degree_name')
    list_filter = ('start_date', 'completion_date')

# Registering the Experience model
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'start_date', 'end_date', 'description')
    search_fields = ('job_title',)
    list_filter = ('start_date', 'end_date')

# Registering the Job model
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'job_type', 'created_by_user', 'job_description')
    search_fields = ('job_title', 'company__company_name', 'job_type__job_name', 'created_by_user__username')
    list_filter = ('company', 'job_type')

# Registering the JobType model
@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('job_name',)
    search_fields = ('job_name',)

# Registering the SeekerJob model
@admin.register(SeekerJob)
class SeekerJobAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'job')
    search_fields = ('seeker__user__username', 'job__job_title')




# # user.set_password('admin123')
# from django.contrib import admin
# from .models import *

# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('company_name', 'location', 'contacts')

# admin.site.register(Company, CompanyAdmin)

# class SeekerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'education', 'experience')

# admin.site.register(Seeker, SeekerAdmin)

# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('university', 'degree_name', 'start_date', 'completion_date')

# admin.site.register(Education, EducationAdmin)

# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('start_date', 'end_date', 'job_title', 'description')

# admin.site.register(Experience, ExperienceAdmin)

# class JobAdmin(admin.ModelAdmin):
#     list_display = ('company', 'job_type', 'created_by_user', 'job_description')

# admin.site.register(Job, JobAdmin)

# class JobTypeAdmin(admin.ModelAdmin):
#     list_display = ('job_name',)

# admin.site.register(JobType, JobTypeAdmin)

# class SeekerJobAdmin(admin.ModelAdmin):
#     list_display = ('seeker', 'job')

# admin.site.register(SeekerJob, SeekerJobAdmin)




