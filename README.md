# Distance Calculation for Plant Locations

## Problem Statement

The objective of this project was to calculate the minimum driving distance between various plant locations and two reference points — Andheri and Churchgate (both located in Mumbai, India). The plant locations were provided by name, but their exact coordinates were not available. We needed to use the Google Maps Geocoding API to resolve these locations to coordinates and then calculate the driving distance using the Google Maps Distance Matrix API.

## Approach

1. **Geocoding Plant Locations**: 
   - The plant locations (e.g., Dolvi, Salav, Vasind, etc.) were geocoded using the Google Maps Geocoding API to convert the location names into coordinates (latitude and longitude).
   
2. **Distance Calculation**:
   - Using the **Google Maps Distance Matrix API**, the driving distance from each plant to the two reference points (Andheri and Churchgate) was calculated.
   - The distance between each plant and the two reference points was computed in kilometers, and the minimum distance was selected for each plant.

3. **Handling Edge Cases**:
   - In cases where the geocoding failed (e.g., no valid result was returned), the plant was flagged as "Not Found".
   - The distance calculation also handled exceptions where the Google Maps API failed to respond.

4. **Output**:
   - The final output was a structured table (or Excel sheet) listing the plant name and the closest distance (in kilometers) to either Andheri or Churchgate.

## Requirements

- Python 3.x
- Google Maps API Key
- Libraries:
  - `googlemaps`
  - `pandas`

## How to Run

1. Install required Python libraries:
   ```bash
   pip install googlemaps pandas

2. Replace YOUR_GOOGLE_MAPS_API_KEY with your actual Google Maps API key in the code:
   ```python
   API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your API Key

3. Run the script:
   ```bash
   python distance_calculator.py
  
4. The results will be printed to the console, and a structured output will be available in the DataFrame.
