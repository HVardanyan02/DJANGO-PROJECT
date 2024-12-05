from django.shortcuts import render, redirect
# from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def index(request): 
    return render(request,'index.html',{})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if not User.objects.filter(username=email).exists():
                messages.error(request, 'Invalid email')
                return redirect('login')
            
            user = authenticate(username=email, password=password)
            
            if user is None:
                messages.error(request, "Invalid Password")
                return redirect('login')
            else:
                login(request, user)
                return redirect('index')
    
    return render(request, 'login.html')

def signUp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_type_password = request.POST.get('re_type_password')
        
        if password != re_type_password:
            messages.error(request, "Passwords do not match")
            return redirect('login')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect('login')
        
        user = User.objects.create_user(username=email, password=password)
        user.save()
        
        login(request, user)
        messages.success(request, "Registration successful")
        return redirect('index')
    
    return render(request, 'login.html', {})

def about(request): 
    return render(request,'about.html',{})

def contact(request): 
    return render(request,'contact.html',{})

def jobSingle(request): 
    return render(request,'job-single.html',{})

def postJob(request): 
    return render(request,'post-job.html',{})

def blog(request): 
    return render(request,'blog.html',{})

# def login(request): 
#     return render(request,'login.html',{})

def blogSingle(request): 
    return render(request,'blog-single.html',{})

def services(request): 
    return render(request,'services.html',{})

def serviceSingle(request): 
    return render(request,'service-single.html',{})

def gallery(request): 
    return render(request,'gallery.html',{})

def faq(request): 
    return render(request,'faq.html',{})

def testimonials(request): 
    return render(request,'testimonials.html',{})

def portfolio(request): 
    return render(request,'portfolio.html',{})

def portfolioSingle(request): 
    return render(request,'portfolio-single.html',{})




