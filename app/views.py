from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from app.models import Confession

# Create your views here.


class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('confessions')


class Register(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('confessions')

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

        return context
