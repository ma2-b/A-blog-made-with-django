from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse, reverse_lazy
from .forms import SingUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SingUpForm 
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm 
    template_name = 'registration/edit_profile.html'
    
    def get_success_url(self):
        return reverse('blog:posts')
    
    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm 
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('accounts:password_success')
 
    
def password_success(request):
    return render(request,'registration/password_success.html', {})

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args,**kwargs):
        # f = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
         
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile 
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','webiste_url','facebook_url','instagram_url']
    
    def get_success_url(self):
        return reverse('blog:posts')

    
    

    


     
    