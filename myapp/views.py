from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Note
from myapp.forms import NoteForm


def index(request: HttpRequest) -> HttpResponse:
    form = NoteForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('myapp:index')

    return render(
        request,
        'pages/notepad.html',
        {'form': form, 'notes': Note.objects.all()}
    )


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = "pages/note_detail.html"
