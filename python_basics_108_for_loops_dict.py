# Continuation of for loops

dict_data = {
    1: {
        'Name': 'Bronson', 'Money': 0.50
    },
    2: {
        'Name': 'Janet', 'Money': 3.50
    },
    3: {
        'Name': 'Bartolumeu', 'Money': 1.50
    },
    4: {
        'Name': 'Vanessa', 'Money': 0.23
    }
}

# When you do a simple for loop on a dictionary you get the individual keys
# for key in dict_data:
#     print(key, '-->', dict_data[key])


# We want the name of the person and how much they owe us, after we apply the interest (4000%)
for key in dict_data:
    print(dict_data[key]['Name'], 'owes us: ', (dict_data[key]['Money']*4000/12)+ dict_data[key]['Money'])

for values in dict_data.values():
    print(values)


