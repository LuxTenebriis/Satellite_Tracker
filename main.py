# main.py

# Setup
import time
from geopy.geocoders import Nominatim

# Title
print("★ Satellite Tracker ★", "\n\n")

#SATELITES
sat_name = "ISS"
print("☆ You are now tracking: ", sat_name)

# Input user location w geolocator
geolocator = Nominatim(user_agent="lux_sat_tracker_learning")

while True:
    location_in = input("☆ Enter your desired location: ")
    print()
    location = geolocator.geocode(location_in, timeout = 10)

    # check if it is the desired location
    if location is not None:
        print(f"Matched location: {location.address}")
        confirmation = input("Is this the correct place? (yes/no): ")
        confirmation = confirmation.strip().lower()

        # if location valid, print location and corresponding lat/long
        if confirmation in ("yes", "y"):
            observer_lati = location.latitude
            observer_long = location.longitude

            print("Analysing location...")
            time.sleep(3)
            print()
            print(f"Latitude: {observer_lati}")
            print(f"Longitude : {observer_long}")
            print
            print(f"You are tracking the {sat_name} from {location}.")
            break
        else:
            print("Location not accepted. Please enter a location again.")
    else:
        print("Location not found. Try a more specific name.")