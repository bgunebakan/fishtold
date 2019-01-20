# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import *

def scan(request):
    return render(request, 'index.html')

def details(request,code):

    box = Box.objects.get(rfid_no=code)
    locations = Locations.objects.filter(fishing=box.fishing).order_by('-created_date')
    harbor_name = unicode(box.fishing.harbor.name)

    i = 0
    points = []
    #points.append([])
    for location in locations:
        if i<1:
            harbor_lat = location.position.latitude
            harbor_lon = location.position.longitude
        point = str(location.position.latitude)+","+str(location.position.longitude)
        points.append(point)
        #print location.position.latitude,",", location.position.longitude
    print harbor_name

    #points = ('-33.890542,151.274856', '-33.923036,151.259052', '-34.028249,151.157507', '-33.80010128657071,151.28747820854187')
    return render(request, 'customer.html',{'box': box,'locations':locations,'points': points,'harbor_lat':harbor_lat,'harbor_lon':harbor_lon,'harbor_name':harbor_name })


def write(request,code):

    box = Box.objects.get(rfid_no=code)
    locations = Locations.objects.filter(fishing=box.fishing).order_by('-created_date')
    harbor_name = unicode(box.fishing.harbor.name)
    print harbor_name
    print box.company.name
    i = 0
    points = []
    #points.append([])
    for location in locations:
        if i<1:
            harbor_lat = location.position.latitude
            harbor_lon = location.position.longitude
        point = str(location.position.latitude)+","+str(location.position.longitude)
        points.append(point)
        #print location.position.latitude,",", location.position.longitude

    print points
    print "---------------"
    #points = ('-33.890542,151.274856', '-33.923036,151.259052', '-34.028249,151.157507', '-33.80010128657071,151.28747820854187')
    print points
    return render(request, 'customer.html',{'box': box,'locations':locations,'points': points,'harbor_lat':harbor_lat,'harbor_lon':harbor_lon,'harbor_name':harbor_name })
