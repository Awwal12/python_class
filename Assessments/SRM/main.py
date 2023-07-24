class DuplicateStudentIDError(UserWarning):
    pass


class StudentNotFoundError(UserWarning):
    pass


class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age

    def format_data(self):
        return f'{self.id} {self.name} {self.age}'


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        with open("student_records.txt", "w+") as file:
            for text in file.readlines():
                if text == student:
                    raise DuplicateStudentIDError
                print('here')
            file.write(student + "\n")

    def get_student(self, id):
        with open("student_records.txt", "r+", encoding='utf-8') as file:
            for text in file.readlines():
                if str(id) == text.split(' ')[0]:
                    return text.strip('\n')
            raise StudentNotFoundError

    def update_student(self, student: Student) -> None:
        with open("student_records.txt", "a", encoding="utf-8") as file:
            for text in file.readlines():
                if str(student.split(' ')[0]) == text.split(' ')[0]:
                    file.writelines(student + "\n")
                else:
                    raise StudentNotFoundError


manager = StudentRecordManager()

student1 = Student(1, "Moh", 33)
manager.add_student(student1.format_data())
print(manager.get_student(1))
