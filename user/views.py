from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegisterForm, LoginUserForm


class RegisterUser(CreateView):
    template_name = 'user/user_create.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/user_login.html'

    def get_success_url(self):
        return '/'


def detail_user(request):
    if request.user.is_authenticated:
        return render(request, 'user/detail_user.html')
    else:
        return JsonResponse({'error': 'You are not authenticated'})


def logout_user(request):
    logout(request)
    return redirect('home')


def service(request):
    return render(request, 'user/service.html')
