from django.urls import path

from catalog.views import ContactView, item, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('products/<int:pk>', item, name='item_url')
]
