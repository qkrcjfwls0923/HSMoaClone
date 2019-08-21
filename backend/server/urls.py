from django.contrib import admin
from django.urls import path

from .views import SetupView, ShoppingMallView, CategoryView, ItemView

urlpatterns = [
    path('setup', SetupView.as_view()),
    path('mall', ShoppingMallView.as_view()),
    path('category', CategoryView.as_view()),
    path('item/<str:date>/<str:time>/<str:mall>/<str:category>/<str:orderby>', ItemView.as_view())
]
