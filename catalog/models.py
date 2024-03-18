from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NULLABLE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='владелец', to_field='email', default='admin@admin.ru')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.name}, ${self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.SET_NULL, default=None, **NULLABLE,
                                verbose_name='продукт')
    number = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='номер')
    name = models.CharField(max_length=50, verbose_name='название')
    is_current = models.BooleanField(verbose_name='текущая')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_images/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
