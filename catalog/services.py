from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories_cached():
    if settings.CACHE_ENABLED:
        categories = cache.get('categories')

        if not categories:
            categories = Category.objects.all()
            cache.set('categories', categories)
    else:
        categories = Category.objects.all()

    return categories
