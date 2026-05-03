def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("AFter kitchen update", chai_type) 


update_order()      




#     | Case               | Result                        |
# | ------------------ | ----------------------------- |
# | With `nonlocal`    | Outer variable is modified    |
# | Without `nonlocal` | New inner variable is created |

chai_type = "Elaichi"   # global variable

def update_order():
    def kitchen():
        global chai_type
        chai_type = "Kesar"   # modifies global variable
    
    kitchen()
    print("After kitchen update", chai_type)

update_order()