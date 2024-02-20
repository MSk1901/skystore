from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""Имя: {name}
Телефон: {phone}
Сообщение: {message}""")
        return render(request, self.template_name)


def item(request, pk):
    context = {'object': get_object_or_404(Product, pk=pk)}
    return render(request, 'catalog/item.html', context)
