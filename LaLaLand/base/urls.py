from django.contrib import admin
from django.urls import path
from django.urls import include
<<<<<<< HEAD
from django.contrib.auth.views import LoginView
=======

>>>>>>> f66e0d9b6c7887c296ad5c4faeca1041fe625f37
from . import views

from Auth import views as user_views    
urlpatterns = [
    
    path('', user_views.homepage, name='homepage'), 
<<<<<<< HEAD

    path('UserLogin/',user_views.UserLogin.as_view(), name = "UserLogin"),
    path('logout/'   ,user_views.UserLogout,name = "UserLogout"),
    path('register/' , user_views.registerUser,name = 'UserRegisteration'),

    path('guest/', user_views.GuestHomePage, name='GuestHomePage'),  
=======
    # path('login/',user_views.UserLogin,name = "UserLogin"),
    path('UserLogin/',user_views.UserLogin.as_view(), name = "UserLogin"),
    # path('login/', user_views.UserLogin.as_view(), name='UserLogin'),  
    path('logout/'   ,user_views.UserLogout,name = "UserLogout"),
    path('register/' , user_views.registerUser,name = 'register'),
    
    
    path('guest/', user_views.GuestHomePage, name='GuestHomePage'),  
    # path('home/', views.UserHomePage, name='UserHomePage'), 
    
>>>>>>> f66e0d9b6c7887c296ad5c4faeca1041fe625f37
    path('student/', views.student_profile, name='student_profile'),
    path('career_recommendations/<int:student_id>/', views.career_recommendations, name='career_recommendations'),
    path('startup/', views.startup_idea, name='startup_idea'),
    path('startup_results/<int:idea_id>/', views.startup_results, name='startup_results'),
]
