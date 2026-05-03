import datetime

name = input("Enter your name : ").strip()
age = int(input("Enter your age : "))
city = input("Enter your city : ").strip()
profession = input("Enter your profession : ").strip()
hobby = input("Enter your favourite hobby : ").strip()

current_date = datetime.date.today().isoformat()

border = "*" * 80

print(f"""{border}\nHello! My name is {name}. I'm {age} years old and live in
      {city}.\nI work as a {profession} and I absolutely enjoy {hobby}
      in my free time.\nNice to meet you!
      Logged in on - {current_date}\n{border}""")

