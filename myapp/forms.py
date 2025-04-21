from django import forms

from myapp.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body']
