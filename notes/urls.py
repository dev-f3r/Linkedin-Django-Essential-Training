from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.list),
    path('notes/<int:pk>', views.detail) # pk is a parameter for detail view
]