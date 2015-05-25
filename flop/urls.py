from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = staticfiles_urlpatterns() + [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('flop.dashboard.urls', namespace='dashboard')),
]
