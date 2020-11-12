import json
import statistics
import logging
import functools


def CheckArgumentsWrapper(object):
    def create_function_with_argument_check(function):
        def function_with_argument_check(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except KeyError:
                return f"The argument should be one of the existing {object}"
        return function_with_argument_check
    return create_function_with_argument_check


@CheckArgumentsWrapper("Student")
def get_student_average_score(student):
    return statistics.mean(student['marks'])


@CheckArgumentsWrapper("Student")
def check_attendance(student):
    present = list(
        filter(lambda is_present: is_present, student['attendance']))
    return len(present)/len(student['attendance'])


@CheckArgumentsWrapper('highschool class')
def get_class_average_score(highschool_class):
    students_average_score_list = []
    for student in highschool_class['students']:
        students_average_score_list.append(get_student_average_score(student))
    return statistics.mean(students_average_score_list)


@CheckArgumentsWrapper('highschool class')
def get_class_average_attendance(highschool_class):
    students_average_attendance = []
    for student in highschool_class['students']:
        students_average_attendance.append(check_attendance(student))
    return statistics.mean(students_average_attendance)


@CheckArgumentsWrapper('highschool')
def get_highschool_average_score(highschool):
    class_average_score_list = []
    for highschool_class in highschool['classes']:
        class_average_score_list.append(
            get_class_average_score(highschool_class))
    return statistics.mean(class_average_score_list)


@CheckArgumentsWrapper('highschool')
def get_highschool_average_attendance(highschool):
    class_average_attendance = []
    for highschool_class in highschool['classes']:
        class_average_attendance.append(
            get_class_average_attendance(highschool_class))
    return statistics.mean(class_average_attendance)


def load_highscool_data(json_file_name):
    with open(json_file_name, 'r') as json_file:
        json_object = json.load(json_file)
    return json_object


@CheckArgumentsWrapper("schools")
def print_general_info_about_school(schools):
    for school in schools:
        print(f"""School name: {school['name']}
            School average score: {get_highschool_average_score(school)}
            School average attendance: {get_highschool_average_attendance(school)}""")
        for school_class in school['classes']:
            print(
                f"""    Class {school_class['level']} 
                Class average score: {get_class_average_score(school_class)},
                Class average attendance: {get_class_average_attendance(school_class)}""")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    schools = load_highscool_data("data.json")

    print_general_info_about_school(schools)
