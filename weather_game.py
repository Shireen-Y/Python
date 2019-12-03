# Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'

import time
weather = {'sunny': 'sun', 'stormy': 'storm/thunder', 'rainy': 'rain', 'rainy and stormy': 'rain and storm/thunder'}
print('Please choose from the following:')
time.sleep(1)
for key in weather:
    print(key)
    time.sleep(1)
weather_response = input('What is the weather like today? ')
if weather_response == (weather['sunny']):
    print('Do not forget to take your shorts!')
elif

# if age < 21 and age > 18:
#     print('You can vote, but unfortunately cannot drink')
# elif age >= 18:
#     print('You can vote, please register :)')
# elif age > 16:
#     print('You can drive in the US')
# else:
#     print('You are a child')

