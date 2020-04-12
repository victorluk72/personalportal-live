from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#View function for shopping.html page
@login_required(login_url='login')
def func_shopping(request):

    return render(request, 'shopping/shopping.html', {})