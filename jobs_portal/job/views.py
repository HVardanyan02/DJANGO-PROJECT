from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from job.forms import JobForm
from django.contrib.auth.models import User
from job.models import Job,Company

def index(request):
    return render(request, 'index.html', {})

# def job_list(request):
#     jobs = Job.objects.all()
#     print(":::::::::::::::::::::::::",jobs)
#     return render(request, 'index.html', {'jobs': jobs})


def job_board(request):
    companies = Company.objects.all()
    jobs = Job.objects.all()

    company_count = companies.count()
    job_count = jobs.count()

    print("Companies Count:", company_count)
    print("Jobs Count:", job_count)
    print("Companies:", companies)
    print("Jobs:", jobs)

    return render(request, 'job-listed-index.html', {
        'companies': companies,
        'jobs': jobs,
        'company_count': company_count,
        'job_count': job_count,
    })



@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def signup_login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')

# Sign Up
def signup_view(request):
    if request.method == "POST":
        email = request.POST.get('email') 
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')


        # if not email or not password or not re_password:
        #     messages.error(request, "All fields are required.")
        #     return redirect('signup')

        if password != re_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "A user with this email already exists.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=email, password=password)
            user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('signup')

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

# def login(request, user): 
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

