from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # lets grab the username for the time being
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully! Please login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# @login_required(login_url='login')
@login_required()
def profile(request):
    return render(request, 'users/profile.html')
    # instead of writing the login_url here, we can also write it in the settings.py file