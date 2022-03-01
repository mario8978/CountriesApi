import json
import sys

import requests

URl_ALL = "https://restcountries.com/v2/all"
URl_NAME = "https://restcountries.com/v2/name/"

def request(url):
    try:
        answer = requests.get(url)
        if answer.status_code == 200:
            return answer.text

    except:
        print("error making request")

def parsing(text_answer):
    try:
        return json.loads(text_answer)
    except:
        print("error making parsing")


def count_countries():
    answer = request(URl_ALL)
    if answer:
        list_countries = parsing(answer)
        if list_countries:
            return len(list_countries)


def show_population(country_name):
    answer = request(URl_NAME + country_name)
    if answer:
        list_countries = parsing(answer)
        if list_countries:
            for country in list_countries:
                print("{}: {}".format(country['name'],country['population']))

    else:
        print("country not found")


def show_currency(country_name):
    answer = request(URl_NAME + country_name)
    if answer:
        list_countries = parsing(answer)
        if list_countries:
            for country in list_countries:
                print("currencies of {}".format(country['name']))
                currencies = country['currencies']
                for currency in currencies:
                    print("{} - {}".format(currency['name'], currency['code']))

    else:
        print("country not found")


def reed_name_country():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("you need to give the name of the country")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("welcome to the system of countries")
        print("Use: python country.py <action> <country name> ")
        print("available steels:count, currencies,population  ")

    else:
        argument1 = sys.argv[1]
        if argument1 == "count":
            countries_number = count_countries()
            print("exist {} countries in the world".format(countries_number))

        elif argument1 == "currencies":
            country = reed_name_country()
            if country:
                show_currency(country)

        elif argument1 == "population":
            country = reed_name_country()
            if country:
                show_population(country)
        else:
            print("invalid argument ")
