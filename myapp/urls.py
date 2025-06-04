from django.urls import path

from myapp.views import (
    NoteHomeView, NoteDetailView, SignupView,
)

app_name = 'myapp'

urlpatterns = [
    path("", NoteHomeView.as_view(), name="index"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("signup/", SignupView.as_view(), name="signup"),
]
