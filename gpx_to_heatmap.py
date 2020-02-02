import xml.etree.ElementTree as ET
import gmplot

ns = {'default_ns': "http://www.topografix.com/GPX/1/1", 'xsi': "http://www.w3.org/2001/XMLSchema-instance", 
'ns2': "http://www.garmin.com/xmlschemas/GpxExtensions/v3", 'ns3': "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"}

tree = ET.parse('xxx.gpx')
root = tree.getroot()
root_tag = root.tag
root_attribute = root.attrib

our_track = root.find('default_ns:trk', ns)
if our_track is None:
    raise Exception("Could not retrieve requested track")
else:
    track_points = []
    for track_seg in our_track.findall('default_ns:trkseg', ns):
        for trkpt in track_seg.findall('default_ns:trkpt', ns):
            track_points.append(trkpt.attrib)

lats = []
lons = []
for point in track_points:
    this_lat = float(point['lat'])
    this_lon = float(point['lon'])
    lats.append(this_lat)
    lons.append(this_lon)

gmap = gmplot.gmplot.GoogleMapPlotter(54.5, -5.5, 6)
gmap.heatmap(lats, lons)
gmap.apikey = ""
gmap.draw("map_1.html")

        


