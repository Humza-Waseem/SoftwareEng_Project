from django.db import models
<<<<<<< HEAD
# from django.contrib.auth.models import User


# # Create your models here.
# class UserModel(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
   
#     REQUIRED_FIELDS = [email,password]
#     def __str__(self):
#         return self.username
=======

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
   
    REQUIRED_FIELDS = [email,password]
    def __str__(self):
        return self.username
>>>>>>> f66e0d9b6c7887c296ad5c4faeca1041fe625f37
    