import requests
import math


def get_size(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    xstart, ystart = map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split())
    xstop, ystop = map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())
    longitude_size, lattitude_size = [xstart - xstop, ystart - ystop]
    return str(longitude_size), str(lattitude_size)


def get_pos(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return toponym_longitude, toponym_lattitude


def get_org_pos(json_response):
    coords = json_response["features"][0]["geometry"]["coordinates"]
    return str(coords[0]), str(coords[1])


def get_response(api_server, params):
    response = requests.get(api_server, params=params)
    if not response:
        print(response.content)
        exit(-1)
        pass
    json_response = response.json()
    return json_response


def PointToPointCenter(a, b):
    return str((float(a[0]) + float(b[0])) / 2), str((float(a[1]) + float(b[1])) / 2)


def VectorLenght(a, b):
    return math.sqrt((float(a[0]) - float(b[0])) ** 2 + (float(a[1]) - float(b[1])) ** 2)
