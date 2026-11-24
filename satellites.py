# satellites.py
# Downloads, caches, and reads CSV data

# Setup
import pandas as pd
from pathlib import Path

# Read in the satellites
def load_sats():
    file_path = Path("/home/lucia/SatTracker/data/stations.csv")

    table = pd.read_csv(file_path)
    satellites = table.to_dict(orient="records")

    return satellites

# Display the satellites in a list
def display_satellites():
    satellites = load_sats()

    print(f"Loaded {len(satellites)} satellite records.")

    for number, satellite in enumerate(satellites, start=1):
        print(f"{number}. {satellite['OBJECT_NAME']}")
    
    print()
    return

# Gets input satellites, checks if valid
def get_satellites():
    satellites = load_sats()
    display_satellites()

    while True:
            sat_in = input("☆ Enter your desired satellite: ")
            print()
            search = sat_in.strip().casefold()
            selected_sat = None

            # If user inputs number
            if sat_in.strip().isdigit():
                 sat_in = int(sat_in)
                 for number, sat in enumerate(satellites, start=1):
                      if number == sat_in:
                        selected_sat = sat
                        break

            # Search the catalogue
            for sat in satellites:
                 name = sat["OBJECT_NAME"].casefold()
                 catalog_number = str(sat["NORAD_CAT_ID"])

                 if search == name or search == catalog_number:
                      selected_sat = sat
                      break
            
            # Check if it is the desired satellite
            if selected_sat is not None:
                 print(f"Matched satellite:{selected_sat['OBJECT_NAME']}")

                 confirmation = input("Is this the correct satellite? (yes/no): ")
                 confirmation = confirmation.strip().lower()

                 # If confirmed, print the corresponding latitude/longitude
                 if confirmation in ("yes", "y", "ye"):
                      return selected_sat, selected_sat['OBJECT_NAME'], sat["NORAD_CAT_ID"]
                 else:
                      print("Satellite not accepted. Please try again.")
            else:
                print("Satellite not found. Try its full name or catalog number.")