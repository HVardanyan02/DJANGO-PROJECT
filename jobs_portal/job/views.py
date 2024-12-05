from django.shortcuts import render
from django.template.loader import render_to_string

def index(request): 
    return render(request,'index.html',{})

# def index(request):
#     navbar_html = render_to_string('/navbar.html')
#     return render(request, 'index.html', {'navbar_html': navbar_html})

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