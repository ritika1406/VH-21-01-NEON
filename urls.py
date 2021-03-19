from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import home, donor_register, ngo_register, register

urlpatterns = [
    path('register/',views.register, name='register'),
    path('home/', views.home, name='home'),
    path('donor_register/',views.donor_register.as_view(), name='donor_register'),
    path('ngo_register/',views.ngo_register.as_view(),name='ngo_register'),
    path('login/',auth_views.LoginView.as_view(template_name = '../templates/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = '../templates/logout.html'),name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profileupdate/', views.profileUpdate, name = 'profileupdate'),
]


