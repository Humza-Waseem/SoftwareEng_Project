<<<<<<< HEAD
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    # Add the email field
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']  # Only include password1 and other fields you need

    def clean_password1(self):
        # Custom validation for password1 (you can add more complex rules)
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password
=======
# from django.forms import ModelForm
# from .models import Room,User
# from django.contrib.auth.forms import UserCreationForm

# class MyUserCreationForm(UserCreationForm):   #  creating a class that inherits properties from the UserCreationForm class,,,, We will 
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']  # this will create a form with all the fields of the User model,,,we can also take specific fields from the model and create a form with those fields only
    
#     #creating a class that inherits properties from the UserCreationForm class,,,, We will
>>>>>>> f66e0d9b6c7887c296ad5c4faeca1041fe625f37
