

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


