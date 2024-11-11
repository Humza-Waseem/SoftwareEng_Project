from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
##http resonse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import MyUserCreationForm
from django.contrib import messages



# @login_required(login_url="UserLogin")
def homepage(request):
   return render(request, 'Auth/homepage.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def GuestHomePage(request):
    return render(request, 'Auth/GuestHomePage.html')

@login_required(login_url="UserLogin")
def UserHomePage(request):
    return render(request, 'Auth/UserHomePage.html')






def registerUser(request):
    form = MyUserCreationForm()  # Initialize the form

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)  # Initialize form with POST data
        if form.is_valid():
            # Save the user (commit=False means we can modify before saving)
            user = form.save(commit=False)
            user.save()  # Save the user to the database

            # Log the user in automatically after registration
            login(request, user)
            messages.success(request, 'Registration successful')
            print('Registration successful')
            # Redirect to the home page or any page you prefer
            return redirect('homepage')  # Ensure 'home' is a valid URL pattern in your urls.py
        else:
            # If the form is invalid, display an error message
            print(form.errors)
            messages.error(request, 'An error occurred during registration')

    # Render the registration template with the form
    return render(request, 'Auth/UserLogin.html', {'form': form , 'page': 'register'} )


class UserLogin(LoginView):
    template_name = 'Auth/UserLogin.html'
    redirect_authenticated_user = True  # Redirects the user to the home page if the user is already logged in
    
    def get_success_url(self):
        return reverse_lazy('homepage')  # Redirect to 'homepage' after successful login
    
def UserLogout(request):    
    logout(request)   
    return redirect('homepage')   
