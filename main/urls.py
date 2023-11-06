from django.urls import path, include
from .views import home_page, about, contact

urlpatterns = [
    path('', home_page, name='home'),
    path('user/', include('user.urls')),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]
