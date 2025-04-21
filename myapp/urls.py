from django.urls import path

from myapp.views import index, NoteDetailView

app_name = 'myapp'

urlpatterns = [
    path("", index, name="index"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
]
