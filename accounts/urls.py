from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('edit_profile/',views.UserEditView.as_view(),name='edit_profile'),
    path('password/',views.PasswordsChangeView.as_view(),name='password_change'),
    path('password_success/',views.password_success,name='password_success'),   
    path('<int:pk>/profile/',views.ShowProfilePageView.as_view(),name='show_profile'), 
    path('<int:pk>/edit_profile_page/',views.EditProfilePageView.as_view(),name='edit_profile_page'),  
 
      
     
]


