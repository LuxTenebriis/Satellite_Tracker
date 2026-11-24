# main.py

import sys

from observer import get_observer_location
from satellites import get_satellites
from orbit import create_sat, sat_stats, observer_sat_sats

def main():
    print("★ Satellite Tracker ★")
    print("Find a satellite and explore its position relative to you.")
    print("Enter an Earth location when prompted.")

    sat, sat_obj_name, sat_norad_cat_id = get_satellites()

    observer_location, observer_lati, observer_long = (
        get_observer_location()
    )

    city = observer_location.split(",")[0].strip()
    print(f"\nYou are now tracking {sat_obj_name} from {city}\n")

    # Create the orbital model
    sat_model = create_sat(sat)

    # Print terminal statistics
    sat_stats(sat_model)
    observer_sat_sats(sat_model, observer_lati, observer_long)

    return 0


if __name__ == "__main__":
    sys.exit(main())