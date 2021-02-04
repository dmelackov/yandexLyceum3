def get_size(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    xstart, ystart = map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split())
    xstop, ystop = map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())
    longitude_size, lattitude_size = [xstart - xstop, ystart - ystop]
    return str(longitude_size), str(lattitude_size)
