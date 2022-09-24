from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class LoginClassView(SuccessMessageMixin, LoginView):
    template_name = "login.html"

    def get_success_message(self, cleaned_data):
        return f"Hello {self.request.user}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Log in",
            title="Log in",
            classes="w-50",
            active_login="active"
        )
        return context


class RegisterClassView(SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "login.html"
    success_message = "Your profile was created successfully - you can log in"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Register",
            title="Register",
            classes="w-50",
            active_register="active"
        )
        return context

    success_url = reverse_lazy("users:login")
