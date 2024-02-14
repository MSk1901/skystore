from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {'objects': Product.objects.all}
    return render(request, 'main/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""Имя: {name}
Телефон: {phone}
Сообщение: {message}""")
    return render(request, 'main/contacts.html')


def item(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'main/item.html', context)
