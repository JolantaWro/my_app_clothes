"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clothes.views import LandingPage, Register, Login, DonationAdd, Logout, UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', LandingPage.as_view(), name="index"),
    path('user_register', Register.as_view(), name="user_register"),
    path('user_login', Login.as_view(), name="user_login"),
    path('user_logout', Logout.as_view(), name="user_logout"),
    path('user_profile', UserProfileView.as_view(), name="user_profile"),
    path('donation_add', DonationAdd.as_view(), name="donation_add"),
]