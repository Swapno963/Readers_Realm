from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView
# Create your views here.

from django.shortcuts import get_object_or_404, redirect

from .forms import RegistrationForm,AddMoneyForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Reader,Borrow_model
from django.views import View
from Books.models import Books



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
    if request.method == 'POST' and form.is_valid():
        amount = form.cleaned_data['amount']
        user_account = Reader.objects.get(user=request.user)
        # print(amount, user_account)
        user_account.balance += amount
        user_account.save()
        #
        balance = user_account.balance
    
    return render(request,'add_money.html',{'form':form})



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
        return redirect("profile")




class ReturnBook(View):
    def get(self, request, id):
        # print('request:', request,'id:',id)
        # book = get_object_or_404(Books,id=id)
        # user = get_object_or_404(Reader,user=request.user)
        borrow = get_object_or_404(Borrow_model,id=id)
        # reader = Reader.objects.get(user = request.user)
        # print("book :",book.borrow_price)
        # print("user :",user.balance)
        try:
            print("Borrow price :",borrow.book.borrow_price)
            print("Is Borrow :",borrow.IsBorrowed)
            print("User balance :",borrow.user.balance)
            if borrow.IsBorrowed == True:
                borrow.user.balance += borrow.book.borrow_price
                borrow.IsBorrowed = False

                borrow.save()
            else:
                print("Vai, Ty sudu sudu chapcish kno,Aita False e to aace")


            # print("_")
            # print("_")
            # print("_")
            # print("After Borrow price :",borrow.book.borrow_price)
            # print("Is Borrow :",borrow.IsBorrowed)
            # print("User balance :",borrow.user.balance)

        except:
            print("holo nah")

        # if borrow.IsBorrowed == True:
        #     user.balance += book.borrow_price
        #     user.save()
        #     borrow.IsBorrowed = False
        #     borrow.save()
        # user_account = request.user


        # if IsBorrowed == True:
        #     reader.balance += book.borrow_price
        # reader.save()
        # book.save()
        # Borrow_model.objects.create(
        #     IsBorrowed = False
        # )
        return redirect("profile")