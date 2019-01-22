from geopy.geocoders import Nominatim
geolocator = Nominatim()

location = geolocator.geocode("9.781074, 76.649662")
print(location.address)
print(location.latitude, location.longitude)

location1 = geolocator.geocode("Knoxfield, Australia")
print(location1.address)
print(location1.latitude, location1.longitude)

#from geolocation.main import GoogleMaps

#address = "New York City Wall Street 12"

#google_maps = GoogleMaps(api_key='AIzaSyDNHpu2_7QvJH5rvGRZN0F69r-GnAnlfFU')
#location = google_maps.search(location) # sends search to Google Maps.


#my_location = location.first() # returns only first location.

#print(my_location.city)
#print(my_location.lat)
#print(my_location.lng)

# import geocoder
# g = geocoder.ip('me')
# print(g.lat)
# print(g.lng)

#Bowser Crescent, Wangaratta, Rural City of Wangaratta, Hume, Victoria, 3677, Australia

# import js2py
#
# js = """
# function escramble_758(){
#     var txt ="";
#     if (navigator.geolocation) {
#         navigator.geolocation.getCurrentPosition(showPosition);
#     }
#     txt = ""+position.coords.latitude+":"+position.coords.longitude;
#     document.write(txt)
# }
# escramble_758()
# """.replace("document.write", "return ")
# result = js2py.eval_js(js)
# print("res:"+result)