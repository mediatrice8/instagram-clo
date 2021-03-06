from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome, name='welcome'),
    url(r'^like/(\d+)', views.like, name='like'),
    url(r'^$',views.profile,name = 'profile'),
    url(r'^$',views.timeline,name = 'timeline'),
    # url(r'^image/(\d+)', views.single_image, name='single_image'),
    url(r'^comment/(?P<id>\d+)', views.comment, name='comment'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^displays/', views.displays, name='displays'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),


]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

   
    
    