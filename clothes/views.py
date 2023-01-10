from django.shortcuts import render
from django.views import View


class LandingPage(View):
    def get(self, request):
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class DonationAdd(View):
    def get(self, request):
        return render(request, 'form.html')

