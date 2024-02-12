from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView
# Create your views here.
from django import forms
from django.shortcuts import get_object_or_404, redirect

from .forms import RegistrationForm,AddMoneyForm,ChangeUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Reader,Borrow_model
from django.views import View
from Books.models import Books, CommentModel
from Books.forms import CommentForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        print(form.cleaned_data)
        print('valid :', form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid : ",form.cleaned_data)

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
@login_required
def show_profile(request):
    user = request.user.reader
    borrow_history = Borrow_model.objects.filter(user=user)
    return render(request,'profile.html',{'user':user,'borrow_history':borrow_history})

@login_required
def add_money(request):
    
    form = AddMoneyForm(request.POST)
    # print('from add money : ',request.user)

    if request.method == 'POST' and form.is_valid():
        amount = form.cleaned_data['amount']
        user_account = Reader.objects.get(user=request.user)
        print(amount, user_account.email)



        # sending email
        message =f'Deposit done, amount {amount}'
        send_email = EmailMultiAlternatives('Deposit','',to=[user_account.email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()
        user_account.balance += amount
        user_account.save()
        #
        balance = user_account.balance
    user = request.user.reader
    return render(request,'add_money.html',{'form':form,'user':user})


class BorrowBookView(View):
    def get(self, request, id):
        book = get_object_or_404(Books,id=id)
        reader = Reader.objects.get(user = request.user)
        print("book :",book.borrow_price, "reader : ",reader.balance)
        # user_account = request.user


        if reader.balance >= book.borrow_price:
            reader.balance -= book.borrow_price
            reader.save()
            book.save()
            Borrow_model.objects.create(
                user=reader,
                book=book,
                IsBorrowed = True,
                  )
            message =f'Borrow Book done, Book price {book.borrow_price} is taken from you balance'
            send_email = EmailMultiAlternatives('Borrow','',to=[reader.email])
            send_email.attach_alternative(message, 'text/html')
            send_email.send()
        return redirect("profile")

class ReturnBook(View):
    def get(self, request, id):
        borrow = get_object_or_404(Borrow_model,id=id)
        try:
            print("Borrow price :",borrow.book.borrow_price)
            print("Is Borrow :",borrow.IsBorrowed)
            print("User balance :",borrow.user.balance)
            if borrow.IsBorrowed == True:
                borrow.user.balance += borrow.book.borrow_price
                borrow.IsBorrowed = False

                borrow.save()
                borrow.user.save()
            else:
                print("Vai, Ty sudu sudu chapcish kno,Aita False e to aace")
        except:
            print("holo nah")
        return redirect("profile")


def add_comment(request,id):
    form = CommentForm(request.POST)
    return render(request, 'add_comment.html', {'form':form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            # messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = ChangeUserForm(instance = request.user)
        user = request.user.reader
    return render(request, 'update_profile.html', {'form' : profile_form,'user':user})


@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    user = request.user.reader
    return render(request, 'pass_change.html', {'form' : form,'user':user})