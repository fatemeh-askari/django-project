from django.shortcuts import render, redirect
from .forms import RegistrationForms
from .models import Account
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, "Register Successful!")
            return redirect('register')
    else:
        form = RegistrationForms()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return