from django.core.exceptions import ValidationError
from django import forms

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control my-2"}),
            "text": forms.Textarea(attrs={"class": "form-control mb-5"})
            }
        labels = {"text": "Write your thoughts here:"}