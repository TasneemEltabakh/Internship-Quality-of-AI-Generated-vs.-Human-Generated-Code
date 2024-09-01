from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
zipcode1 = "99501"
print("\nZipcode:",zipcode1)
location = geolocator.geocode(zipcode1)
print("Details of the said pincode:")
print(location.address) 
zipcode2 = "CA9 3HX"
print("\nZipcode:",zipcode2)
location = geolocator.geocode(zipcode2)
print("Details of the said pincode:")
print(location.address) 
zipcode3 = "61000"
print("\nZipcode:",zipcode3)
location = geolocator.geocode(zipcode3)
print("Details of the said pincode:")
print(location.address) 
zipcode4 = "713101"
print("\nZipcode:",zipcode4)
location = geolocator.geocode(zipcode4)
print("Details of the said pincode:")
print(location.address)
