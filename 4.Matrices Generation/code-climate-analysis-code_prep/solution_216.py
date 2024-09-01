from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
state1 = "Uttar Pradesh"
print("State Name:",state1)
location = geolocator.geocode(state1)
print("State Name/Country Name: ")
print(location.address)
state2 = " Illinois"
print("\nState Name:",state2)
location = geolocator.geocode(state2)
print("State Name/Country Name: ")
print(location.address)
state3 = "Normandy"
print("\nState Name:",state3)
location = geolocator.geocode(state3)
print("State Name/Country Name: ")
print(location.address) 
state4 = "Jerusalem District"
print("\nState Name:",state4)
location = geolocator.geocode(state4)
print("State Name/Country Name: ")
print(location.address)
