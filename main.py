# main.py

# Setup
from observer import get_observer_location

print("★ Satellite Tracker ★")
print ()
sat_name = "ISS"
observer_name, observer_lati, observer_long = get_observer_location()
print(f"You are tracking the {sat_name} from {observer_name}.")