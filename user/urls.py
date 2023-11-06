from django.urls import path
from .views import RegisterUser, LoginUser, detail_user, logout_user

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='user_register'),
    path('login/', LoginUser.as_view(), name='user_login'),
    path('logout/', logout_user, name='logout'),
    path('area/', detail_user, name='detail_user')

]