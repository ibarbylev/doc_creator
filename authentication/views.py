from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from authentication.forms import UserForm, ProfileForm


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm()
        context['profile_form'] = ProfileForm()
        return context

    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
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


class LoginView:
    pass


class LogoutView:
    pass
