from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignupForm

def index(request):
   items = Item.objects.filter(is_sold=False) [0:6]
   categories = Category.objects.all
   return render(request, 'core/index.html', {'items':items, 'categories':categories,})

def contact(request):
      return render(request, 'core/contact.html')

def signup(request):
   if request.method  == 'POST':
      form = SignupForm(request.POST)

      if form.is_valid():
         form.save()

         return redirect('/login/')

   else:
         form = SignupForm()

   return render(request, 'core/signup.html', {'form':form})


def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('core:login')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! Keeps user logged in.
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(user=request.user)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'w-full p-2 rounded-xl border'
    return render(request, 'core/change_password.html', {'form': form})

@login_required
def password_change_done(request):
    return render(request, 'core/password_change_done.html')








   