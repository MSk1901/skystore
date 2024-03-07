from django.urls import path

from catalog.views import ContactView, ProductListView, ProductDetailView, BlogPostListView, BlogPostCreateView, \
    BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView, ProductUpdateView, ProductCreateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('products/create/', ProductCreateView.as_view(), name='create_item'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='update_item'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_item'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='item_url'),
    path('blog/', BlogPostListView.as_view(), name='posts'),
    path('blog/create/', BlogPostCreateView.as_view(), name='create_post'),
    path('blog/update/<int:pk>', BlogPostUpdateView.as_view(), name='update_post'),
    path('blog/<slug>', BlogPostDetailView.as_view(), name='post'),
    path('blog/delete/<int:pk>', BlogPostDeleteView.as_view(), name='delete_post'),
]
