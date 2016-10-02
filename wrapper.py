import requests
from nasa_asteroids import Asteroid

class Nasa:
    def __init__(self):
        self.asteroid_dump = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=oyRkinCOV4EADrJok2o8LHQQ6ts2HoLdUWoPqTRU"

    def asteroids(self):
        return requests.get(self.asteroid_dump).json()


if __name__=="__main__":
    c = Nasa()
    dump = c.asteroids()
    print
