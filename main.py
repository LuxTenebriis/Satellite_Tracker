# main.py

# Setup
import sys
from observer import get_observer_location
from satellites import get_satellites

def main():
    print("★ Satellite Tracker ★")
    print("Find a satellite and explore its position relative to you.")
    print("Enter an Earth location when prompted.")
    print("Press Ctrl+C in the terminal to stop.\n")

    sat, sat_obj_name, sat_norad_cat_id = get_satellites()
    observer_location, observer_lati, observer_long = get_observer_location()
    print(f"\nYou are now tracking {sat_obj_name} from {observer_location}")

    return 

if __name__ == "__main__":
    sys.exit(main())