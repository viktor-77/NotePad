from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Note
from myapp.forms import NoteForm


class NoteHomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            'pages/index.html',
            {'notes': Note.objects.all(), 'form': NoteForm()}
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myapp:index")

        return render(
            request,
            'pages/index.html',
            {'notes': Note.objects.all(), 'form': form}
        )


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = "note"
    template_name = "pages/note_detail.html"
