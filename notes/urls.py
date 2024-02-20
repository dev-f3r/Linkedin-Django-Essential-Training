from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'), # pk is the note's id
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'), # pk is the note's id
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new')
]