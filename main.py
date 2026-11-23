# main.py

# Setup
import sys

from observer import get_observer_location

def main():
    print("★ Satellite Tracker ★")
    print ()
    print("Find a satellite and explore its position relative to you.")
    print("Enter an Earth location when prompted.")
    print("Press Ctrl+C in the terminal to stop.\n")

    sat_name = "ISS"
    observer_name, observer_lati, observer_long = get_observer_location()
    print(f"You are tracking the {sat_name} from {observer_name}.")

    return 0

if __name__ == "__main__":
    sys.exit(main())