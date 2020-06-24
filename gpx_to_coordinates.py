import xml.etree.ElementTree as ET
import os
import csv
from datetime import datetime

# set key with environment variables (dotenv)

ns = {'default_ns': "http://www.topografix.com/GPX/1/1", 'xsi': "http://www.w3.org/2001/XMLSchema-instance", 
'ns2': "http://www.garmin.com/xmlschemas/GpxExtensions/v3", 'ns3': "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"}

files = os.listdir("./gpx/")

positions = {}
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
                    time = trkpt.find('default_ns:time', ns)
                    time_text = time.text
                    time_dt_obj = datetime.strptime(time_text, "%Y-%m-%dT%H:%M:%S.000Z")
                    time_formatted = datetime.strftime(time_dt_obj, "%d/%m/%Y, %H:%M:%S")
                    coordinates = trkpt.attrib
                    latitude = float(coordinates['lat'])
                    longitude = float(coordinates['lon'])
                    positions[time_formatted] = latitude, longitude           
                    
    except ET.ParseError as ex:
        print(f"Encountered an error: {ex}")
        continue


with open('coordinates.csv', 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file)
    for item in positions.items():
        csvwriter.writerow([item[0], item[1][0], item[1][1]])