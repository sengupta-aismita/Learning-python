def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
print(strong_chai)