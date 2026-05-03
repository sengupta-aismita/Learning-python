class OutofBounds(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutofBounds("Missing milk or sugar")
    print("Ready")


make_chai(0,5)    