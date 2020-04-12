from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for notes.html page
@login_required(login_url='login')
def func_notes(request):

    return render(request, 'notes/notes.html', {})
