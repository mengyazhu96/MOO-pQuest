#!/usr/bin/python
import sys
from urllib2 import Request, urlopen, URLError

#move these
start_address = raw_input('Input starting address: ')

end_address = raw_input('Input destination: ')

# api call here

api_url_start = Request('http://www.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}&callback=renderGeocode.'.format(start_address))

api_url_end = Request('http://www.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}&callback=renderGeocode.'.format(end_address))

try:
    mapquest_reply_start = urlopen(api_url_start)
    mapquest_reply_end = urlopen(api_url_end)
    latlong_start = mapquest_reply_start.read()
    latlong_end = mapquest_reply_end.read()
  
    data_start = json.loads(latlong_start)
    data_end = json.loads(latlong_end)

    print["results"]["locations"]["latLng"]["lng"]
    print["results"]["locations"]["latLng"]["lat"]
  
except URLError, error:
     print 'Error: ', error