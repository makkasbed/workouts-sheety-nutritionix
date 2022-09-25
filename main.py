import requests
import os
import datetime


def get_nutrition_details(query):
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    payload = {
        "query": query
    }
    headers = {
        "x-app-id": os.getenv("N_APP_ID"),
        "x-app-key": os.getenv("N_API_KEY")
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def save_to_sheet(exercise, duration, calories):
    url = os.getenv("ENDPOINT_API")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic '+os.getenv("AUTH")
    }
    payload = {
        "workout": {
            "date": datetime.date.today().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%-H:%M:%-S"),
            "exercise": str(exercise),
            "duration": str(duration),
            "calories": str(calories)
        }
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, json=payload)
    return response.json()


def manage(query):
    resp = get_nutrition_details(query)
    exercises = resp['exercises']
    for exercise in exercises:
        name = str(exercise['name']).title()
        calories = exercise['nf_calories']
        duration = exercise['duration_min']
        result = save_to_sheet(name, duration, calories)
        print(result)


print(manage("I run to ArdeyMan for 1 hour, 39 minutes and completed 9km"))
