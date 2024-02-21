from django.views.generic import UpdateView,CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

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

    # Override the 'form_valid' method
    def form_valid(self, form):
        # Saves the form data to a model instance without commiting it to the database
        self.object = form.save(commit=False)
        # Sets the 'user' field of the note object to the logged user
        self.object.user = self.request.user
        # Saves the notel
        self.object.save()

        # Redirects to the success URL
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/login"

    # Override the get_queryset method
    # Now returns all the notes of the logged user
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_details.html'
    login_url = "/login"