

cat_weight = [("Snowshoe", 15), ("Siamese", 20), ("Persian", 12)]

for cat, weight in cat_weight:
    print("Cat is a %s and it weighs %s pounds" % (cat , weight))
    
    
#######

print('this is new code')


number = input("enter a number and I'll tell you if its even or odd:  ")
number = int(number)

# modulo operator (%) divides a number by another number and returns the remainder. so if modulo of a number and two is 0, the number is even. otherwise its odd.
if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")
    
    
######

party = input("How many people in your party?  ")
party = int(party)

if party >= 10:
    print("you have too many people in your party")
else:
    print("your table is ready")