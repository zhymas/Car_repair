from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegisterForm, LoginUserForm
from datetime import datetime
from .models import RegistrationCar


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
    all_time = [
        '09:00', '10:00',
        '11:00', '12:00', '13:00',
        '14:00', '15:00', '16:00',
        '17:00', '18:00', '19:00']

    yesterday = datetime.today()
    min_day_value = yesterday.strftime('%Y-%m-%d')

    context = {
        'min_day_value': min_day_value,
        'all_time': all_time,
    }
    if request.method == "POST":
        user = request.user
        model = request.POST.get('model-car', '')
        problem = request.POST.get('type-of-problem', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')

        errors = []
        if not model:
            errors.append('Please write models of your cars.')
        if not problem:
            errors.append('Please write type of problem.')
        if not date:
            errors.append('Please select date.')
        if errors:
            context.update({'errors': errors})

        if not errors:
            car = RegistrationCar(user=user, model_of_car=model, type_of_problem=problem, visit_date=date, visit_time=time)
            car.save()
            return redirect('home')

    return render(request, 'user/service.html', context)


