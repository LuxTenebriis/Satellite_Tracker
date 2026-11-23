# main.py

# Set up
from geopy.geocoders import Nominatim

print("★ Satellite Tracker ★", r"\n\n")

sat_name = "ISS"
print("☆", sat_name)

# Input user location w geolocator ---------------------------------------------
geolocator = Nominatim(user_agent="lux_sat_tracker_learning")

while True:
    location_in = input("☆ Enter your city, state/region, and country: ")
    location = geolocator.geocode(location_in, timeout = 10)

    # if location valid, print location and corresponding lat/long
    # else ask to input again

    if location_in is not None:
        observer_lati = location.latitude
        observer_long = location.longitude

        print("Analysing location...")
        print("Latitude: " {observer_lati})
        print("Longitude :" {observer_long})

        print(f"You are tracking the {sat_name} from {location_in}.")

        break
    else:
        print("Location not found. Try a more specific name.")