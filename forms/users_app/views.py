from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserCreationForm()

    return render(request,"registration/register.html",{"form":form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user_obj': request.user})
