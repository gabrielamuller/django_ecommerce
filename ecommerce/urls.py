from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import get_index
from accounts import urls as accounts_urls
from products.views import product_list
from django.views import static
from .settings import MEDIA_ROOT
from products import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
#from search import urls as urls_search
from products import urls as product_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', get_index, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^$', product_list, name='index'),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    #url(r'^search/', include(urls_search)),
    url(r'^products/', include(product_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]