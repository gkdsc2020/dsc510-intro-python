# DSC510
# Week 12
# Programming Assignment - Final Project
# Author: Ganesh Kale
# Date: 03/05/2021
# The purpose of this program is to Create Weather app.


import requests
import datetime
from requests.exceptions import HTTPError

message1 = 'Please enter the city or zip code to get weather information: OR\nFor USA locations enter city name, state code separated by comma (e.g:Boston,MA):\n'
message2 = 'Would you like to see temperatures in F:Fahrenheit or C:Celsius or K:Kelvin? \nPlease Enter your choice or enter any key to see in Fahrenheit \n'
end_point = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = '840f7d46836aac562ec7ae43d51ab402'
units_f = '&units=imperial'
units_c = '&units=metric'
bold_start = '\033[1m'
bold_end = '\033[0m'


# function to get user input and check entered value is zip code or city name and create api url based on it


def get_url(user_input, degree):
    if user_input.isdigit():
        query_string = f'zip={user_input}&APPID={api_key}'
        url = end_point+query_string+get_unit(degree)
        return url
    elif len(user_input.split(',')) > 1:
        city, state = user_input.split(',')   # api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
        query_string = f'q={city.strip()},{state.strip()},US&APPID={api_key}'
        url = end_point+query_string+get_unit(degree)
        return url
    else:
        query_string = f'q={user_input}&APPID={api_key}'
        url = end_point+query_string+get_unit(degree)
        return url

# function to get units based on user preference, default to F


def get_unit(degree):
    if degree in ['C', 'c']:
        return units_c
    elif degree in ['K', 'k']:
        return ''
    else:
        return units_f


# function to print the weather information for user


def show_weather(data, degree):
    if degree in ['C', 'c']:
        current_temp = round(data.get('main').get('temp'))
        current_temp = f'{current_temp}{chr(176)}C'
        feels_like = round(data.get('main').get('feels_like'))
        feels_like = f'{feels_like}{chr(176)}C'
        temp_min = round(data.get('main').get('temp_min'))
        temp_min = f'{temp_min}{chr(176)}C'
        temp_max = round(data.get('main').get('temp_max'))
        temp_max = f'{temp_max}{chr(176)}C'
        wind_speed = data.get('wind').get('speed')
        wind_speed = f'{wind_speed} m/s'
    elif degree in ['K', 'k']:
        current_temp = round(data.get('main').get('temp'))
        current_temp = f'{current_temp}{chr(176)}K'
        feels_like = round(data.get('main').get('feels_like'))
        feels_like = f'{feels_like}{chr(176)}K'
        temp_min = round(data.get('main').get('temp_min'))
        temp_min = f'{temp_min}{chr(176)}K'
        temp_max = round(data.get('main').get('temp_max'))
        temp_max = f'{temp_max}{chr(176)}K'
        wind_speed = data.get('wind').get('speed')
        wind_speed = f'{wind_speed} m/s'
    else:
        current_temp = round(data.get('main').get('temp'))
        current_temp = f'{current_temp}{chr(176)}F'
        feels_like = round(data.get('main').get('feels_like'))
        feels_like = f'{feels_like}{chr(176)}F'
        temp_min = round(data.get('main').get('temp_min'))
        temp_min = f'{temp_min}{chr(176)}F'
        temp_max = round(data.get('main').get('temp_max'))
        temp_max = f'{temp_max}{chr(176)}F'
        wind_speed = data.get('wind').get('speed')
        wind_speed = f'{wind_speed} mph'

    city = data.get('name')
    humidity = data.get('main').get('humidity')
    pressure = data.get('main').get('pressure')
    description = data.get('weather')[0].get('description')
    sunrise = data.get('sys').get('sunrise')
    sunset = data.get('sys').get('sunset')
    sunrise = datetime.datetime.fromtimestamp(sunrise)
    sunset = datetime.datetime.fromtimestamp(sunset)

    print('*'*50)
    print(f"{bold_start} {city.upper():^43} {bold_end}")
    print(f'{description.title():^45}')
    print(f'{bold_start} {current_temp:^43} {bold_end}')
    print(f"{f'Feels Like:{feels_like}':^45}")
    print(f"{f'High:{temp_max} | Low:{temp_min}':^45}")
    print(f"{f'Sunrise:{str(sunrise)[11:16]} UTC | Sunset:{str(sunset)[11:16]} UTC':^45}")
    print(f"{f'Humidity:{humidity}% | Pressure:{pressure} hPa | Wind:{wind_speed}':^45}")
    print('*'*50)


def main():
    print('+'*30)
    print(' Welcome to Weather Channel!!!')
    print('+'*30)
    count = 0
    user_input = input(message1)
    while True:
        if len(user_input) > 2 and not user_input == '':
            degree = input(message2)
            url = get_url(user_input, degree)
            print('Retrieving weather information.....\n')
            try:
                weather = requests.get(url)
                weather.raise_for_status()       # raise HTTP error other than 200 status code
            except HTTPError as err:
                error = weather.json()    # capture the message from error response
                if error.get('message') == 'city not found':     # if error message is 404 then allow user to enter correct details
                    print('Error has occurred while retrieving weather information, because:', error.get('message'))
                    # print('Would you like to enter correct details or "q" to quit now?')
                    user_input = input('Would like to re-enter correct city or zip or "q" to quit now?\n')
                    if user_input in ['q', 'Q']:
                        print('Thank you for visiting Weather Channel!!! \nSee You Again!!')
                        break
                    else:
                        continue
                else:
                    print('Error has occurred while retrieving weather information')
                    print('Thank you for visiting our channel, Please start over by providing city or zip code!!')
                    print('More information about error:', err)  # these details are logged to get more details about exception, not for user to view, here shown for info only
                    break

            data = weather.json()
            print('Weather Info retrieved successfully.....\n')
            show_weather(data, degree)
            print("Would you like to view weather information for other city? please enter the city or zip or 'q' to exit now?")
            user_input = input()
            if user_input in ['q', 'Q']:
                print('Thank you for visiting Weather Channel!!! \nSee You Again!!')
                break
            else:
                continue
        else:
            count += 1
            user_input = input('Please enter the valid city or zip code to see weather information or "q" to quit now:\n')

            if user_input in ['q', 'Q']:
                print('Thank you for visiting Weather Channel!!! \nSee You Again!!')
                break
            elif count >= 3 and len(user_input) < 3:        # allow user to enter city or zip code less than 3 chars for 4 times ina session and then exit
                print('It seems you entered City names or Zip codes are not valid.')
                print('Thank you for visiting Weather Channel!!! \nSee You Again!!')
                break
            else:
                continue


if __name__ == "__main__":
    main()
