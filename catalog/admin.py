from django.contrib import admin

from catalog.models import Category, Product, BlogPost, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published',)
    list_filter = ('title',)
    search_fields = ('title', 'content',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'product', 'is_current',)
    list_filter = ('product', 'is_current',)
