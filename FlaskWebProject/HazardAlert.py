import requests
import json
from math import radians, cos, sin, asin, sqrt
URL = "http://eonet.sci.gsfc.nasa.gov/api/v2.1/"
def findHazard(lon, lat):
    params = {
    'status':'open',
    'limit':20
    }
    r = requests.get(URL+'events')
    hazardList = []
    dicEvents = r.json();
    for each in dicEvents['events']:
        # print(each)
        for coords in each['geometries']:
            if (coords['type'] == 'Point'):
                #print(coords)
                # print coords['coordinates'][0]
                # print coords['coordinates'][1]
                distances = haversine(coords['coordinates'][0],coords['coordinates'][1]\
                                    ,lon,lat )

                if (distances < 50):
                    hazardList.append(each)
    return hazardList


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km
