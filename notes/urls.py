from django.urls import path
from notes import views

urlpatterns = [
    path('notes', views.NotesRegister.as_view(), name="notes"),
]
