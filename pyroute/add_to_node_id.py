#!/usr/bin/python
import sys
import urllib2rror



#move these
start_address = raw_input('Input starting address: ')

end_address = raw_input('Input destination: ')

# api call here

api_url_start = Request('http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}&callback=renderGeocode'.format(start_address))

api_url_end = Request('http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluu82q0bnl%2Caa%3Do5-94yxlf&location={}&callback=renderGeocode'.format(end_address))

try:
  mapquest_reply_start = urlopen(api_url_start)
  mapquest_reply_end = urlopen(api_url_end)
  latlong_start = mapquest_reply_start.read()
  latlong_end = mapquest_reply_end.read()
except URLError, error:
  print 'Problem!', error
  