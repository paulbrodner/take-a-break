__version__ = "0.0.1"

import os

import requests
from PIL import Image


def get_resources(filename):
    dirname = os.path.join(os.path.dirname(__file__), 'resources')
    fullname = os.path.join(dirname, filename)
    return fullname


def get_random_joke():
    response = requests.get("http://api.icndb.com/jokes/random")
    if response.status_code == requests.codes.ok:
        joke = response.json()["value"]["joke"]
        print(joke)
        joke = joke.replace("&quot;", "\"")
        return joke
    else:
        return "Take a brake! You need it!"


def jpeg_to_png(image):
    png_image = "{}.png".format(os.path.splitext(image)[0])
    Image.open(image).save(png_image)
    os.remove(image)
    return png_image
