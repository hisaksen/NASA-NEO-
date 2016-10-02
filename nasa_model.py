from wrapper import Nasa
from nasa_asteroids import Asteroid

#Global dump from NASA API
nasa = Nasa()
dump = nasa.asteroids()
neos = dump['near_earth_objects']

def parse_json_into_neo_list(dump):
    asteroidlist = []
    for elem in dump:
        temp_asteroid = Asteroid()
        temp_asteroid.name = elem["name"]
        temp_asteroid.neo_id = elem["neo_reference_id"]
        temp_asteroid.avg_dia = (elem["estimated_diameter"]["kilometers"]["estimated_diameter_min"]+elem["estimated_diameter"]["kilometers"]["estimated_diameter_min"])/2
        temp_asteroid.url= elem["nasa_jpl_url"]
        temp_asteroid.pot_hazard= elem["is_potentially_hazardous_asteroid"]
        temp_asteroid.magnitude= elem["absolute_magnitude_h"]
        temp_asteroid.close_app_data = elem["close_approach_data"]
        temp_asteroid.orbital_data = elem["orbital_data"]
        asteroidlist.append(temp_asteroid)
    return asteroidlist

class Model:
    asteroid_list = None

    def __init__(self):
        self.asteroid_list = parse_json_into_neo_list(neos)

    def large_stroid(self):
        largest_stroid = 0
        asteroid_obj = None
        for asteroids in self.asteroid_list:
            if int(asteroids.avg_dia) > int(largest_stroid):
                largest_stroid = asteroids.avg_dia
                asteroid_obj = asteroids
        return asteroid_obj

    def small_stroid(self):
        smallest_stroid = self.asteroid_list[0].avg_dia if len(self.asteroid_list)>0 else 0 #ternary conditional operator
        asteroid_obj = None
        for asteroids in self.asteroid_list:
            if float(asteroids.avg_dia) < float(smallest_stroid):
                smallest_stroid = asteroids.avg_dia
                asteroid_obj = asteroids
        return asteroid_obj

if __name__=="__main__":
    test = Model()
    test.large_stroid()
    test.small_stroid()
