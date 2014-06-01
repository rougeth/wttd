from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),

    url(r'^inscricao/$', 'subscriptions.views.subscribe', name='subscribe'),
    url(r'^inscricao/(\d+)/$', 'subscriptions.views.detail', name='detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
