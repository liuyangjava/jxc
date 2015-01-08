from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jxc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin.py', include(admin.site.urls)),
    url(r'^order/index.php', 'apps.orders.views.index'),
    url(r'^order/login.php', 'apps.orders.views.order_login'),
    url(r'^order/main.php', 'apps.orders.views.order_main'),
)
