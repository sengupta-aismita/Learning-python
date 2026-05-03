num = int(input("How many people are there in your group ? "))
for i in range(num):
    input(f"Name of person {i+1} : ").split()

total_bill = int(input("Enter the total bill amount : "))
avg = round(total_bill / num, 2)

print(f"Each person owes : {avg}")