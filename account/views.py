from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from account.forms import Login


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:main')
    else:
        form = Login()

    return render(request, 'account/login.html', {'form': form})


def register_view(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('passwords are not match!')
            return render(request, 'account/register.html', context)

        user = User.objects.create(username=username, email=email)
        user.set_password(password1)
        user.save()
        login(request, user)
        return redirect('home:main')

    return render(request, 'account/register.html', {})


def logout_view(request):
    logout(request)
    return redirect('home:main')

