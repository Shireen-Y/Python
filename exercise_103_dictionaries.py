# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the following keys:
        # hero_name, hero_age, start, middle and end
story1 = {'Hero Name': 'Ice Man', 'Hero Age': '24', 'Start': 'Young man realises his powers and understands its importance',
          'Middle': 'He starts to use his powers to help lock up criminals', 'End': 'He receives an Honour award from the Queen for his service'}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print(type(story1))

#4 - Print only the keys
for x in story1:
    print(x)

#5 - print only the values
for x in story1:
    print(story1[x])

#6 - print the individual values using the keys (individually, lots of printing commands)
print(story1['Hero Name'])
print(story1['Hero Age'])
print(story1['Start'])
print(story1['Middle'])
print(story1['End'])

#7 - Now let's reassign the exist key value pairs with user inputs
    # - hero_name, hero_age, hero_power
story1['Hero Name'] = input('What is your Hero name? ')
story1['Hero Age'] = input('How old is your hero? ')

#8 print the story in an organised/formated manor
print(story1['Start'])
print('He named himself ' + story1['Hero Name'] + '. He was ' + story1['Hero Age'] + ' years old.')
print(story1['Middle'])
print(story1['End'])