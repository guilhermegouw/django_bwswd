import imp
from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.quote_req, name="quote-request"),
]
