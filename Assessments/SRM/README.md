Problem: Student Record Management

You are tasked with implementing a Student Record Management system that allows users to add, retrieve, and update student records. The student records should be stored in a text file.

Requirements:

1. Implement a class called "Student" with the following attributes:

   - id (int): unique identifier for each student
   - name (str): name of the student
   - age (int): age of the student

2. Implement a class called "StudentRecordManager" with the following methods:

   - add_student(student: Student) -> None: Adds a new student record to the file.
   - get_student(id: int) -> Student: Retrieves a student record based on the given ID.
   - update_student(student: Student) -> None: Updates an existing student record in the file.

3. Implement proper error handling for the following scenarios:

   - When adding a student, if the student ID already exists, raise a custom exception called "DuplicateStudentIDError".
   - When retrieving a student, if the student ID does not exist, raise a custom exception called "StudentNotFoundError".

4. Implement file handling to read and write student records from/to a text file. Each line in the file represents a student record in the following format: "id,name,age".

Instructions:

1. Implement the classes "Student" and "StudentRecordManager" according to the given requirements.
2. Write a text file called "student_records.txt" with sample student records.
3. Test your implementation by adding new students, retrieving student records, and updating existing student records.

Example usage:

```
manager = StudentRecordManager()

# Adding a new student
student1 = Student(1, "John Doe", 20)
manager.add_student(student1)

# Retrieving a student
student2 = manager.get_student(1)
print(student2.name)  # Output: "John Doe"

# Updating a student
student2.age = 21
manager.update_student(student2)

# Retrieving the updated student
student3 = manager.get_student(1)
print(student3.age)  # Output: 21
```

Note:

- You may assume that the text file "student_records.txt" already exists and contains valid student records in the specified format.
- You can choose any method you prefer to read from and write to the text file.
- Make sure to handle any potential errors or exceptions that may occur during file operations or record retrieval.
