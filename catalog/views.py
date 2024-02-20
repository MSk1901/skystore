from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""Имя: {name}
Телефон: {phone}
Сообщение: {message}""")
    return render(request, 'catalog/contacts.html')


def item(request, pk):
    context = {'object': get_object_or_404(Product, pk=pk)}
    return render(request, 'catalog/item.html', context)
