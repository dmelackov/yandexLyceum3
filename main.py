import sys
from io import BytesIO

import requests

from PIL import Image
from utils import get_size, get_pos

if __name__ == '__main__':

    toponym_to_find = " ".join(sys.argv[1:])

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        exit(-1)
        pass

    json_response = response.json()

    pos = get_pos(json_response)
    map_params = {
        "ll": ",".join(pos),
        "spn": ",".join(get_size(json_response)),
        "l": "map",
        "pt": f"{pos[0]},{pos[1]},flag"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(response.content)).show()
