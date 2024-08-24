from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterAdminForm
from payment.models import Wallet
from django.contrib.auth.models import User

# Admin views
def register_admin(request):
    if request.method == 'POST':
        form = RegisterAdminForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_staff = True
            var.save()
            Wallet.objects.create(user=var)
            messages.info(request, 'Admin account created successfully. Please login')
            return redirect('admin_login')
        else:
            messages.warning(request, 'Ooops Sorry. Something went wrong')
            return redirect('admin_register')
    else:
        form = RegisterAdminForm()
        context = {'form': form}
        return render(request, 'admin/register.html', context)

def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')  # Redirect to the Django admin dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin/custom_login.html')


def logout_admin(request):
    logout(request)
    return redirect('admin_login')

# Create your views here.
