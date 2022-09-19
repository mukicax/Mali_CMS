from django.shortcuts import render
from django.views import generic
from .models import Kategorije, Potkategorije, Kupci, Proizvodi

class KategorijeListView(generic.ListView):
    model = Kategorije
    
    
class PotkategorijeListView(generic.ListView):  
    model = Potkategorije


class KupciListView(generic.ListView):  
    model = Kupci


class ProizvodiListView(generic.ListView):  
    model = Proizvodi

# -------------------- FORME

class KategorijeAddView(generic.CreateView):
    model = Kategorije
    fields = '__all__'

class PotkategorijeAddView(generic.CreateView):
    model = Potkategorije
    fields = '__all__'

class ProizvodiAddView(generic.CreateView):
    model = Proizvodi
    fields = '__all__'

class KupciAddView(generic.CreateView):
    model = Kupci
    fields = '__all__'
    #fields = ('ime', 'prezime', 'adresa', 'primedba', 'email', 'telefon')