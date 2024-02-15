from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import datetime

def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required # block the access if not login
def authorized(request):
    return render(request, 'home/authorized.html', {})