# Define a class named "Student"
class Student:
    def __init__(self, name, age):
        """
        Constructor method to initialize a Student object.
        :param name: The name of the student.
        :param age: The age of the student.
        """
        self.name = name
        self.age = age
        self.courses = []  # Initialize an empty list to store courses

    def enroll(self, course):
        """
        Method to enroll a student in a course.
        :param course: The name of the course to enroll in.
        """
        self.courses.append(course)
        print(f"{self.name} has enrolled in the {course} course.")

    def display_info(self):
        """
        Method to display information about the student.
        """
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        if self.courses:
            print("Enrolled Courses:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print("No courses enrolled yet.")

# Create two Student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Enroll students in courses
student1.enroll("Math")
student1.enroll("History")
student2.enroll("Science")

# Display information about students
print("\nStudent Information:")
student1.display_info()
print("\nStudent Information:")
student2.display_info()
