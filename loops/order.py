n = int(input("Enter number of names : "))
names = []
bills = []
for i in range(n):
    names.append(input("Enter a name : "))
    bills.append(input("Enter the amount : "))

for name,bill in zip(names,bills):
    print(f"{name} paid {bill} rupees")