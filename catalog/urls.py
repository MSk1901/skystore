from django.urls import path

from catalog.views import contacts, item, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', contacts),
    path('products/<int:pk>', item, name='item_url')
]
