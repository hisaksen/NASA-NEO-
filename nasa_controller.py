from nasa_view import View
from nasa_model import Model

def run():
    exit = False
    while not exit:
        menu = view.menu()
        if menu == '0':
            exit = True
            view.exiting()
        elif menu == '1':   #see all potentially hazardous NEOs
            view.bar()
            list_bad_asteroids()
            view.bar()
        elif menu == '2':   #View detail of largest asteroid"
            show_large()
        elif menu == '3':   #View detail of smallest asteroid"
            show_small()
        elif menu == '4':   #View every NEO by name"
            view.bar()
            list_asteroids()
            view.bar()
            asteroid_detail()

def list_asteroids():
    for i in range(0, len(model.asteroid_list), 1):
        view.body(str(i+1),model.asteroid_list[i].name, model.asteroid_list[i].neo_id, model.asteroid_list[i].url)

def asteroid_detail():
    ast_num = int(view.show_list_of_every_neo()) - 1
    asteroid_selected = model.asteroid_list[ast_num]
    view.asteroid_detail(asteroid_selected)

def list_bad_asteroids():
    for i in range(0, len(model.asteroid_list), 1):
        if model.asteroid_list[i].pot_hazard:
            view.body(str(i+1),model.asteroid_list[i].name, model.asteroid_list[i].neo_id, model.asteroid_list[i].url)

def show_large():
    largest_asteroid = model.large_stroid()
    view.show_details_largest_neo(largest_asteroid)

def show_small():
    smallest_asteroid = model.small_stroid()
    view.show_details_smallest_neo(smallest_asteroid)



if __name__=="__main__":
    view = View()
    model = Model()
    run()
