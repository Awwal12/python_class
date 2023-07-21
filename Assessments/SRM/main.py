class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        pass  # Adds a new student record to the file.

    def get_student(self, id: int) -> Student:
        pass  # Retrieves a student record based on the given ID

    def update_student(student: Student) -> None:
        pass  # Updates an existing student record in the file
