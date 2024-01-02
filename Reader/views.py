from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.

from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    



class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
@login_required
def show_profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})