import scraping
import json

user_prereqs = set()

def filtering_compsci_courses(courses: list) -> (dict, set):
    """Takes out compsci courses from all course list, removes unnecessary information, and returns a new dictionary of filtered dictionaries """
    compsci_courses = dict()
    prereq_set = set()
    for course in courses:
        if (course["department"] == "COMPSCI" or course["department"] == "I&C SCI") and course["course_level"] == "Upper Division (100-199)":
            del course['course_level'], course['professor_history'], course['terms'], course['id'], course['department_alias'], course['school'], course['department_name']
            compsci_courses[course['department'] + ' ' + course['number']] = course
            prereq_set.update(course['prerequisite_list'])
    return compsci_courses, prereq_set

def prereqs(prereq_set: set) -> None:
    """Collects the information on what courses the user has already taken. Still needs ability to redact a course."""
    #user_prereqs = set()
    print(sorted(prereq_set))
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
        print(sorted(user_prereqs))
        print("\nNon-chosen classes:")
        print(sorted(prereq_set - user_prereqs))
        print("\nIs that all? Choose more completed courses or type \"f\" when finished.")
        prereq_input = input().upper()

def recursive_prerequisite_breakdown(prereq_tree: dict) -> bool:
    if 'AND' in prereq_tree:
        for branch in prereq_tree['AND']:
            if type(branch) == dict:
                branch = recursive_prerequisite_breakdown(branch)
            if (type(branch) == str and branch not in user_prereqs) or (type(branch) == bool and not branch):
                return False
        return True
    elif 'OR' in prereq_tree:
        for branch in prereq_tree['OR']:
            if type(branch) == dict:
                branch = recursive_prerequisite_breakdown(branch)
            if (type(branch) == str and branch in user_prereqs) or (type(branch) == bool and branch):
                return True
        return False

def offer_course_suggestions(courses: dict) -> list:
    possible_courses = list()
    for course in courses.values():
        if course['prerequisite_tree'].strip() == '':
            possible_courses.append(course)
        elif recursive_prerequisite_breakdown(json.loads(course['prerequisite_tree'])):
            possible_courses.append(course)
    return possible_courses


def main():
    scrape, prereq_set = filtering_compsci_courses(scraping.grab_local_file())
    prereqs(prereq_set)
    for suggestion in offer_course_suggestions(scrape):
        print(suggestion)


if __name__ == "__main__":
    main()