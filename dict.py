

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")


alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_1['x_position']}")

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New Position: {alien_1['x_position']}")

####################################


user = {'username': 'jlew24asu', 'first': 'jeff', 'last': 'lewis'}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
    
########
favorite_programming = {
    
    'jeff': 'python',
    'sam': 'C++',
    'eddy': 'ruby',
    'stephen': 'saltstack'
}

for name,program in favorite_programming.items():
    print(f"{name.title()}'s favorite program is {program.title()}")


####

print("this is new code")

favorite_programming = {
    
    'jeff': 'python',
    'sam': 'C++',
    'eddy': 'ruby',
    'stephen': 'saltstack'
}

for name in favorite_programming.keys():
    print(name.title())
    
###

print('this is new code')

favorite_programming = {
    
    'jeff': 'python',
    'sam': 'C++',
    'eddy': 'ruby',
    'stephen': 'saltstack'
}

for name in sorted(favorite_programming.keys()):
    print(f"{name.title()}, thanks for everything")
    
    
####
print("this is new code for empty list")

aliens = []

for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:4]:
    print(alien)
print("....")


######

print('this is new code again')

favorite_programming = {
    
    'jeff': ['ruby', 'python'],
    'sam': ['C++'],
    'eddy': ['chef', 'ruby'],
    'stephen': ['k8s', 'saltstack']
}

for name, program in favorite_programming.items():
    print(f"\n{name.title()}'s favorite programs are:")
    for programming in program:
        print(f"\t{programming.title()}")

