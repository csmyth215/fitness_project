import xml.etree.ElementTree as ET
import os
import folium
from folium.plugins import HeatMap

files = os.listdir("./gpx/")
ns = {'default_ns': "http://www.topografix.com/GPX/1/1", 'xsi': "http://www.w3.org/2001/XMLSchema-instance", 
'ns2': "http://www.garmin.com/xmlschemas/GpxExtensions/v3", 'ns3': "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"}

def generateBaseMap(default_location=[51.45, -0.01], default_zoom_start=6):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start, )
    return base_map

track_points = []
count = 1
for filename in files:
    try:
        tree = ET.parse(f'./gpx/{filename}')
        root = tree.getroot()
        our_track = root.find('default_ns:trk', ns)
        if our_track is None:
            raise Exception("Could not retrieve requested track")
        else:
            for track_seg in our_track.findall('default_ns:trkseg', ns):
                for trkpt in track_seg.findall('default_ns:trkpt', ns):
                    track_points.append(trkpt.attrib)

    except ET.ParseError as ex:
        count += 1
        continue

if count == 1:
    print("Encountered one error: unable to process one file")        
else:
    print(f"Encountered {count} errors: unable to process {count} files")


coordinates = []
for point in track_points:
    this_lat = float(point['lat'])
    this_lon = float(point['lon'])
    this_tuple = (this_lat, this_lon)
    coordinates.append(this_tuple)

this_map = generateBaseMap()
folium.TileLayer('Stamen Toner').add_to(this_map)
folium.TileLayer('Stamen Watercolor').add_to(this_map)
folium.TileLayer('CartoDB dark_matter').add_to(this_map)
HeatMap(data=(coordinates), name='heatmap', radius=8, max_zoom=8).add_to(this_map)
folium.LayerControl(position='topright', collapsed=False).add_to(this_map)
this_map.save('folium.html')