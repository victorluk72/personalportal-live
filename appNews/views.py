from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for news.html page
@login_required(login_url='login')
def func_news(request):

    return render(request, 'news/news.html', {})