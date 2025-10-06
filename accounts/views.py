from django.shortcuts import render ,redirect
from .models import My_User
from .form import Create_UserForm , change_profileForm , LoginForm
from django.views.generic  import CreateView, DetailView ,UpdateView
from django.contrib.auth import   logout 
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView ,PasswordChangeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm


class create_user(CreateView):
    form_class = Create_UserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class login_user(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")


def logout_user(request):
    logout(request)
    return redirect("login")

class profile(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    model = My_User
    template_name = "registration/profile.html"
    context_object_name = "profile"

    def test_func(self):
        profile_to_update = self.get_object()
        return self.request.user == profile_to_update
    
class update_profile(LoginRequiredMixin,UserPassesTestMixin, UpdateView ):
    form_class = change_profileForm
    template_name = "registration/update_profile.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        profile_to_update = self.get_object()
        return self.request.user == profile_to_update
    
    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.object.pk})
    
class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    model = My_User
    form_class = PasswordChangeForm
    success_url = reverse_lazy("home")
    template_name = 'accounts/change_password.html'

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})
    
    
class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/reset_password.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')

class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_sent.html'

class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_complete')

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_done.html'