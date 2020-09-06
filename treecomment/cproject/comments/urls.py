from django.urls import path

from .views import base_view

urlpatterns = [
    path('post-comments/', base_view)
]