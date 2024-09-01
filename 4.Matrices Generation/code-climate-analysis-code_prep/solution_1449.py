from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "47.470706, -99.704723"
print("Latitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald = "34.05728435, -117.194132331602"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald = "38.8976998, -77.0365534886228"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald = "55.7558 N, 37.6173 E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald = "35.6762 N, 139.6503 E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald = "41.9185 N, 45.4777 E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
