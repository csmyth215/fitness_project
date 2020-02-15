import xml.etree.ElementTree as ET
import gmplot
from gmplot import GoogleMapPlotter
import os

# set key with environment variables (dotenv)


ns = {'default_ns': "http://www.topografix.com/GPX/1/1", 'xsi': "http://www.w3.org/2001/XMLSchema-instance", 
'ns2': "http://www.garmin.com/xmlschemas/GpxExtensions/v3", 'ns3': "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"}

files = os.listdir("./gpx/")

track_points = []
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
        print(f"Encountered an error: {ex}")
        continue
        

coordinates = []
for point in track_points:
    this_lat = float(point['lat'])
    this_lon = float(point['lon'])
    this_tuple = (this_lat, this_lon)
    coordinates.append(this_tuple)

