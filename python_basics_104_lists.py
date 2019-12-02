# Lists in Python
# Lists are ordered by index
## AKA --> Arrays or (confusingly) as objects in JavaScript

# Syntax
# Declare lists using []
    # Separate objects using ,
# var_list_name = [0 , 1, 2, 3,..] --> index numbers
crazy_x_landlords = ['Sr. Julio', 'Jane', 'Alfred', 'Marksons']

print(crazy_x_landlords)
print(type(crazy_x_landlords))

# How to access record number 3 in the list: --> record number - 1
print(crazy_x_landlords[2])

# Accessing other location
print(crazy_x_landlords[0])
print(crazy_x_landlords[-1])

# New list of places to live
places_to_live = ['California', 'Rio de Janeiro', 'Melbourne', 'Manchester', 'Singapore']

# Re-assign an index
places_to_live[3] = 'Hawaii'

print(places_to_live[3])

# Method .append(object)
print(len(places_to_live))
places_to_live.append('LA')
print(len(places_to_live))
print(places_to_live)

# .insert(index,,object)
places_to_live.insert(0, 'Lisboa')
print(places_to_live)

# .pop(index) --> removes from list at specific index
places_to_live.pop(3)
print(places_to_live)

# List slicing
    # This is used to manage lists

# Prints from index to end of the list
print(places_to_live[3:])
# Prints from index to the start of the list (not inclusive the index '3')
print(places_to_live[:3])

# Print from specified index to second specified index (not inclusive of the index)
print(places_to_live[0:3])
print(places_to_live[1:3])

# Skip slicing
list_exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(list_exp)
print(list_exp[2:10:3])
print(list_exp[::-1])


# Tuples --> Immutable lists
# Syntax
    # Defined using (object, object)

mortal_enemies = ('Mario', 'Sailormoon', 'MOON CAKE', 'Jerry', 'Berry')

print(type(mortal_enemies))

# If you try re-assign it will break

# print(mortal_enemies[0]) = 'Goku'
# print(mortal_enemies)