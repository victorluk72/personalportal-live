from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for calendar.html page
@login_required(login_url='login')
def func_calendar(request):

    return render(request, 'calendar/calendar.html', {})
