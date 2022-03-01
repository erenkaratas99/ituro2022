from django.conf.urls import url
from .views import *


app_name = 'eventapp'

urlpatterns = [

    url(r'^gorus-belirt/$', present_opinion, name='opinion'),
    url(r'^ani-birak/$', upload_photo, name='photo'),
    url(r'^kat-plani/$', plan_view, name='floors'),
    url(r'^gunler/$', days_choice, name='days_choice'),
    url(r'^gunler/konusmalar/$', days_view, name='days'),
    url(r'^gunler/yarismalar/$', days_competetion_view, name='days_competetions'),


]