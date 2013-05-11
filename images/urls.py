from django.conf.urls import patterns, include, url

urlpatterns = patterns('images.views',
    url(r'^$', 'local_list', name='index'),
    url(r'^add_image$', 'add_image', name="add_image"),
    url(r'^view/(?P<id>\d+)$', 'image_view', name="image_view"),
    url(r'^filter/(?P<id>\d+)$', 'filter', name='filter'),
    url(r'^update/(?P<id>\d+)$', 'update', name='update'),
    url(r'^upload/(?P<id>\d+)$', 'upload', name='upload'),
    url(r'^download/(?P<id>\w+)$', 'download', name='download'),
    url(r'^delete/(?P<id>\d+)$', 'delete', name='delete'),
    url(r'^remote_delete/(?P<id>\w+)$', 'remote_delete', name='remote_delete'),
    url(r'^local_list$', 'local_list', name='local_list'),
    url(r'^remote_list$', 'remote_list', name='remote_list'),
    url(r'^sync_all$', 'sync_all', name='sync_all'),
)
