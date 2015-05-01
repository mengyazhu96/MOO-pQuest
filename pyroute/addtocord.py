#!/usr/bin/python
import sys
from urllib2 import Request, urlopen, URLError
from urllib import quote
from json import loads

#move these
#ABSTRACT START
start_address = raw_input('Input starting address: ')

end_address = raw_input('Input destination: ')
#ABSTRACT END

# api call here

api_url_start = Request('http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}'.format(quote(start_address)))

api_url_end = Request('http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}'.format(quote(end_address)))

try:
    mapquest_reply_start = urlopen(api_url_start)
    mapquest_reply_end = urlopen(api_url_end)

    latlong_start = mapquest_reply_start.read()
    latlong_end = mapquest_reply_end.read()
  
    data_start = loads(latlong_start)
    data_end = loads(latlong_end)

    print data_start['results'][0]['locations'][0]['latLng']['lat']
    print data_start['results'][0]['locations'][0]['latLng']['lng']

    print data_end['results'][0]['locations'][0]['latLng']['lat']
    print data_end['results'][0]['locations'][0]['latLng']['lng']
  
except URLError, error:
     print 'Error: ', error