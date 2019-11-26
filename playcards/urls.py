from django.conf.urls import url
from . import views

app_name = 'cards'

urlpatterns = [
    url(r'^$', views.playcards_list, name="list"),
    url(r'^create/$', views.card_create, name="create")
]
