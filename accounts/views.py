from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import AvatarUploadForm
from .models import Profile
from django.shortcuts import get_object_or_404


def func_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out')
        return redirect('login')


# function to upload avatar
# @login_required
def func_profile(request):
    user = request.user
    #ava = user.user_profile.avatar.url
    instance = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = AvatarUploadForm()
    return render(request, 'pages/profile.html', {'form': form, 'user': user})
