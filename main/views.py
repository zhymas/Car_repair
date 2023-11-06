from django.http import JsonResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'main/main.html')


def about(request):
    return JsonResponse({"page": 'about'})


def contact(request):
    return JsonResponse({'page': 'contact'})
