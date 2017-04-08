from django.contrib.gis.geos import Polygon
from osm_xml import OSM_XML
from osm_pbf import OSM_PBF
from kml import KML
from geopackage import Geopackage
from shp import Shapefile
from feature_selection.feature_selection import FeatureSelection
import logging
import os
logging.basicConfig(level=logging.DEBUG)

try:
    os.makedirs('scratch', 6600)
except:
    print "Exists"

y = '''
waterways:
    types: 
        - lines
        - polygons
    select:
        - name
        - waterway
buildings:
    types:
        - lines
        - polygons
    select:
        - name
        - building
    where: building IS NOT NULL
'''
feature_selection = FeatureSelection(y)
aoi_geom = Polygon.from_bbox((-10.80029,6.3254236,-10.79809,6.32752))
osm_xml = OSM_XML(aoi_geom, 'scratch/osm_xml.osm')
osm_xml.run()
osm_pbf = OSM_PBF('scratch/osm_xml.osm','scratch/osm_pbf.pbf')
osm_pbf.run()
geopackage = Geopackage('scratch/osm_pbf.pbf','scratch/geopackage.gpkg','scratch/osmconf.ini',feature_selection)
geopackage.run()
kml = KML('scratch/geopackage.gpkg','scratch/kml.kmz')
kml.run()
shp = Shapefile('scratch/geopackage.gpkg','scratch/shapefile.shp.zip')
shp.run()
