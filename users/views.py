from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm
from payment.models import Wallet

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            Wallet.objects.create(user=var)
            messages.info(request, 'Account created successfully. Please login')
            return redirect('login')
        else:
            messages.warning(request, 'Ooops Sorry. Something went wrong')
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {'form' : form}
        return render(request, 'users/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Ooops Sorry. Something went wrong')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')

    


# Create your views here.
