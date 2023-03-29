import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
url = 'https://rumobile.rutgers.edu/2/rutgers-dining.txt'
@app.route('/meals', methods=['POST'])
def meals():
    user_request = request.values.get('Body', '')
    user_request = user_request.split("\n")
    
    location_name = str(user_request[0].strip())
    meal_name = str(user_request[1].strip())
    resp = MessagingResponse()
    msg = resp.message()
    api_result = requests.get(url)
    data = api_result.json()
    formatted_response = ""
    if api_result.status_code == 200:
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
        msg.body(formatted_response)
    else:
        msg.body('Sorry, I am unable to get meal data for that dining hall.')

    return str(resp)

# @app.route('/meals', methods=['GET'])
# def get_message():
#     user_request = request.values.get('Body', '')
#     resp = MessagingResponse()
#     msg = resp.message()
#     msg.body('Hello! this is the Rutgers Dining Bot. Please send a message in the following format: "location_name meal_name". \n These are the dining halls available: Brower Commons, Livingston Dining Commons, Busch Dining Hall, Neilson DIning Hall. \n These are the meal names available: Breakfast, Lunch, Dinner, Late Night. \n Example: Brower Commons Breakfast, Lunch, Dinner, Knight Room, Late Knight.')
#     return str(resp)
    

if __name__ == '__main__':
    app.run(debug=True)
