from django import forms


class FormRegister(forms.Form):
   password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)
   password_repeat = forms.CharField(label='Powtórz hasło', max_length=100, widget=forms.PasswordInput)
   mail = forms.EmailField(label='Email', max_length=100)


class FormLogin(forms.Form):
   mail = forms.EmailField(label='Email', max_length=100)
   password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)


class ChangeProfileForm(forms.Form):
   first_name = forms.CharField(max_length=64)
   last_name = forms.CharField(max_length=64)
   mail = forms.EmailField(label='Email', max_length=100)
   password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
   password_new_repeat = forms.CharField(label='Repeat new password', max_length=100, widget=forms.PasswordInput)
   password_new = forms.CharField(label='New password', max_length=100, widget=forms.PasswordInput)