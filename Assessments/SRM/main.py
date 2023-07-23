class DuplicateStudentIDError:
    pass


class StudentNotFoundError:
    pass


class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        with open("student_records.txt", "r+") as f:
            for x in f:
                if x == student:
                    raise Exception("DuplicateStudentIDError")
                else:
                    f.writelines()

    def get_student(self, id: int) -> Student:
        pass  # Retrieves a student record based on the given ID

    def update_student(self, student: Student) -> None:
        pass  # Updates an existing student record in the file
