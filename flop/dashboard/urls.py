from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'accounts/login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
