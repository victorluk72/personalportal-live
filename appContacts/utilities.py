import googlemaps

# ----Get coordinates from address---------------
def add_coordinates(cont_address):
    # Set Google maps Key
    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_KEY"))

    #ta = '1594 Lancaster dr, Oakville, ON, L6H 2Z6'
    # Geocoding an address
    geocode_result = gmaps.geocode(cont_address)
    try:
        latitude = geocode_result[0]["geometry"]["location"]["lat"]
        longitude = geocode_result[0]["geometry"]["location"]["lng"]

    except:
        latitude = 51.4977578
        longitude = -0.1435168

    # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.reverse_geocode((43.4830017, -79.6915834))
    #print(latitude, longitude)
    return latitude, longitude
