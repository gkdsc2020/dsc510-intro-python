# DSC510
# Week 10
# Programming Assignment - 10.1
# Author: Ganesh Kale
# Date: 02/20/2021
# The purpose of this program is to read data from open api and parse it.

import requests
from requests.exceptions import HTTPError

api_url = 'https://api.chucknorris.io/jokes/random'
message = 'Would you like to read Chuck Norris joke? "Yes/No or Y/N"\n'
user_response = input(message)
count = 0  # counter to allow user give 3 total invalid responses before quiting
while user_response:
    if user_response.lower() in ['yes', 'y']:      # user_response.lower() == 'yes' or user_response.lower() == 'y':
        try:
            print('Retrieving......\n')
            response = requests.get(api_url)     # store the response from the api
            response.raise_for_status()
            data = response.json()  # raising the standard http errors
            print('Here you go:\n')
            joke_lines_list = data['value'].split('.')
            if len(joke_lines_list) > 1:
                for line in joke_lines_list:
                    print(line.strip())
            else:
                print(joke_lines_list[0])
            user_response = input("\nWould you like to read more Chuck Norris Jokes?\n")
            count = 0           # resetting counter 0 for successful read
        except HTTPError as err:
            print('Error has occurred while retrieving Joke:', err)
            break
        except Exception as ex:
            print('Error has occurred while retrieving Joke:', ex)
            break

    elif user_response.lower() in ['no', 'n']:   # user_response.lower() == 'no' or user_response.lower() == 'n':
        print('Thank you for visiting our site...See you again!!!')
        break
    else:
        count += 1
        if count < 2:
            print('Please enter valid options: "Yes/No or Y/N"')
            user_response = input(message)
        elif count == 2:
            print('If you really want to read Chuck Norris Jokes then type: "Yes/No or Y/N"')
            user_response = input(message)
        elif count == 3:
            print('It seems not a valid option, Thank you for visiting our site...See you again!!!')
            break


