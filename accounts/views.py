from django.shortcuts import render, redirect
from django.contrib import messages, auth    

def func_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out')
        return redirect('login')