import csv

from ..models import Student


def load_students(filename):
    students = []

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            name = row[0]
            scores = [float(x) for x in row[1:]]
            students.append(Student(name, scores))

    return students