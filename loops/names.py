n = int(input("Enter number of names : "))
names = []
for i in range(n):
    names.append(input("Enter a name : "))

for name in names:
    print(f"Order ready for {name}")    

#enumerate for printing menu items with numbers
for idx,item in enumerate(names, start = 1):
    print(f"Order ready for :{item} #{idx}")