import googlemaps
import pandas as pd

# Initialize Google Maps API
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your API Key
gmaps = googlemaps.Client(key=API_KEY)

# Plant locations
plant_locations = ["Dolvi", "Salav", "Vasind", "Tarapur"]  # Example

# Fixed destination locations
destinations = ["Andheri, Mumbai, India", "Churchgate, Mumbai, India"]

# Create a DataFrame to store results
results = []

for plant in plant_locations:
    try:
        # Geocode plant location to get full address
        geocode_result = gmaps.geocode(plant + ", India")
        
        if not geocode_result:
            print(f"No location found for {plant}")
            continue
        
        # Take the first geocoded location (best match)
        plant_address = geocode_result[0]['formatted_address']
        plant_location = geocode_result[0]['geometry']['location']
        
        # Get distance from plant to Andheri and Churchgate
        distance_result = gmaps.distance_matrix(origins=plant_address,
                                                 destinations=destinations,
                                                 mode='driving')
        
        # Extract distances
        distances = []
        for element in distance_result['rows'][0]['elements']:
            if element['status'] == 'OK':
                distances.append(element['distance']['value'])  # in meters
        
        if distances:
            min_distance_meters = min(distances)
            min_distance_km = min_distance_meters / 1000  # convert to KM
        else:
            min_distance_km = None
        
        results.append({
            "Plant": plant,
            "Closest Distance (km)": min_distance_km
        })
        
    except Exception as e:
        print(f"Error processing {plant}: {e}")

# Convert to DataFrame
df = pd.DataFrame(results)
print(df)
