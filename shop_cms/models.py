from django.db import models
import uuid
from django.urls import reverse

class Kategorije(models.Model):
    naziv_kategorije = models.CharField(max_length=200)
    def __str__(self):
        return self.naziv_kategorije
    
    class Meta:
        verbose_name_plural = "Kategorije"#ne bi li u admin panelu pisalo Kategorijes 
        #(konvencionalno u Engleskom jeziku pluralna imenica sadrži s na kraju)

    def get_absolute_url(self):
        return reverse('Kategorije')

class Proizvodi(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4) # random ID za svaki proizvod bez kompromitovanja privatnosti
    naziv_proizvoda = models.CharField(max_length=200)
    opis_proizvoda = models.TextField(max_length=1000)
    # veza ka kupcima i potkategorijama,s'tim da moramo takođe biti sigurni da kad obrisemo nesto ne prsne tabela
    potkategorija_veza = models.ForeignKey('Potkategorije', on_delete=models.SET_NULL, null=True)
    kupac_veza = models.ForeignKey('Kupci', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Proizvodi'

    def __str__(self):
        return self.naziv_proizvoda

    def get_absolute_url(self):
        return reverse('Proizvodi')



class Potkategorije(models.Model):
    naziv_potkategorije = models.CharField(max_length=200)
    opis = models.TextField(max_length=4000)
    veza = models.ForeignKey('Kategorije', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.naziv_potkategorije

    class Meta:
        verbose_name_plural = "Potkategorije"

    def get_absolute_url(self):
        return reverse('Potkategorije')


class Kupci(models.Model):
    ime = models.CharField(max_length = 200)
    prezime = models.CharField(max_length = 200)
    adresa = models.TextField(max_length = 200)
    primedba = models.TextField(max_length = 1000)
    email = models.EmailField()
    telefon = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = 'Kupci'

    def __str__(self):
        return "{} {} - {} - {}".format(self.ime, self.prezime, self.email, self.primedba)

    def get_absolute_url(self):
        return reverse('Kupci')