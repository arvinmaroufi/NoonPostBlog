from django.shortcuts import render , redirect
from .forms import NewsleterForm,ContactUsForm
from .models import SiteSetting

# Create your views here.

def home(request):
    site_settings = SiteSetting.objects.first()
    
    context = {    
        'site_settings':site_settings
    }
    return render(request,"core/home.html",context)


def newsleter(request):
    if request.method=="POST":
        form=NewsleterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
        
def contactus(request):
    site_settings = SiteSetting.objects.first()
    if request.method == 'POST':
        form =ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactUsForm()
        
    context = {
        'form':form,
        'site_settings':site_settings
    }
    return render(request,'core/contactus.html',context)


def about_us(request):
    site_settings = SiteSetting.objects.first()
    
    context = {    
        'site_settings':site_settings
    }
    return render(request,"core/aboutus.html",context)
