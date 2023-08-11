import scraping
import json

prereq_set = set()


def filtering_compsci_courses(courses: list) -> list:
    """Takes out compsci courses from all course list, removes unnecessary information, and returns a new list of filtered dictionaries """
    compsci_courses = dict()
    for course in courses:
        if (course["department"] == "COMPSCI" or course["department"] == "I&C SCI") and course["course_level"] == "Upper Division (100-199)":
            del course['course_level'], course['professor_history'], course['terms'], course['id'], course['department_alias'], course['school'], course['department_name']
            compsci_courses[course['department'] + ' ' + course['number']] = course
            prereq_set.update(course['prerequisite_list'])
    return compsci_courses

def prereqs() -> None:
    """Collects the information on what courses the user has already taken. Still needs ability to redact a course."""
    user_prereqs = set()
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

def offer_course_suggestions(prereq_tree) -> None:
    if prereq_tree.strip() == '': return True
    else: recursive_prerequisite_breakdown(json.loads(prereq_tree))

def recursive_prerequisite_breakdown(prereq_tree: dict|bool) -> bool:
    if 'AND' in prereq_tree:
        for branch in prereq_tree['AND']:
            if type(branch) == dict:
                branch = recursive_prerequisite_breakdown(branch)
            if (type(branch) == str and branch not in prereq_set) or (type(branch) == bool and not branch):
                return False
        return True
    elif 'OR' in prereq_tree:
        for branch in prereq_tree['OR']:
            if type(branch) == dict:
                branch = recursive_prerequisite_breakdown(branch)
            if (type(branch) == str and branch in prereq_set) or (type(branch) == bool and branch):
                return True
        return False


    """
    if prereq_tree.strip() == '':
        return True
    else: #{"AND": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}
        prereq_tree = prereq_tree.split('{') #['"AND": ["I&C SCI 33", "I&C SCI 61",' , '"OR": ["MATH 3A", "I&C SCI 6N"]}]}']
    current = prereq_tree[len(prereq_tree)-1] # '"OR": ["MATH 3A", "I&C SCI 6N"]}]}'
    elements = current[current.index('[') + 1:current.index(']')].split(',')
    if current.startswith("\"OR\""):
        for element in elements:
            if element.strip().strip('\"') in prereq_set:
                return True
        return False
    elif current.startswith("\"AND\""):
        for element in elements:
            if element.strip().strip('\"') not in prereq_set:
                return False
        return True
    """


def main():
#    for course in filtering_compsci_courses(grab_local_file()):
#       print(course)
    offer_course_suggestions(filtering_compsci_courses(grab_local_file()))
 #   prereqs()

if __name__ == "__main__":
    main()