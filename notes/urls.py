from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()) # pk is a parameter for detail view
]