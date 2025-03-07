from django.shortcuts import render , redirect
from .forms import NewsleterForm,ContactUsForm

# Create your views here.

def home(request):
    return render(request,"core/home.html",{})


def newsleter(request):
    if request.method=="POST":
        form=NewsleterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
        
def contactus(request):
    if request.method == 'POST':
        form =ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactUsForm()
    
    return render(request,'core/contactus.html',{'form':form})