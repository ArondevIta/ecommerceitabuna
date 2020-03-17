from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import View, TemplateView

from .forms import ContactForm


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


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


def product_list(request):
    template_name = 'product_list.html'
    return render(request, template_name)


def product(request):
    template_name = 'product.html'
    return render(request, template_name)
