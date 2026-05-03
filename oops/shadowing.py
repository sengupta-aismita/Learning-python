class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print(cutting.temperature)
print(cutting.cup)

print(Chai.temperature)

del cutting.temperature
print(cutting.temperature)
# del cup.temperature
# print(cup.temperature)

#if there's no fallback it will fALLBACK TO THE CLASS ITSELF IF IT DOESNT HAVE A CLASS IT HAS no fallback for it