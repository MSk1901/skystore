from django.db import models


class Product(models.Model):

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
