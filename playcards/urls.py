from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('openPack/', views.open_pack, name="openPack"),
    path('pack/', views.pack, name="pack"),
    path('create/', views.card_create, name="create"),
    path('delete/<int:pk>/', views.card_delete, name="delete"),
    path('play/', views.card_play, name="play"),
    path('API/get-card/<int:pk>/', views.get_card, name="get_card"),
    path('API/get-user/<int:pk>/', views.get_user, name="get_user"),
    path('API/get-pack/<int:pk>/', views.get_pack, name="get_pack")
]
