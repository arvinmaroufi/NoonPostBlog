from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

def signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request,'registration\signup.html', {'form':form}) 



# class Signup(generic.CreateView):
#     form_class=UserCreationForm
#     template_name="registration\signup.html"
#     success_url=reverse_lazy('login')