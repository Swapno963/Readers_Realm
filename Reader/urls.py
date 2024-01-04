from django.urls import path
from .views import UserRegistrationView,show_profile,UserLogoutView,add_money,UserLoginView,BorrowBookView,ReturnBook
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='register'), 
   path('profile/',show_profile, name='profile'), 
   path('logout/', UserLogoutView.as_view(), name='logout'), 
   path('login/', UserLoginView.as_view(), name='login'), 
   path('deposit_money/', add_money, name='deposit_money'), 
   path('Borrow_book/<int:id>/', BorrowBookView.as_view(), name='borrow_book'), 
   path('ReturnBook/<int:id>/', ReturnBook.as_view(), name='ReturnBook'), 
]
