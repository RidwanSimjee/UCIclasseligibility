import requests
import json

prereq_set = set()
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
    compsci_courses = dict()
    for course in courses:
        if (course["department"] == "COMPSCI" or course["department"] == "I&C SCI") and course["course_level"] == "Upper Division (100-199)":
            del course['course_level'], course['professor_history'], course['terms'], course['id'], course['department_alias'], course['school'], course['department_name']
            compsci_courses[course['department'] + ' ' + course['number']] = course
            prereq_set.update(course['prerequisite_list'])
    return compsci_courses

def prereqs() -> None:
    user_prereqs = set()
    print(prereq_set)
    print("\nSelect the classes that you have already taken, seperated by commas. (in the form: CSE 1,I&C SCI 2,COMPSCI 3, etc..)")
    prereq_input = input().upper()
    while prereq_input != "F":
        for inputted_prereq in prereq_input.split(','):
            inputted_prereq = inputted_prereq.strip()
            if not inputted_prereq in prereq_set:
                print("\n"+inputted_prereq + " was not in the prerequisite list and was not added.")
            else:
                user_prereqs.add(inputted_prereq)
        print("\nChosen classes:")
        print(user_prereqs)
        print("\nNon-chosen classes:")
        print(prereq_set - user_prereqs)
        print("\nIs that all? Choose more completed courses or type \"f\" when finished.")
        prereq_input = input().upper()

def main():
#    for course in finding_compsci_courses(grab_local_file()).items():
#        print(course)
    finding_compsci_courses(grab_local_file())
    prereqs()

if __name__ == "__main__":
    main()