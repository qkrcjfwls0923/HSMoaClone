from django.contrib import admin
from django.urls import path

from .views import SetupApi, ShoppingMallApi, CategoryApi, ItemApi

urlpatterns = [
    path('setup', SetupApi.as_view()),
    path('mall', ShoppingMallApi.as_view()),
    path('category', CategoryApi.as_view()),
    path('item/<str:date>/<str:time>/<str:mall>/<str:category>/<str:orderby>', ItemApi.as_view())
]
