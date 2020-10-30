# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.

class Student:
    def __init__(self, name, surname, *marks):
        self.name = name
        self.surname = surname
        self.frequency = 100
        self.marks = marks

    def get_average_score(self):
        scoreSum = 0
        for mark in self.marks:
            scoreSum += mark
        return scoreSum/len(self.marks)


class Highscool:
    def __init__(self, *studClasses):
        self.studClasses = studClasses

    def print_avarage_score_in_classes(self):

        countClass = 0
        for studClass in self.studClasses:
            scoreSum = 0
            countClass += 1
            for student in studClass:
                scoreSum += student.get_average_score()
            scoreAverage = scoreSum/len(studClass)
            print(
                f"The average score of class nr. {countClass} is {scoreAverage}"


if __name__ == "__main__":
    someSchool=Highscool([[Student("Adam", "Nowak", [4, 5, 3])]])
    someSchool.print_avarage_score_in_classes()
