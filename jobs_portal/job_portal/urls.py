"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('about.html', views.about, name = 'about'),
    path('contact.html', views.contact, name = 'contact'),
    path('job-single.html', views.jobSingle, name = 'job-single'),
    path('post-job.html', views.postJob, name = 'post-job'),
    path('blog.html', views.blog, name = 'blog'),
    path('login.html', views.login, name = 'login'),
    path('blog-single.html', views.blogSingle, name = 'blog-single'),
    path('services.html', views.services, name = 'services'),
    path('service-single.html', views.serviceSingle, name = 'service-single'),
    path('gallery.html', views.gallery, name = 'gallery'),
    path('faq.html', views.faq, name = 'faq'),
    path('testimonials.html', views.testimonials, name = 'testimonials'),
    path('portfolio.html', views.portfolio, name = 'portfolio'),
    path('portfolio-single.html', views.portfolioSingle, name = 'portfolio-single'),
]
