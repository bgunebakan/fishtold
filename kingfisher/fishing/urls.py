from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^rfid/scan/$', views.scan, name='scan'),
    url(r'^rfid/details/(?P<code>[\w-]+)/$', views.details, name='details'),
    url(r'^rfid/write/(?P<code>[\w-]+)/$', views.write, name='write'),
]
