import sys
from io import BytesIO

import requests

from PIL import Image
from utils import get_size, get_pos, get_response, get_org_pos, PointToPointCenter, VectorLenght

if __name__ == '__main__':
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    search_api_server = "https://search-maps.yandex.ru/v1/"
    toponym_to_find = " ".join(sys.argv[1:])

    json_response = get_response(geocoder_api_server, {"geocode": toponym_to_find,
                                                       "format": "json",
                                                       "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"})
    json_response2 = get_response(search_api_server,
                                  {"text": "Аптека", "lang": "ru_RU",
                                   "type": "biz", "ll": ",".join(get_pos(json_response)),
                                   "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"})

    pos2 = get_org_pos(json_response2)
    pos1 = get_pos(json_response)
    size = get_size(json_response)
    print(json_response2["features"][0]["properties"]["CompanyMetaData"]["address"])
    print(json_response2["features"][0]["properties"]["CompanyMetaData"]["name"])
    print(json_response2["features"][0]["properties"]["CompanyMetaData"]["Hours"]["text"])
    print(VectorLenght(pos1, pos2) * 40000 / 360 * 1000, "м")

    map_params = {
        "ll": ",".join(PointToPointCenter(pos1, pos2)),
        "spn": ",".join(size),
        "l": "map",
        "pt": f"{','.join(pos2)},flag~{','.join(pos1)},flag"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(response.content)).show()
