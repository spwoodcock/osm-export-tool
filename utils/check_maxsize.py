import aoi_utils

from django.contrib.gis.geos import GEOSGeometry
#from aoi_utils import simplify_geom
str = '{"type": "Polygon", "coordinates": [[[82.229365234375, 30.461887976785263], [81.35045898437501, 30.594375551592606], [81.10875976562501, 30.32921997305067], [80.55944335937502, 30.253328855657386], [80.07604492187501, 29.548566040804488], [79.94420898437501, 28.68475983186609], [80.51549804687502, 28.395220964394326], [81.10875976562501, 28.279183045180275], [81.26256835937501, 28.007936291358547], [81.89977539062501, 27.736004806409156], [82.60290039062501, 27.48288774067173], [83.30602539062501, 27.190105364650535], [84.140986328125, 27.30731110259252], [84.47057617187501, 27.17055907805282], [84.51452148437501, 26.935737107335612], [85.371455078125, 26.56293465319699], [86.93151367187501, 26.228342889338705], [88.183955078125, 26.228342889338705], [88.44762695312502, 26.955324361687246], [88.20592773437501, 27.190105364650535], [88.381708984375, 28.10488896326109], [87.78844726562501, 28.240475596497035], [87.085322265625, 28.182388083226925], [85.964716796875, 28.37589011477759], [85.32750976562501, 28.72330480766867], [84.27282226562501, 29.414673615330855], [83.34997070312501, 29.758610340225857], [82.229365234375, 30.461887976785263]]]}'
#aoi_geom = simplify_geom(aoi_geom)
aoi_geom = GEOSGeometry(str)
print aoi_utils.check_extent(aoi_geom,"http://export.hotosm.org:6080/api/")