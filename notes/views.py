from django.views.generic import UpdateView,CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_delete.html"

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/admin"

    # Override the get_queryset method
    # Now returns all the notes of the logged user
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_details.html'