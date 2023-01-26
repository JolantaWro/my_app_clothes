from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from clothes.models import Donation, Category, Institution
from clothes.forms import FormRegister, FormLogin, ChangeProfileForm
import datetime


class LandingPage(View):
   def get(self, request):
       foundations = Donation.objects.filter(institution__type=1)
       organizations_non_governmenta = Donation.objects.filter(institution__type=2)
       local_collection = Donation.objects.filter(institution__type=3)
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
           "local_collection": local_collection,
           "organizations_non_governmenta": organizations_non_governmenta,
           "foundations": foundations,
           "quantity_sum": quantity_sum,
           "institution_sum": institution_sum,
       }
       return render(request, 'index.html', cnx)


class Register(View):
   def get(self, request):
       form = FormRegister()
       return render(request, 'register.html', {'form': form})

   def post(self, request):
       form = FormRegister(request.POST)
       if form.is_valid():
           first_name = form.cleaned_data.get('first_name')
           last_name = form.cleaned_data.get('last_name')
           password = form.cleaned_data.get('password')
           password_repeat = form.cleaned_data.get('password_repeat')
           mail = form.cleaned_data.get('mail')
           if User.objects.filter(username=mail).exists():
               raise ValidationError('Użytkownik już istnieje')

           if password != password_repeat:
               form.add_error(None, 'Wprowadzone różne hasła')

           new_user = User.objects.create_user(username=mail, password=password, email=mail, first_name=first_name, last_name=last_name)
           change_user = Permission.objects.get(codename='change_user')
           add_donation = Permission.objects.get(codename='add_donation')
           view_donation = Permission.objects.get(codename='view_donation')
           change_donation = Permission.objects.get(codename='change_donation')
           delete_donation = Permission.objects.get(codename='delete_donation')
           add_category = Permission.objects.get(codename='add_category')
           view_category = Permission.objects.get(codename='view_category')
           change_category = Permission.objects.get(codename='change_category')
           delete_category = Permission.objects.get(codename='delete_category')
           add_institution = Permission.objects.get(codename='add_institution')
           view_institution = Permission.objects.get(codename='view_institution')
           change_institution = Permission.objects.get(codename='change_institution')
           delete_institution = Permission.objects.get(codename='delete_institution')


           new_user.user_permissions.add(add_donation, view_donation, change_donation, delete_donation, add_category
                                         , view_category, change_category, delete_category, add_institution
                                         , view_institution, change_institution, delete_institution, change_user)

           new_user.save()
           return redirect('user_login')

       return redirect('user_login')


class Login(View):
   def get(self, request):
       form = FormLogin()
       return render(request, 'login.html', {'form': form})

   def post(self, request):
       form = FormLogin(request.POST)
       if form.is_valid():
           password = form.cleaned_data.get('password')
           username = form.cleaned_data.get('mail')
           user = authenticate(username=username, password=password)
           if user:
               login(request, user)
               return redirect('index')

           else:
               form.add_error(None, 'Błąd logowania')
               return redirect('user_register')
       return redirect('index')


class Logout(LoginRequiredMixin, View):
   def get(self, request):
       logout(request)
       return redirect('index')


class DonationAdd(LoginRequiredMixin, View):
   def get(self, request):
       categories = Category.objects.all()
       institutions = Institution.objects.all()
       cnx = {
           'categories': categories,
           'institutions': institutions,
       }
       return render(request, 'form.html', cnx)

   def post(self, request):
       pass
       # institution_name = request.POST.get("organization")
       # institution = get_object_or_404(Institution, name=institution_name)
       # print(institution)
       # quantity = request.POST.get("bags")
       # quantity_number = int(quantity)
       # street_address = request.POST.get("address")
       # city = request.POST.get("city")
       # zip_code = request.POST.get("postcode")
       # phone = request.POST.get("phone")
       # phone_number = int(phone)
       # print(phone_number, type(phone_number))
       # pick_up_date = request.POST.get("data")
       # date_test = pick_up_date.replace('-','.')
       # pick_up_time = request.POST.get("time")
       # time_test = pick_up_time.replace(':', '.')
       # time_test = int(time_test)
       # print(date_test)
       # print(time_test)
       # pick_up_comment = request.POST.get("more_info")
       # print(quantity_number,street_address, city, zip_code, phone_number, pick_up_comment)
       #
       # donation_add = Donation.objects.create(quantity=quantity_number, institution=institution,
       #                                        street_address=street_address, city=city, zip_code=zip_code,
       #                                        phone_number=phone_number, pick_up_date=datetime.date(date_test),
       #                                        pick_up_time=datetime.time(time_test), pick_up_comment=pick_up_comment)

       return redirect('donation_confirmation')


class DonationConfirmation(LoginRequiredMixin, View):

   def get(self, request):

       return render(request, 'formConfirmation.html')



class UserProfileView(LoginRequiredMixin, View):
   def get(self, request):
       user = request.user
       if user.is_authenticated:
           donations = Donation.objects.filter(user=request.user)

           return render(request, 'profile.html', context={'user': user, 'donations': donations})
       else:
           message = f"Widok tylko dla zalogowanych"
           return render(request, 'profile.html', context={'message': message})

class ChangeProfile(LoginRequiredMixin, View):

   def get(self, request, user_id):
       form = ChangeProfileForm()
       return render(request, 'profile_change.html', {'form': form})

   def post(self, request, user_id):
       form = ChangeProfileForm(request.POST)
       if form.is_valid():
           user = get_object_or_404(User, pk=user_id)
           password = form.cleaned_data.get('password')
           password_new = form.cleaned_data.get('password_new')
           password_new_repeat = form.cleaned_data.get('password_new_repeat')
           first_name = form.cleaned_data.get('first_name')
           last_name = form.cleaned_data.get('last_name')
           mail = form.cleaned_data.get('mail')
           userTest = authenticate(username=user.username, password=password)
           if userTest is not None:
               if password_new != password_new_repeat:
                   form.add_error('Wprowadzone hasła różnią się')
               user.first_name = first_name
               user.last_name = last_name
               user.email = mail
               user.set_password = password_new
               user.save()

           return redirect('index')
       return redirect('index')

