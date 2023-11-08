from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import RegistrationCar


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
)
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class RegistrationCarForm(forms.ModelForm):
    class Meta:
        model = RegistrationCar
        fields = '__all__'
        exclude = ['user', 'status']

        widgets = {
            'model_of_car': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_problem': forms.TextInput(attrs={'class': 'form-control'}),
            'visit_time': forms.DateTimeInput()
        }
