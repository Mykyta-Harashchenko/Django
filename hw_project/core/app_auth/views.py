from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from core.app_auth.models import Profile
from core.app_auth.forms import RegisterForm, ProfileForm


class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(f'Form is received')
        if form.is_valid():
            print(f'Form is valid')
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Вітаємо, {username}. Ваш аккаунт успішно створено')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})
    
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quotes:root')
        else:
            messages.error(request, 'Невірний пароль або логін')
            return render(request, 'app_auth/login.html')
        
    return render(request, 'app_auth/login.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='app_auth:profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app_auth/profile.html', {'profile_form': profile_form})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')


