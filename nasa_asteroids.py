
class Asteroid:
    #Important stuff
    name = None
    neo_id = None
    url = None
    pot_hazard = None
    estimated_diameter = None
    magnitude = None
    close_app_data = None   #dictionary inside
    orbital_data = None     #dictionary inside
    #est_diameter_min = None#temporarily unused
    #est_diameter_max = None#temporarily unused


    def get_estimated_diameter(self): #Getter to avoid changing names throughout code
        return self.estimated_diameter

    def __init__(self):
        pass

    def debug_display(self):
        print("Name: " + self.name)
        print("Id: " + self.neo_id)
        print("URL: " + self.nasa_jpl_url)
