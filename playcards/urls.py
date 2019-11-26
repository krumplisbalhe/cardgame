from django.conf.urls import url
from . import views

app_name = 'cards'

urlpatterns = [
    # url(r'^$', views.playcards_list, name="list"),
    url(r'^openPack/$', views.open_pack, name="openPack"),
    url(r'^pack/$', views.pack, name="pack"),
    url(r'^create/$', views.card_create, name="create")
]
