import xml.etree.ElementTree as ET
import os
import csv
from datetime import date, datetime

# still to do: set key with environment variables (dotenv)

ns = {'default_ns': "http://www.topografix.com/GPX/1/1", 'xsi': "http://www.w3.org/2001/XMLSchema-instance", 
'ns2': "http://www.garmin.com/xmlschemas/GpxExtensions/v3", 'ns3': "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"}

files = os.listdir("./gpx/")

activity_start_timestamps = []
for filename in files:
    try:
        tree = ET.parse(f'./gpx/{filename}')
        root = tree.getroot()
        our_metadata = root.find('default_ns:metadata', ns)
        if our_metadata is None:
            raise Exception("Could not retrieve requested metadata")
        else:
            start_time = our_metadata.find('default_ns:time', ns)
            activity_start_timestamps.append(start_time.text)

    except ET.ParseError as ex:
        continue
        
timestamps = []
for start_timestamp in activity_start_timestamps:
    time_as_datetime_obj = datetime.strptime(start_timestamp, "%Y-%m-%dT%H:%M:%S.000Z")
    timestamps.append(time_as_datetime_obj)

activity_count = {}
for timestamp in timestamps:
    activity_year = datetime.strftime(timestamp, "%Y")
    activity_month = datetime.strftime(timestamp, "%m")
    if activity_year not in activity_count.keys():
        activity_count[activity_year] = {}

    if activity_month in activity_count[activity_year].keys():
        activity_count[activity_year][activity_month] += 1
    else:
        activity_count[activity_year][activity_month] = 1

with open('activity_counts.csv', 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file)
    for activity_year in activity_count:
        for activity_month in activity_count[activity_year]:
            csvwriter.writerow([activity_year, activity_month, activity_count[activity_year][activity_month]])


