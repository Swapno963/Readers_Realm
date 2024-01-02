from django.urls import path
from .views import UserRegistrationView,show_profile,UserLogoutView
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='register'), 
   path('profile/',show_profile, name='profile'), 
   path('logout/', UserLogoutView.as_view(), name='logout'), 
   path('login/', UserRegistrationView.as_view(), name='login'), 
   path('deposit_money/', UserRegistrationView.as_view(), name='deposit_money'), 
]
