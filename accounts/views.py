from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'User created successfully')
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) 