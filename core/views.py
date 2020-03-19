from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import ContactForm


User = get_user_model()


class IndexViewConta(TemplateView):

    template_name = 'index.html'


index = IndexViewConta.as_view()


def contato(request):
    template_name = 'contact.html'
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, template_name, context)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('login')


register = RegisterView.as_view()
