
age = 8
if age >=18:
    print("you are old enought to vote")
    
ages = 12
if ages < 4:
    price = 0
elif ages < 18:
    price = 25
elif ages < 65:
    price = 40
elif ages <= 65:
    price = 20
print(f"Your cost is ${price}.")