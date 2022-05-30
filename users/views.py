from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForm


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')

    else:
        form = signupForm()
    context = {
        "form": form,
    }
    return render(request, 'users/signup.html', context)

