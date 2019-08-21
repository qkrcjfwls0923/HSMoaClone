from django.contrib import admin
from django.urls import path

from .views import SetupView, ItemView

urlpatterns = [
    path('setup', SetupView.as_view()),
    path('item/<str:date>/<str:time>/<str:mall>/<str:category>/<str:orderby>', ItemView.as_view())
]
