from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for photos.html page
@login_required(login_url='login')
def func_photos(request):

    return render(request, 'photos/photos.html', {})
