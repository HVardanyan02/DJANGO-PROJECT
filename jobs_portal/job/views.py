from django.shortcuts import render

def index(request): 
    return render(request,'index.html',{})

def about(request): 
    return render(request,'about.html',{})

def contact(request): 
    return render(request,'contact.html',{})

def jobSingle(request): 
    return render(request,'job-single.html',{})

def postJob(request): 
    return render(request,'post-job.html',{})