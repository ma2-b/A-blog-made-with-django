from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms 

class SingUpForm(UserCreationForm):
    email = forms.EmailField() 
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']
        
class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100) 
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField() 
    date_joined = forms.CharField(max_length=100)
    
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password','date_joined']
        

        
        
        
