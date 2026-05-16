import pandas as pd

# Global variable
GRADE_THRESHOLDS = {
    "A": (90, 100),
    "B": (80, 89),
    "C": (70, 79),
    "D": (60, 69),
    "F": (0, 59)
}

# Helper function
def calculate_grade(score):
        for grade, (low, high) in GRADE_THRESHOLDS.items():
            if low <= score <= high:
                return grade


class Subject:
    def __init__(self, name, score):
        self.name = name
        self.score = score
  
    @property
    def grade(self):
        return calculate_grade(self.score)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            print("Score must be in the range of 0-100")
        

    def __str__(self):
        return f"{self.name} | {self.score} | {self.grade}"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, name):
        subject = next((s for s in self.subjects if s.name == name), None)
        if subject:
            self.subjects.remove(subject)
        else:
            print(f"Subject: {name} is not studied by Student: {self.name}")

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"], data["student_id"])
        student.subjects = data["subjects"]
        return student

    @property
    def average_score(self):
        if self.subjects:
            average_score = sum(s.score for s in self.subjects)/len(self.subjects)
            return average_score
        else:
            print("Error: There must be atleast one subject")

    @property
    def average_grade(self):
        if self.average_score is not None:
            return calculate_grade(self.average_score)
    
    @property
    def top_subject(self):
        return max(self.subjects, key=lambda subject:subject.score)
    
    def get_report(self):
        print(f"--- {self.name}'s Report Card ---")
        for subject in self.subjects:
            print(subject)
        print(f"{"-"*28}\nAverage: {self.average_score:.2f} | {self.average_grade}\n{"-"*28}")

    def __str__(self):
        return f"Name: {self.name} | ID: {self.student_id} | Average: {self.average_score:.2f} | {self.average_grade}"
    

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        student = next((s for s in self.students if s.name == name), None)
        if student:
            self.students.remove(student) 
        else:
            print(f"Student: {name} is not in Classroom: {self.name}")

    @staticmethod
    def is_passed(students):
        return [student for student in students if student.average_score > 59]

    @property
    def top_student(self):
        return max(self.students, key=lambda student:student.average_score)
    
    @property
    def average_score(self):
            if self.students:
                return sum(student.average_score for student in self.students)/len(self.students)
            else:
                print("Error: There must be atleast one student")

    @property
    def average_grade(self):
            if self.average_score is not None:
                return calculate_grade(self.average_score)

    def __str__(self):
        return f"Class: {self.name} | Students: {len(self.students)} | Average: {self.average_score:.2f} | {self.average_grade}"


# Creating students
student1 = Student("George", "678955")
student2 = Student("Ronald", "738262")
student3 = Student("Albert", "271387")

# Creating subjects
subject1 = Subject("Maths", 92)
subject2 = Subject("Physics", 78)
subject3 = Subject("Computer Science", 89)

subject4 = Subject("Maths", 75)
subject5 = Subject("Physics", 67)
subject6 = Subject("Computer Science", 75)

subject7 = Subject("Maths", 83)
subject8 = Subject("Physics", 76)
subject9 = Subject("Computer Science", 85)

# Testing setter
subject10 = Subject("Additional Maths", 200)
subject11 = Subject("Additional Maths", -100)

# Adding subjects to students
student1.add_subject(subject1)
student1.add_subject(subject2)
student1.add_subject(subject3)

student2.add_subject(subject4)
student2.add_subject(subject5)
student2.add_subject(subject6)

student3.add_subject(subject7)
student3.add_subject(subject8)
student3.add_subject(subject9)

# Printing reports for students
student1.get_report()
student2.get_report()
student3.get_report()

# Creating classroom
classroom1 = Classroom("Section-D")

# Adding students to classroom
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

# Fetching top student object and accessing it's name attribute
classroom1.top_student.name

# Removing a subject from a student
student1.remove_subject("Machine Learning")

# Adding data to a dataframe
data = []
for student in classroom1.students:
    data.append({
        "name": student.name,
        "student_id": student.student_id,
        "average_score": student.average_score,
        "average_grade": student.average_grade,
        "top_subject": student.top_subject.name,
        "total_subjects": len(student.subjects)
    })
df = pd.DataFrame(data)
print(df)

# Locate and print students with average scores greater than 75
print(df.loc[df["average_score"] > 75])