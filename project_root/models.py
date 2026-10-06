from utils import mean, letter_grade


# 한 명의 학생 정보를 저장하는 클래스
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    # 평균 계산
    def average(self):
        return mean(self.scores)

    # 학점 계산
    def grade(self):
        return letter_grade(self.average())


# 여러 학생의 성적을 관리하는 클래스
class GradeBook:
    def __init__(self):
        self.students = []

    # 학생 추가
    def add_student(self, student):
        self.students.append(student)

    # 전체 반 평균 계산
    def class_average(self):
        total = 0
        for s in self.students:
            total += s.average()
        return total / len(self.students)