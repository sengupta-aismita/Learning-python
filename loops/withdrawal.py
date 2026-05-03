flavours = ["ginger", "Out of stock", "lemon", "discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "discontinued":
        break
    print("discontinued item found")