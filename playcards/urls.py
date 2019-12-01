from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('openPack/', views.open_pack, name="openPack"),
    path('pack/', views.pack, name="pack"),
    path('create/', views.card_create, name="create"),
    path('delete/<int:pk>/', views.card_delete, name="delete"),
    path('API/get-card/<int:pk>/', views.get_card, name="get_card")
]
