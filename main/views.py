from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import *
from main.utils import DataMixin
from .models.post.models import Post

class show_post(DataMixin, ListView):
    model = Post
    template_name = 'main/show_post.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_res = self.get_user_context(title='Главная')
        return context | context_res


class register_user(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('show_post')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_res = self.get_user_context(title='Регистрация')
        return context | context_res


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('show_post')


class login_user(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_user_context(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return c_def | context

    def get_success_url(self):
        return reverse_lazy('show_post')

def logoutuser(request):
    logout(request)
    return redirect('login')

