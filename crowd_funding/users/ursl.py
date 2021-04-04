from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^profile$',views.index ),
    url(r'^deleteItem/(?P<pk>\d+)$', views.deleteItem,name='deleteItem'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
