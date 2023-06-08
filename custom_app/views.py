from django.shortcuts import render, redirect
from .models import User
from .forms import user_form
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

# Create your views here.


def home(request):
    if request.method == "GET":
        form = user_form
        return render(request, 'home.html', {'form': form})
    else:
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect("home")

    

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        

        user = auth.authenticate(email=email,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            # messages.info(request,'Incorrect username/password')
            return redirect('login')
        
    else:
        return render(request,'login.html')