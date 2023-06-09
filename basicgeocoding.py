from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from lxml.html import fromstring
import re
import csv
import pandas as pd

from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude
 

 # libraries from displaying images
 # from IPython.display import Image
 # from IPython.core.display import HTML

 # from IPython.display import display_html



 ## address we need geocode
loc = 'Taj Hotel,Mumbai,India'

# making an instance of Nominatim class
# geolocator = Nominatim(user_agent="my_request")
geolocator = Nominatim(user_agent="my_request")

# applying geocode method to get the location
# location = geolocator.geocode(loc)
location = geolocator.geocode(loc)

 # printing address and coordinates
print(location.address)
print((location.latitude, location.longitude))

"""**Reverse Geocoding**"""

locator = Nominatim(user_agent='myGeocoder')
coordinates = "18.921778, 72.8332848316978"
location = locator.reverse(coordinates)
location.raw
