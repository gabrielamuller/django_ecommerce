from django.conf.urls import url
from .views import product_list, do_search, product_details

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^search', do_search, name="search"),
    url(r'^(\d+)$', product_details, name='product_details'),
]