from django.db import models
from django.contrib.auth.models import User

# class UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     role_name = models.CharField(max_length=50)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company_website_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    contacts = models.CharField(max_length=50, blank=True, null=True)

class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.ForeignKey('Education', on_delete=models.CASCADE)
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)

class Education(models.Model):
    university = models.CharField(max_length=50)
    degree_name = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)

class Experience(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.ForeignKey('JobType', on_delete=models.SET_NULL, blank=True, null=True)
    created_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    job_description = models.TextField()

class JobType(models.Model):
    job_name = models.CharField(max_length=50)

class SeekerJob(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)