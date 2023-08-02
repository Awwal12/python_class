import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Student:
    def __init__(self, first_name, last_name, phoneNumber):
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber

    def __str__(self) -> str:
        return self.first_name


class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='attendancemanager'
        )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

    def add_new_student(self, student: Student):
        self.__cursor.execute(f'INSERT INTO {self.studentT} (first_name, last_name, phone_number) VALUES (%s, %s, %s)', (
            student.first_name, student.last_name, student.phoneNumber))
        self.__db.commit()

    def get_all_data(self, tableName):
        self.__cursor.execute(f'SELECT * FROM {tableName}')
        return self.__cursor.fetchall()

    def update_firstname(self, F_NAME, ID):
        self.__cursor.execute(
            f'UPDATE {self.studentT} SET first_name = "{F_NAME}" WHERE student_id = {ID} ')
        self.__db.commit()

    def update_lastname(self, L_NAME, ID):
        self.__cursor.execute(
            f'UPDATE {self.studentT} SET last_name = "{L_NAME}" WHERE student_id = {ID} ')
        self.__db.commit()

    def update_phoneNumber(self, P_NUM, ID):
        self.__cursor.execute(
            f'UPDATE {self.studentT} SET phone_number = "{P_NUM}" WHERE student_id = {ID} ')
        self.__db.commit()

    def mark_attendance(self, id: int):
        self.__cursor.execute(
            f'INSERT INTO {self.presentT} (student_id) VALUE (%s)', (id,)
        )
        self.__db.commit()


class AttendanceSystem:
    def __init__(self) -> None:
        self.db = DB()
        self.attendance_record = {}
        self.student_record = []

    def add_student(self, student: Student):
        for _student in self.db.get_all_data('student'):
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.add_new_student(student)

    def update_f_name(self, id, firstname):
        self.db.update_firstname(firstname, id)

    def update_l_name(self, id, lastname):
        self.db.update_lastname(lastname, id)

    def update_phone_number(self, id, phoneNumber):
        self.db.update_phoneNumber(phoneNumber, id)

    def display_all_students(self):
        return self.db.get_all_data('student')

    # def mark_attendance(self, id):
    #     date = datetime.datetime.now().date()
    #     for student in self.student_record:
    #         if student.id == id:
    #             if date in self.attendance_record.keys():
    #                 self.attendance_record[date].append(student)
    #             else:
    #                 self.attendance_record[date] = [student]
    #             break
    #     else:
    #         raise StudentNotFound
    def mark_attendance(self, id):
        for values in self.db.get_all_data('present'):
            if (str(values[1])[:10] == str(datetime.datetime.now())[:10]):
                if values[2] == id:
                    raise Exception

        else:
            self.db.mark_attendance(id)

    def check_attendance_punctuality(self, id):
        for values in self.db.get_all_data('present'):
            if (values[1]).date() == (datetime.datetime.now()).date():
                if values[2] == id:
                    print('early')

    def add_attendance(self, id):
        self.db.mark_attendance(id)


student1 = Student('John', 'James', '234566')
student2 = Student('James', 'John', '234566')
student4 = Student('Mohammed', 'ben', '6789124566')

manager = AttendanceSystem()
# manager.add_student(student1)
# manager.add_student(student4)
manager.check_attendance_punctuality(1)
# manager.update_phone_number(1, "090999999999")
# print(manager.display_all_students())
# manager.add_attendance(2)
