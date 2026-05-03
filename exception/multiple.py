def process_order(item,quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is : {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")
    else:
        print("Cannot print")    

process_order("ginger", 2)
process_order("masala", "two")