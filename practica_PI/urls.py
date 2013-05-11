from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import images.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica_PI.views.home', name='home'),
    # url(r'^practica_PI/', include('practica_PI.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^images/', include(images.urls)),
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
