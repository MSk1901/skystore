from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Prefetch, Subquery, OuterRef, TextField
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, BlogPost, Version


class ProductListView(LoginRequiredMixin, ListView):
    login_url = "users:login"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = self.model.objects.select_related(
            "category", "owner").prefetch_related(
            Prefetch("versions", queryset=Version.objects.filter(is_current=True))
        )
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['versions'] = product.versions.all()
        context['current_version'] = product.versions.filter(is_current=True).first()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    login_url = "users:login"

    def get_success_url(self):
        return reverse('catalog:item_url', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save(commit=False)
                self.object.owner = self.request.user
                self.object.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
                return super().form_valid(form)
            else:
                return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    login_url = "users:login"

    def get_success_url(self):
        return reverse('catalog:item_url', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        is_moderator = user.groups.filter(name='moderator').exists()
        if not is_moderator:
            FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                formset = FormSet(self.request.POST, instance=self.object)
            else:
                formset = FormSet(instance=self.object)
            context['formset'] = formset
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        if 'formset' in context_data:
            formset = context_data['formset']
            with transaction.atomic():
                if form.is_valid() and formset.is_valid():
                    self.object = form.save()
                    formset.instance = self.object
                    formset.save()
                    return super().form_valid(form)
                else:
                    return self.render_to_response(self.get_context_data(form=form, formset=formset))
        else:
            return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name='moderator').exists():
            return ModeratorProductForm
        else:
            return super().get_form_class()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
    login_url = "users:login"


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


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.is_published = True
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post', args=(self.object.slug,))


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:posts')