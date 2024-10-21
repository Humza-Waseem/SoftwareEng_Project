from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
##http resonse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# @login_required(login_url="UserLogin")
def homepage(request):
   return render(request, 'Auth/homepage.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def GuestHomePage(request):
    return render(request, 'Auth/GuestHomePage.html')

@login_required(login_url="UserLogin")
def UserHomePage(request):
    return render(request, 'Auth/UserHomePage.html')


def UserLogout(request):  # creating this view to so that   
    logout(request)   # user presses the logout button then its session will be deleted from the database
    return redirect('homepage')   # and the user is redirected to the home page..

def registerUser(request):  
    # page = 'register' 
    # form = UserCreationForm()
    form = MyUserCreationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = MyUserCreationForm(request.POST)   # using MyUserCreationForm because it has our custom user model form
        if form.is_valid():
            user = form.save(commit=False)#commit = False means that we are not saving the form yet
            user.username = user.username
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')

    return render(request,'base/UserLogin.html',{'form':form})

class UserLogin(LoginView):
    template_name = 'Auth/UserLogin.html'
    fields = '__all__'
    
    
    redirect_authenticated_user = True # this allows us to redirect the user to the home page if they are already logged in. Meaning, if a user is already login we will not show the login page to him again even if the user enters the address in the search bar.
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    
# def UserLogin(request):
#     page  = 'login'
#     if request.user.is_authenticated: # if a authenticated user try to manually enter "/login" in the browser then we will restrict the Login page
#         return redirect('homepage') # and rediredct the user to the home page because uer is already logged in
    
#     if request.method == "POST":  
#         email = request.POST.get('email') # getting the email from the login form in lowercase
#         password = request.POST.get('password')  # getting the password from the login form
        
#         try:
#             user = User.objects.get(email=email) # getting the user with the specific username
#         except:
#             messages.error(request,"email does not exist")
        
#         user = authenticate(request,email =email,password= password )
#         if user is not None:
#             login(request,user)
#             return redirect('homepage')
#         else:
#             messages.error(request,"email or Password is incorrect")

#     context={'page':page}
#     return render(request,'Auth/UserLogin.html',context)