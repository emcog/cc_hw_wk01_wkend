# WRITE YOUR FUNCTIONS HERE

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