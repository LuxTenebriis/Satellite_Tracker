# orbit.py

# Setup
from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import wgs84

def create_sat(sat_record):
    timescale = load.timescale(builtin=True)

    sat = EarthSatellite.from_omm(timescale, sat_record)

    return sat

def get_sat_position(satellite):
    timescale = load.timescale(builtin=True)
    now = timescale.now()

    position = satellite.at(now)
    coordinates = wgs84.geographic_position_of(position)

    return coordinates.latitude.degrees, coordinates.longitude.degrees, coordinates.elevation.km

def sat_stats(sat_model):
    sat_lati, sat_long, sat_altitude = get_sat_position(sat_model)
    
    print(f"\nSatellite latitude: {sat_lati:.2f} degrees")
    print(f"Satellite longitude: {sat_long:.2f} degrees")
    print(f"Satellite altitude: {sat_altitude:.2f} km\n")
    return

def get_observer_stats(sat_model, observer_lati, observer_long):
    observer = wgs84.latlon(
        latitude_degrees=observer_lati,
        longitude_degrees=observer_long,
    )

    timescale = load.timescale(builtin=True)
    now = timescale.now()

    relative_position = (sat_model - observer).at(now)
    elevation, azimuth, distance = relative_position.altaz()

    return elevation.degrees, azimuth.degrees, distance.km

def observer_sat_sats(sat_model, observer_lati, observer_long):
    elevation, azimuth, distance = get_observer_stats(
        sat_model,
        observer_lati,
        observer_long,
    )

    print(f"Elevation above your horizon: {elevation:.2f} degrees")
    print(f"Direction (azimuth): {azimuth:.2f} degrees")
    print(f"Distance from you: {distance:.2f} km\n")

    if elevation > 0:
        print("The satellite is above your horizon.")
    else:
        print("The satellite is at or below your horizon.")

    directions = [
        "North",
        "Northeast",
        "East",
        "Southeast",
        "South",
        "Southwest",
        "West",
        "Northwest",
    ]

    index = int((azimuth + 22.5) // 45) % 8
    print(f"Direction: {directions[index]} ({azimuth:.2f} degrees)")

    return

def get_orbit_age(sat_model):
    timescale = load.timescale(builtin=True)
    now = timescale.now()

    return float(now - sat_model.epoch)