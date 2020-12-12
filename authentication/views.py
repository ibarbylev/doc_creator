from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View

from authentication.forms import UserForm, ProfileForm, LoginForm


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Registration'
        context['user_form'] = UserForm()
        context['profile_form'] = ProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = User(
                username=user_form.cleaned_data['username'],
                email=user_form.cleaned_data['email'],
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
            )
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'auth/register.html', context)


# class LoginView(View):
#     template_name = 'auth/login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['login_form'] = LoginForm()
#         return context
#
#     def post(self, request):
#         login_form = LoginForm(request.POST)
#         # user = request.user
#         if login_form.is_valid():
#             user = login_form.get_user()
#             login(request, user)
#             # user.last_login = timezone.now()
#             user.save()
#
#             return redirect('index')
#
#         context = {
#             # 'user': user,
#             'login_form': login_form,
#         }
#         return render(request, 'auth/login.html', context)


def login_user(request):
    context = {'heading_text': 'Log In', 'login_form': LoginForm()}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            context = {
                'heading_text': 'Log In',
                'login_form': LoginForm(),
                'attention': f'The user with name {username} is not registered in the system!'}

        else:
            context = {'login_form': login_form}

    return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
