from django.contrib import admin
from .models import Kategorije, Potkategorije, Kupci, Proizvodi

admin.site.register(Kategorije)
admin.site.register(Potkategorije)
admin.site.register(Kupci)
admin.site.register(Proizvodi)