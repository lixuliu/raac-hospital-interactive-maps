"""
Aim: To visualize hospital locations on an interactive map using geographic coordinates.

Objective: This script loads hospital coordinates from an Excel file, creates an interactive map centered at the first hospital's location, and adds markers for each hospital. The map is then saved as an HTML file for easy viewing.
"""

import folium
import pandas as pd

# Load the coordinates from the Excel file
df = pd.read_excel('data/coordinates.xlsx')

# Iterate through the DataFrame and print coordinates
for index, row in df.iterrows():
    print(f'Site: {row["Site"]}, Latitude: {row["Latitude"]}, Longitude: {row["Longitude"]}')

# Create a map centered at the first coordinates
m = folium.Map(location=[df.iloc[0]['Latitude'], df.iloc[0]['Longitude']], zoom_start=10)

# Add CircleMarkers for each coordinate
for index, row in df.iterrows():
    popup_text = f"Name: {row['Site']}<br>Address: {row['address']}"
    folium.CircleMarker(location=[row['Latitude'], row['Longitude']], radius=5, fill=True, color='red', popup=popup_text).add_to(m)
# Add markers for each coordinate
#for index, row in df.iterrows():
#   folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Site']).add_to(m)

# Save the map
m.save('index.html')
