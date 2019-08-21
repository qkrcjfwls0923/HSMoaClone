from django.contrib import admin
from django.urls import path

from .views import SetupView

urlpatterns = [
    path('setup', SetupView.as_view()),
]
