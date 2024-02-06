from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
] + static(settings)
