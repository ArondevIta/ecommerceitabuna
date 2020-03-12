from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def contato(request):
    template_name = 'contact.html'
    return render(request, template_name)


def product_list(request):
    template_name = 'product_list.html'
    return render(request, template_name)


def product(request):
    template_name = 'product.html'
    return render(request, template_name)
