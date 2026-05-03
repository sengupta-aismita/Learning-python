#IndexError
#KeyError
#ZeroDivisionError
#TypeError
#NameError

chai_menu = {"masala": 30 , "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("Key doesnt exist")    

def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("We dont know the error")
    except ValueError as e:
        print("Error : ", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please")                

serve_chai("masala")
serve_chai("unknown")