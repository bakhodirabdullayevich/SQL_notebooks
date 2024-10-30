from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import LoginForm


# Create your views here.
def login_function(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    context = {
        'form':forms
    }
    return render(request, 'login.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('index')
                messages.error(
                    request, 'Sizning akkauntingiz faol emas!')
                return render(request, 'login.html')
            messages.error(
                request, 'Notog`ri, boshqatdan urinib ko`ring!')
            return render(request, 'login.html')

        messages.error(
            request, 'Iltimos, login va parolni to`liq kiriting!')
        return render(request, 'login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')


@login_required
def logout_function(request):
    logout(request)
    messages.success(request, 'Siz tizimdan chiqdingiz!')
    return redirect('login')