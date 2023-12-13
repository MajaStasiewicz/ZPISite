
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django import forms
from django.urls import reverse_lazy

#class PasswordsChangeView(PasswordChangeView):
#    form_class = PasswordChangeForm
#    success_url = reverse_lazy('/home/')
    
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, label="Imię")
    last_name = forms.CharField(max_length=100, label="Nazwisko")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

