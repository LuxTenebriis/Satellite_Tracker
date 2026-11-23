# observer.py

# Setup
import time
from geopy.geocoders import Nominatim

# Gets input location, checks if valid
def get_observer_location():
    geolocator = Nominatim(user_agent="lux_sat_tracker_learning")

    while True:
        location_in = input("☆ Enter your desired location: ")
        print()
        location = geolocator.geocode(location_in, timeout=10)

        # Check if it is the desired location
        if location is not None:
            print(f"Matched location: {location.address}")
            confirmation = input("Is this the correct place? (yes/no): ")
            confirmation = confirmation.strip().lower()

            # If confirmed, print the corresponding latitude/longitude
            if confirmation in ("yes", "y"):
                observer_lati = location.latitude
                observer_long = location.longitude

                print("Analysing location...")
                time.sleep(3)
                print()
                print(f"Latitude: {observer_lati}")
                print(f"Longitude : {observer_long}")
                print()

                return location.address, observer_lati, observer_long
            else:
                print("Location not accepted. Please enter a location again.")
        else:
            print("Location not found. Try a more specific name.")