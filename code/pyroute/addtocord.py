#!/usr/bin/python
import sys
from urllib2 import Request, urlopen, URLError
from urllib import quote
from json import loads

def addtocord (address):
    #api_url_start = Request('http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}'.format(quote(address)))
    # api call here
    #https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY

    api_url_start = Request('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyC7O0omzfxKfWfx_7kVZrvAWk60Ld0Y_7M'.format(quote(address)))
    try:
        google_reply_start = urlopen(api_url_start)

        latlong_start = google_reply_start.read()
      
        data_start = loads(latlong_start)

        print data_start['results'][0]['geometry']['location']['lat'],data_start['results'][0]['geometry']['location']['lng']
        return (data_start['results'][0]['geometry']['location']['lat'], data_start['results'][0]['geometry']['location']['lng'])

    except URLError, error:
         print 'Error: ', error