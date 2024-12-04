# 3 자유프로그래밍 (학생출결관리시스템)
class Student:
    def __init__(self, name, student_id):
        self.name = name                # 학생 이름
        self.student_id = student_id    # 학생 ID
        self.attendance = []            # 출결 기록 리스트

    def check_in(self, date):
        """학생 출석 처리"""
        self.attendance.append({"date": date, "status": "Present"})
        print(f"{self.name}님이 {date}에 출석 처리되었습니다.")

    def check_out(self, date):
        """학생 결석 처리"""
        self.attendance.append({"date": date, "status": "Absent"})
        print(f"{self.name}님이 {date}에 결석 처리되었습니다.")

    def view_attendance(self):
        """학생의 전체 출결 기록 확인"""
        print(f"{self.name}님의 출결 기록:")
        for record in self.attendance:
            print(f" - {record['date']}: {record['status']}")


class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name       # 교실 이름
        self.students = []              # 교실의 학생 리스트

    def add_student(self, student):
        """교실에 학생 추가"""
        self.students.append(student)
        print(f"{student.name}님이 {self.room_name} 교실에 추가되었습니다.")

    def view_students(self):
        """교실의 모든 학생 목록 출력"""
        print(f"{self.room_name} 교실 학생 목록:")
        for student in self.students:
            print(f" - 이름: {student.name}, ID: {student.student_id}")

    def attendance_summary(self):
        """교실의 출결 요약 출력"""
        print(f"{self.room_name} 교실의 출결 요약:")
        for student in self.students:
            present_count = sum(1 for record in student.attendance if record['status'] == "Present")
            absent_count = sum(1 for record in student.attendance if record['status'] == "Absent")
            print(f" - {student.name}: 출석 {present_count}회, 결석 {absent_count}회")


class School:
    def __init__(self, name):
        self.name = name                 # 학교 이름
        self.classrooms = []             # 학교의 교실 리스트

    def add_classroom(self, classroom):
        """학교에 교실 추가"""
        self.classrooms.append(classroom)
        print(f"'{classroom.room_name}' 교실이 {self.name}에 추가되었습니다.")

    def list_classrooms(self):
        """학교의 모든 교실 목록 출력"""
        print(f"{self.name}의 교실 목록:")
        for classroom in self.classrooms:
            print(f" - {classroom.room_name}")
