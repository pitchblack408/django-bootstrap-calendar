from datetime import datetime
from django.utils.timezone import utc

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def welcome(request):
    return render(request, "website/welcome.html")

def redirect_to_calendar(request):
    response = redirect('/calendar')
    return response


def servertime(request):

    now = datetime.utcnow().replace(tzinfo=utc)
    return render(request, "website/servertime.html",
                  {"now": now})