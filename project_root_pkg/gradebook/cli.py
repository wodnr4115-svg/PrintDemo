import sys

from .models import Student, GradeBook
from .io.csvio import load_students


def main():
    gb = GradeBook()

    # CSV 파일이 지정된 경우
    if len(sys.argv) > 1:
        students = load_students(sys.argv[1])

        for student in students:
            gb.add_student(student)

    # CSV 파일이 지정되지 않은 경우 기본 데이터 사용
    else:
        gb.add_student(Student("Alice", [90, 85, 92]))
        gb.add_student(Student("Bob", [70, 75, 68]))

    print("전체 반 평균 점수:", round(gb.class_average(), 2))

    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")