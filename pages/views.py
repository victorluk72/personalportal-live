from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# View function for index.html page
@login_required(login_url='login')
def index(request):

    return render(request, 'pages/index.html', {})

# View function for login.html page
def login(request):
    #Check if request from form is POST, then perform logic
    if request.method == 'POST':
     #Get values from form "login"
     username=request.POST['username']
     password=request.POST['password']

     #Authenticate user
     user = auth.authenticate(username=username, password=password)

     if user is not None:
         auth.login(request, user)
         #messages.success(request, 'You are now logged in')
         return redirect ('index')
     else:
         messages.error(request, 'Invalid credentials, try again')  
         return redirect ('login')
    else:
        return render(request, 'pages/login.html', {}) 
 