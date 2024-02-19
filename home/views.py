from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required # No longer required

from datetime import datetime


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_content = {"today": datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"


# @login_required(login_url='/admin') # block the access if not login and redirect to authentication template
def authorized(request):
    return render(request, "home/authorized.html", {})
