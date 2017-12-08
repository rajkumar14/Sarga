from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

# Create your views here.
def index_view(request):
    return render(request,'base.html',locals())
    
    
def home_view(request):
    return render(request,'home.html',locals())
    
### Contact us save the data
def contact_us(request):
    if request.method == 'POST':
        # Get parameters
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Save contact in Contact table
        contact = Contactus.objects.create(first_name=fname,last_name=lname,email=email,message=message)
        return HttpResponseRedirect("/contact-us/")
    return render(request,'contact-us.html',locals())
    
# About us 
def about_us(request):
    return render(request,'about-us.html',locals())
    
def services(request):
    return render(request,'services.html',locals())
    
def portfolio(request):
    return render(request,'portfolio.html',locals())
    
def blog(request):
    return render(request,'blog.html',locals())
    
def career(request):
    return render(request,'career.html',locals())
    
def faq(request):
    return render(request,'faq.html',locals())
    
def terms(request):
    return render(request,'terms.html',locals())
    
def privacy(request):
    return render(request,'privacy.html',locals())
    
def registration(request):
    return render(request,'registration.html',locals())
    
def typography(request):
    return render(request,'typography.html',locals())
    
def company_location(request):
    return render(request,'map.html',locals())
    
def company_coordinate(request):
    queryset = HospitalDetails.objects.all()
    get_maps = []
    ### Hospital get all lattitude and longitude showed in map
    for mp in queryset:
        loc = {}
        if mp.lattitude and mp.longitude:
            uname = mp.title;
            loc.update(name=uname,coordinates=[float(mp.lattitude), float(mp.longitude)])
            get_maps.append(loc)
    return JsonResponse(get_maps, safe=False)
