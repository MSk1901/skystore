from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, CreateView
from pytils.translit import slugify

from catalog.models import Product, BlogPost


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
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


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:posts')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.is_published = True
            new_post.save()

        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost
