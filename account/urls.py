from django.urls import path
from .import views
from .views import home, donor_register, ngo_register, register

urlpatterns = [
    path('register/',views.register, name='register'),
    path('home/', views.home, name='home'),
    path('donor_register/',views.donor_register.as_view(), name='donor_register'),
    path('ngo_register/',views.ngo_register.as_view(),name='ngo_register'),
]


