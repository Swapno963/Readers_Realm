from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from .models import Reader
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    balance = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','balance','password1','password2']

    def save(self, commit =True):
        our_user = super().save(commit=True)
        our_user.save()

        balance = self.cleaned_data.get('balance')
        Reader.objects.create(
            user = our_user,
            balance = balance,
          
        )

        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                     'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })

class UwerLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(label='Enter Deposit Amount',initial=0)
    
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
