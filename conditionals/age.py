age_str = int(input("Enter your age : "))

int(age_str)

verify_age = "Access Granted" if age_str >= 18 else "Access Denied"
print(verify_age)