from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.front, name="front"),
    path("about/", views.about, name='about'),
    path("Contact/", views.Contact, name='Contact'),
]
