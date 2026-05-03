order = dict(type="chai", size="large", count =2)
print(f"Order: {order}")

chai = {}
chai["base"] = "black tea"
chai["liquid"]= "milk"

print(f"Recipe base : {chai['base']}")
print(f"Recipe: {chai}")
del chai["liquid"]
print(f"Recipe: {chai}")

# keys, values, items---both key value pair

last_item = chai.popitem()
print(f"Removed item : {last_item}")

#.update() .get("note", "Alternative msg: No note")

# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# Step 2: Add email and phone
customer.update({"email": "john@gmail.com", "phone":"123456789"})

# Step 3: Print customer's name and city
print([customer["name"], customer["city"]])

# Step 4: Check if "email" exists
print("email" in customer)
# Step 5: Delete the "age" field
del customer["age"]

# Step 6: Print all keys, values, and items
print(customer.keys())
print(customer.values())
print(customer.items())
# Step 7: Remove and print the last inserted item
removed = customer.popitem()
print(removed)
# Step 8: Use .get() to access "membership"
print(customer.get("membership", "no membership"))
# Step 9: Update dictionary with "address"
customer.update({"address":"some"})
# Step 10: Print final dictionary
print(customer)
