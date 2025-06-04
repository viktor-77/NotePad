from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from myapp.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body']


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
