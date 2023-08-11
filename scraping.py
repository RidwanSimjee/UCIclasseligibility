import requests
import json

def make_api_call() -> list:
    """Makes the api call to peterportal for the current list of all courses and returns the list of dictionaries"""
    response = requests.get("https://api.peterportal.org/rest/v0/courses/all")
    return response.json()

def grab_local_file() -> list:
    """Gets the local .txt file in the same format as the api call (to not strain the api while building this application)"""
    with open('all_courses.json', 'r', encoding = 'utf-8') as local_file:
        text = json.loads(local_file.read())
    return text