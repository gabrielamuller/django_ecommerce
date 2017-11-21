from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import get_index
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'^accounts/', include(accounts_urls))
]