from django.shortcuts import render
from django.views import View
from clothes.models import Donation


class LandingPage(View):
    def get(self, request):
        quantity_sum = 0
        institution_sum = 0
        quantity_for_sum = Donation.objects.values_list('quantity', flat=True)
        if len(quantity_for_sum) == 0:
            quantity_sum = 0
        else:
            for quantity in quantity_for_sum:
                quantity_sum += quantity
        institution_for_sum = Donation.objects.values_list('institution', flat=True)
        if len(institution_for_sum) == 0:
            institution_sum = 0
        else:
            for _ in institution_for_sum:
                institution_sum += 1

        cnx = {
            "quantity_sum": quantity_sum,
            "institution_sum": institution_sum,
        }
        return render(request, 'index.html', cnx)


class Register(View):
    def get(self, request):
        return render(request, 'register.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class DonationAdd(View):
    def get(self, request):
        return render(request, 'form.html')

