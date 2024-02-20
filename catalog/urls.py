from django.urls import path

from catalog.views import ContactView, ProductListView, ProductDetailView, BlogPostListView, BlogPostCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='item_url'),
    path('blog/', BlogPostListView.as_view(), name='posts'),
    path('blog/create/', BlogPostCreateView.as_view(), name='create_post')
]
