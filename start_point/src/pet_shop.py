# WRITE YOUR FUNCTIONS HERE
import pdb


def get_pet_shop_name(setUp):
    name = setUp['name']
    return name
    print(name) #sanity check

def get_total_cash(setUp):
    # ignore previous psudo
    # get total cash from setup.cc_pet_shop, (remember to check where the test is pointing to in the dataset)
    total_cash = setUp['admin']['total_cash']
    return total_cash

def add_or_remove_cash(setUp, amount_in_or_out):
    setUp['admin']['total_cash'] += amount_in_or_out


def get_pets_sold(setUp):
    return setUp['admin']['pets_sold']

def increase_pets_sold(setUp, pet_sales):
    setUp['admin']['pets_sold'] += pet_sales

def get_stock_count(setUp):
    # find length of 
    return len(setUp['pets'])

def get_pets_by_breed(setUp, breed_search):
    pets = []
    i = 0
    stock_pets = setUp['pets']

    for pet in stock_pets:
        if stock_pets[i]['breed'] == breed_search:
            pets.append(pet)
        i += 1
    
    return pets


def find_pet_by_name(setUp, name_search):
    i = 0
    stock_pets = setUp['pets']

    for pet in stock_pets:
        if stock_pets[i]['name'] == name_search:
            print('pet', pet)
            return pet
        i += 1