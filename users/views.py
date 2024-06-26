from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    return render(request, "users/profile.html")

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User {username} created successfully")
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, "users/register.html", context)
