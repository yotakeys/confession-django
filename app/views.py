from django import template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from app.models import Confession

# Create your views here.


class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('confessionList')


class Register(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('confessionList')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('confessions')
        return super(Register, self).get(*args, **kwargs)


class ConfessionList(LoginRequiredMixin, ListView):
    model = Confession
    login_url = 'login'
    template_name = 'app/confession_list.html'
    context_object_name = "confessions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confessions'] = context['confessions'].filter(
            user=self.request.user)
        context['count'] = context['confessions'].count()

        return context


class ConfessionUrl(TemplateView):
    template_name = 'app/confession.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['confession'] = get_object_or_404(
            Confession, pk=self.kwargs['slug'],)

        return context


class CreateConfession(LoginRequiredMixin, CreateView):
    model = Confession
    fields = ['slug', 'sender', 'target', 'title', 'message']
    success_url = reverse_lazy('confessionList')
    template_name = 'app/confession_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateConfession, self).form_valid(form)


class DeleteConfession(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Confession
    context_object_name = 'confession'
    success_url = reverse_lazy('confessionList')
    template_name = 'app/confession_delete.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)  # noqa: E501
