from django.shortcuts import render , redirect
from .forms import NewsleterForm

# Create your views here.

def home(request):
    return render(request,"core/home.html",{})


def newsleter(request):
    if request.method=="POST":
        form=NewsleterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")