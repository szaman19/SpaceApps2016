import requests
import json
URL = "http://eonet.sci.gsfc.nasa.gov/api/v2.1/"
def main():
    params = {
    'status':'open',
    'limit':20
    }
    r = requests.get(URL+'events')

    dicEvents = r.json();
    print dicEvents['events']
main()
