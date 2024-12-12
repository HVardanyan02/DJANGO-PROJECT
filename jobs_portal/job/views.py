from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from job.forms import JobForm
from django.contrib.auth.models import User


def index(request): 
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Both fields are required.')
    
    return render(request, 'login.html')

def signUp(request):
    if request.method=="POST": 
        username = request.POST['email']
        password = request.POST['password']
        re_type_password = request.POST['re_type_password']
 
        if password != re_type_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/login')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return render(request, "index.html")
    return render(request, "login.html")

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

def login(request): 
    return render(request,'login.html',{})

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



# def company_list(request):
#     search_query = request.GET.get('search', '') 
#     region_query = request.GET.get('region', '')
#     companies = Company.objects.all()

#     if search_query:
#         companies = companies.filter(company_name__icontains=search_query)

#     if region_query:
#         companies = companies.filter(location__icontains=region_query)

#     return render(request, 'job-single.html', {'companies': companies})

# def create_job_view(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
#         if form.is_valid():
#             form.save()
#             print("Job successfully created.")
#             return redirect('job-single')
#         else:
#             print(form.errors) 
#     else:
#         form = JobForm()
#     return render(request, 'post-job.html', {'form': form})


