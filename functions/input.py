chai = " Ginger chai"

def prepare_order(order):
    print("Prerparing ", order)

prepare_order(chai)    

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "Yes", "Low") 
make_chai(tea="Green", sugar = "Low", milk = "No") #keywords

def special_chai(*ingredients, **extras):
    print("Ingredients ", ingredients)
    print("Extras ", extras)

special_chai("Cinnamon", "Cardamom", sweetener = "Honey", foam = "yes") 

def chai_order(order = []):
    order.append("Masala")
    print(order)

