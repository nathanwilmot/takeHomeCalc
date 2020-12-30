#work out the take home pay after tax

x = input("What is your annual salary?")
if float(x) < 37500:
    salary = (float(x) * 0.8) / 12 
    print("Your monthly takehome after tax is:",salary)
if float(x) > 37500:
    salary = (float(x) - 37500)* 0.6 /12 + (30000 / 12)
    print("Your monthly takehome after tax is:",salary)