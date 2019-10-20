from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User


urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_users, name='search_users'),
    url(r'^profile/(?P<username>[0-9]+)$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)