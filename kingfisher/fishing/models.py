# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django_geofield.fields import GeoPositionField
from django_google_maps import fields as map_fields

class Vessel(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='vessel_pictures/',null=True,default='vessel_pictures/vessel.png',verbose_name = "Tekne Fotoğrafı")
    fishing_license = models.ImageField(upload_to='licenses/',null=True,blank=True,verbose_name = "Av lisansı")
    hull_length = models.FloatField(default=0.0,verbose_name = "Tekne Boyu")
    score = models.FloatField(default=0.0,verbose_name = "Puanı")

    created_date = models.DateTimeField(default=timezone.now,verbose_name="Oluşturulma Tarihi")

    def __unicode__(self):
        return self.name

class Personnel_type(models.Model):
    name = models.CharField(
        max_length=30,
        error_messages={
        'unique': 'That personnel type is already saved.'
        }
        ,verbose_name = "Personel Tipi"
    )
    slug = models.CharField(max_length=30,verbose_name = "Kısa isim")
    icon = models.CharField(max_length=15,default="fa-users",verbose_name = "Icon")
    color = models.CharField(max_length=10,default="bg-yellow",verbose_name = "Renk")
    created_date = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False,verbose_name = "Silinmiş")

    def total(self):
        total = 0
        for type_ in Personnel.objects.filter(personnel_type=self):
            total = total + 1
        return total

    def __unicode__(self):
        return self.name

class Personnel(models.Model):
    Gender = (
            (1, 'Belirtilmemiş'),
            (2, 'Kadın'),
            (3, 'Erkek')
    )


    name = models.CharField(max_length=30,verbose_name = "İsim")
    surname = models.CharField(max_length=30,verbose_name = "Soyisim")
    country = CountryField(verbose_name = "Uyruğu",null=True)
    nat_id = models.CharField(max_length=12,unique=True,verbose_name = "TC No")
    gender = models.IntegerField(choices=Gender, default=1,verbose_name = "Cinsiyet")
    address = models.TextField(max_length=50,null=True,verbose_name = "Adres",blank=True)

    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True,default='profile_pictures/profile.png',verbose_name = "Profil Fotoğrafı")
    description = models.TextField(max_length=100,verbose_name = "Açıklama",null=True,blank=True)
    total_workday = models.IntegerField(verbose_name = "Toplam iş günü",default=0)
    total_workhour = models.IntegerField(verbose_name = "Toplam iş saati",default=0)

    personnel_type = models.ForeignKey(Personnel_type, null=True,on_delete=models.SET_NULL,verbose_name = "Personel Tipi")

    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name + " " + self.surname

class Harbor(models.Model):
    name = models.CharField(max_length=30,verbose_name = "İsim")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Oluşturulma Tarihi")

    def __unicode__(self):
        return self.name

class Fishing(models.Model):
    start_date = models.DateTimeField('Av Başlangıcı')
    end_date = models.DateTimeField('Av Bitişi')

    depot_level = models.FloatField(default=0.0,verbose_name = "Depo Seviyesi")
    depot_temp = models.FloatField(default=0.0,verbose_name = "Depo Sıcaklığı")
    harbor = models.ForeignKey(Harbor,null=True,verbose_name="Liman")

    lot_no = models.CharField(max_length=30,verbose_name = "Parti No")
    vessel = models.ForeignKey(Vessel,null=True,verbose_name="Tekne")
    personnels = models.ManyToManyField(Personnel)
    co2_emmission = models.FloatField(default=0.0,verbose_name = "CO2 salınımı")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Oluşturulma Tarihi")

    def __unicode__(self):
        return unicode(self.vessel) + " - " + unicode(self.start_date)


class Locations(models.Model):
    fishing = models.ForeignKey(Fishing,verbose_name="Av")
    position = GeoPositionField(db_index=True)
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Oluşturulma Tarihi")



class Company(models.Model):
    name = models.CharField(max_length=30,verbose_name = "Şirket Adı")
    address = models.TextField(max_length=50,null=True,verbose_name = "Adres",blank=True)
    tax_id = models.CharField(max_length=30,verbose_name = "Vergi No")
    score = models.FloatField(default=0.0,verbose_name = "Puanı")

    def __unicode__(self):
        return self.name

class Fish_type(models.Model):
    name = models.CharField(
        max_length=30,
        error_messages={
        'unique': 'That fish type is already saved.'
        }
        ,verbose_name = "Balık Cinsi"
    )
    slug = models.CharField(max_length=30,verbose_name = "Kısa isim")
    icon = models.CharField(max_length=15,default="fa-users",verbose_name = "Icon")
    color = models.CharField(max_length=10,default="bg-yellow",verbose_name = "Renk")
    created_date = models.DateTimeField(default=timezone.now)

    def total(self):
        total = 0
        for type_ in Personnel.objects.filter(personnel_type=self):
            total = total + 1
        return total

    def __unicode__(self):
        return self.name

class Box(models.Model):
    rfid_no = models.CharField(max_length=30,default="",verbose_name = "RFID no")
    fishing = models.ForeignKey(Fishing,verbose_name="Av",null=True)
    company = models.ForeignKey(Company,verbose_name="Şirket",null=True)
    fish_type = models.ForeignKey(Fish_type,verbose_name="Balık Cinsi",null=True)

    def __unicode__(self):
        return self.rfid_no

class Box_action(models.Model):
    date = models.DateTimeField(default=timezone.now)
    temp = models.FloatField(default=0.0,verbose_name = "Kasa Sıcaklığı")
    box = models.ForeignKey(Box,verbose_name="Kasa")

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
