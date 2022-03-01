from django.conf.urls import url
from .views import *


app_name = 'robotapp'

urlpatterns = [

    url(r'^index/$',robot_index,name='index'),
    url(r'^secenekler/$',robot_choice,name='robot_choice'),
    url(r'^ne-yapmaliyim/$',robot_what2do,name='what2do'),

]