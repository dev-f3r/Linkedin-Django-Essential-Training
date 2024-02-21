from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from datetime import datetime

class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"
    success_url = "smart/notes"

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
