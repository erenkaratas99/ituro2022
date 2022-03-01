from django.conf.urls import url
from .views import *


app_name = 'konusmaciapp'

urlpatterns = [

    url(r'^index/$',konusmaci_index,name='index'),
    url(r'^(?P<slug>[\w-]+)/$',konusmaci_detail,name='detail'),

]