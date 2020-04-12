from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for stocks.html page
@login_required(login_url='login')
def func_stocks(request):

    return render(request, 'stocks/stocks.html', {})
