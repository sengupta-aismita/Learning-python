device_status = input("Enter your device_status : ").lower()

    
temp = input("Enter temperature : ")

if device_status == "active":
    if temp > "35":
        print("High temperature alert!")
    else:
        print("Normal temperature")    
else: 
    print("Device is offline")    