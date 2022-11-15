

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)


magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I cant wait to see your next trick, {magician.title()}")
    
for value in range(1,5):
    print(value)
    
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

players = ['charles','jeff','sam','roger','ellie','vivi']
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'sushi', 'cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

# tuples - same as lists but use () instead of []
dimensions = (200,5)
print(dimensions[0])
print(dimensions[1])

requested_toppings = []
if requested_toppings:
    for request_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza")
else:
    print("you want an plain pizza?")
    
    

list = [10,20,30,40,50,60,70,80,90,100]
print(list[1:3:4])    #list[start:stop:step]  
print(list[:-1:])
list.__contains__[list]
