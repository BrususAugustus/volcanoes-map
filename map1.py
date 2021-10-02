import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

## Data Read

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

cords = []


def elevation_color(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev <= 3000:
        return "orange"
    else:
        return "red"


print(cords)

fgv = folium.FeatureGroup(name="Volcanoes")

map = folium.Map(location=[41.097535, -116.085615], zoom_start=5)

# Add markers
for lat, lon, elev in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=f"{str(elev)} m", fill_color=elevation_color(
        elev), radius=6, color="grey", fill_opacity=0.7))

# Add GeoJson layer
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
             style_function=lambda x: {'fillColor': 'green' if x["properties"]["POP2005"] < 15000000 
             else "orange" if 15000000 <= x["properties"]["POP2005"] < 30000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)

# Add control layer 
map.add_child(folium.LayerControl())

map.save("Map1.html")
