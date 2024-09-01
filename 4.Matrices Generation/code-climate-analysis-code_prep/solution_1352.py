from geopy import distance
london = ("51.5074 N, 0.1278 W")
newyork = ("40.7128 N, 74.0060 W")
print("Distance between London and New York city (in km):")
print(distance.distance(london, newyork).km," kms")
