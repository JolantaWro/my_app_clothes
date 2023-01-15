from django import forms


class FormRegister(forms.Form):
   password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)
   password_repeat = forms.CharField(label='Powtórz hasło', max_length=100, widget=forms.PasswordInput)
   mail = forms.EmailField(label='Email', max_length=100)


class FormLogin(forms.Form):
   mail = forms.EmailField(label='Email', max_length=100)
   password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)
