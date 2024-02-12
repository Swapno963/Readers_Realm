from django.urls import path
from .views import pass_change,edit_profile,UserRegistrationView,show_profile,UserLogoutView,add_money,UserLoginView,BorrowBookView,ReturnBook,add_comment
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='register'), 
   path('profile/',show_profile, name='profile'), 
   path('edit/',edit_profile, name='edit_profile'), 
   path('password_change/',pass_change, name='password_change'), 
   path('logout/', UserLogoutView.as_view(), name='logout'), 
   path('login/', UserLoginView.as_view(), name='login'), 
   path('deposit_money/', add_money, name='deposit_money'), 
   path('Borrow_book/<int:id>/', BorrowBookView.as_view(), name='borrow_book'), 
   path('ReturnBook/<int:id>/', ReturnBook.as_view(), name='ReturnBook'), 
   path('Comment/<int:id>/', add_comment, name='add_comment'), 
]
