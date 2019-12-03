# Nested data in list and dictionaries

mix_list = ['strings', 98, ['more strings', [1, 2, 'important']]]

# print(type(mix_list[2]))
#
# internal_list = mix_list[2]
#
# print(mix_list[2][1][2])
# print(internal_list[1][2])

### /////////////////////

embeded_dict = {
    'status': 'operational',
    'key1': ['car keys', 'boat keys', 'mansion keys', 'dog house'],
    'staff': {
        'Julio Cesar': {
            'First_Name': 'Julio',
            'Last_Name': 'Cesar',
            'Birth_Date': 1979,
            'Football_club': 'Flamengo'
        },
        'Julia Venus': {
            'First_Name': 'Julia',
            'Last_Name': 'Venus',
            'Birth_Date': 1969,
            'Football_Club': 'Cuba FC.'
        }
    }
}

# Print:
## boat keys and dog house
## inside the key 'staff', print the dictionary with the key 'julio cesar'
## from the dictionary with the key 'julia venus', print:
### the last name, the birthdate and the football club

print(embeded_dict['key1'][1])
print(embeded_dict['key1'][-1])
print(embeded_dict['staff']['Julio Cesar'])
print(embeded_dict['staff']['Julia Venus']['Last_Name'])
print(embeded_dict['staff']['Julia Venus']['Birth_Date'])
print(embeded_dict['staff']['Julia Venus']['Football_Club'])