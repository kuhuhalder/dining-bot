import os
import requests
import json
import jsonify
api_result  =requests.get('https://rumobile.rutgers.edu/2/rutgers-dining.txt') 
user_request = "Brower Commons\nBreakfast"
user_request = user_request.split("\n")
location_name = str(user_request[0])
meal_name = str(user_request[1])

data = api_result.json()
formatted_response = ""
if api_result.status_code == 200:
        formatted_response = ""
        for item in data:
            if item['location_name'] == location_name:
                for meal in item['meals']:
                    if meal['meal_name'] == meal_name:
                        for genre in meal['genres']:
                            genre_name = genre['genre_name']
                            items = genre['items']
                            formatted_response += genre_name + ":" + "\n"
                            for item_name in items:
                                formatted_response += "- "+ item_name + "\n"
print(formatted_response)

