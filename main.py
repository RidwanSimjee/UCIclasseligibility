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


def finding_compsci_courses(courses: list) -> list:
    """Takes out compsci courses from all course list, removes unnecessary information, and returns a new list of filtered dictionaries """
    compsci_courses = []
    for course in courses:
        if course["department"] == "COMPSCI" or course["department"] == "I&C SCI" and course["course_level"] == "Upper Division (100-199)":
            del course['course_level'], course['professor_history'], course['terms'], course['id'], course['department_alias'], course['school'], course['department_name']
            compsci_courses.append(course)
    return compsci_courses

def main():
    for course in finding_compsci_courses(grab_local_file()):
        print(course)

if __name__ == "__main__":
    main()