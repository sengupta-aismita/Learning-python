masala = ("cardamom", "cloves", "cinnamon")

(sp1, sp2, sp3) = masala

print(f"spices : {sp1}, {sp2}") #unpacking

a, b = 2, 1
print(f"Ratio is : {a} :  {b}")
a, b = b, a
print(f"Ratio is : {a} :  {b}")

#membership

print(f"is ginger in masala spices ? {'ginger' in masala} ")
print(f"is ginger in masala spices ? {'cinnamon' in masala} ")

sugar_levels = [1,2,3,4,5]
print(f"Maximum : {max(sugar_levels)}")

base_liquid = ["water", "milk"]
extra = ["ginger"]

mix = base_liquid + extra #operator overloading...same operators can do multiple task

print(f"extra 3 times : {extra * 3}")

raw_spice = bytearray(b"Cinnamon") #return new array of bytes, mutable
print(f"Bytes: {raw_spice}")

# | for all, & for intersection, - for only, frozenset --cannot be changed after its created
# for sets use curly braces {}


