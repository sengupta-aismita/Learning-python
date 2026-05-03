#scopes and name resolution
# local-inside a function
# enclosing from outer function if nested
# global - top level script
# built in

def serve_chai():
    chai_type = "masala" #local
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" #enclosing scope
    def print_order():
        chai_order = "ginger"
        print("Inner: ", chai_order)
    print_order()    
    print("Outside : ", chai_order)    

chai_order = "Tulsi" #global
chai_counter()
print("Global : ", chai_order)

