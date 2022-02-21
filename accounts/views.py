from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    
    if(request.method == 'GET'):
        return render(request, 'register.html')
    elif (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']
        # messages.info(request, 'Account Created')
        
        if User.objects.filter(username = username).exists():
            messages.schoolname(request, 'Username Taken')#print('Username taken')
            return redirect('register')
            
        elif User.objects.filter(email=email).exists():
            messages.schoolname(request, 'Email already exists')#print('Email already Exists')
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.schoolname(request, 'User Created')#print('User Created')
            #return redirect('loginform')
            return render(request, 'loginform.html')
        #return render(request, 'loginform.html')
        
    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password) # This will return an object if the entered creds(username and password) are valid else user will be none
            
            if user is not None:
                auth.login(request, user)
                return redirect("home.html")
            else:
                messages.schoolname(request, "Invalid Credentials")
                return redirect('loginform')
        else:
            return render(request,'loginform.html')
        
    def logout(request):
        auth.logout(request)
        return redirect('/')
# Create your views here.
