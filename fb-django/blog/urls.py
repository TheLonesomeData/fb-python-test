# blog/urls.py

from . import views
from django.urls import path


urlpatterns = [
    path("", views.create_author, name="create_author"),
]
