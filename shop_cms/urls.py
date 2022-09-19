from django.urls import path
from . import views

urlpatterns = [
    path('', views.KategorijeListView.as_view(), name = 'Proizvodi'),
    path('kategorije/', views.KategorijeListView.as_view(), name = 'Kategorije'),
    path('potkategorije/', views.PotkategorijeListView.as_view(), name = 'Potkategorije'),
    path('proizvodi/', views.ProizvodiListView.as_view(), name = 'Proizvodi'),
    path('kupci/', views.KupciListView.as_view(), name = 'Kupci'),



#=== ----------------------------------------- ruta za forme za dodavanje

    path('kategorije-add/', views.KategorijeAddView.as_view(), name = 'Kategorije-add'),
    path('potkategorije-add/', views.PotkategorijeAddView.as_view(), name = 'Potkategorije-add'),
    path('proizvodi-add/', views.ProizvodiAddView.as_view(), name = 'Proizvodi-add'),
    path('kupci-add/', views.KupciAddView.as_view(), name = 'Kupci-add'),
]