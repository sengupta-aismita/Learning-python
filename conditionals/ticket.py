seat = input("Enter your seat type (sleeper/AC/general/luxury): ").lower()

match seat:
    case "sleeper":
        print("Sleeper - NoAC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy")
    case "general":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")                