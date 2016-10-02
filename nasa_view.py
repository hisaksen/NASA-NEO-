class View:

    def menu(self):
        valid_choices = ['1','2','3','4','0']
        selection = None
        while not selection in valid_choices:
            print("1. See all potentially hazardous Near Earth Objects")
            print("2. View detail of largest asteroid")
            print("3. View detail of smallest asteroid")
            print("4. View every NEO by name")
            print("0. Exit")
            selection = input('Select: ')
            return selection

    def show_list_of_every_neo(self):
        print("Here are all the Near Earth Objects")
        inp = input("Input the # of the asteroid to view it's details. ")
        return inp

    def show_details_largest_neo(self, asteroid):
        print("Here is the largest Near Earth Object")
        print("Name of asteroid: {0} Diameter in KM: {1}".format(asteroid.name, asteroid.avg_dia))

    def show_details_smallest_neo(self,asteroid):
        print("Here is the smallest Near Earth Object")
        print("Name of asteroid: {0} Diameter in KM: {1}".format(asteroid.name,asteroid.avg_dia))

    def asteroid_detail(self,asteroid):
        print("Here is " + str(asteroid.name) + " and it's details.")
        print("API ID: " + str(asteroid.neo_id))
        print("Link: " + str(asteroid.url))
        print("Potential Hazard: " + str(asteroid.pot_hazard))
        print("Estimated Diameter: " + str(asteroid.estimated_diameter))
        print("Magnitude(measure of intrinsic brightness of a celestial object) :" + str(asteroid.magnitude))
        print("_____________________________________________________________")
        print("Close approach information: " + str(asteroid.close_app_data))
        print("Orbital Data: " + str(asteroid.orbital_data))
        print("_____________________________________________________________")

    def exiting(self):
        print("Exiting...")
        return

    def bar(self):
        print("+--#--+--------Name--------+------ID-----+----------------URL------------+")

    def body(self, p1, p2, p3, p4):
        #print(p1,p2,p3,p4)
        print("|{:^5}| {:19}|{:^13}|{:^50}".format(p1,p2,p3,p4))

if __name__=="__main__":
    pass
