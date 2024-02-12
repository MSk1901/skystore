from django.urls import path

from catalog.views import index, contacts, item

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/<int:pk>', item, name='item_url')
]
