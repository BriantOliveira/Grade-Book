from student import Student

class Classroom(object):
    '''
    Classroom object that will act as high-level interface for operations on classroom
    full of students.
    Each Classroom object contains the following attributes:
    _____Attributes_______
    class_name:  String. The name of the class.
    teacher_name: String.  The name of the teacher responsible for the class.
    class_day_and_time:  The days the class meets.
    roster: Dictionary {student_ID (Int): student_object (Student)}. A dictionary of
    students enrolled in the class.  Dictionary is empty on initialization.
    _____Methods________
    init(self, class_name, teacher_name, class_day_and_time):
        - Expects all inputs (aside from self) to be passed as a String.
    enroll_student(student_name):
        - Expects student_name as string.
        - Creates a new student object.
        - Sets the new student's student_ID to self.next_available_student_number
        - increments self.next_available_student_number by 1.
        - adds to roster dictionary, with new student's student_ID as key and student
            object as value.
    add_assignment_for_student(student_name, assignment_name, grade):
        - searches roster for student with student_name.
            - if student does not exist, prints and error message.
        - calls student object's add_assignment() method with assignment_name and grade
            as inputs.
    add_assignment_for_class(assignment_name):
        - Expects assignment_name as String.
        - Loops through each student in self.roster.values().
        - For each student, prints message asking teacher to add grade for student.name
        - Once user has entered input, validates input using _is_valid_grade() method.
            - if input is not valid, asks user again for input.
        - If user input is valid, calls student's add_assignment() method and continues
            through loop.
    drop_assignment_for_student(student_name, assignment_name):
        -  Expects student_name as String.
        -  Expects assignment_name as String.
        -  Loops through roster.values() and finds student with student_name passed in.
            - If student does not exist, prints error message saying so.
        -  Calls student's delete_assignment() method, with assignment_name as input.
    drop_assignment_for_class(assignment_name):
        -  Expects assignment_name as String.
        -  Loops through each student in self.roster.values()
            - Calls student's delete_assignment() method with assignment_name as input.
    get_student_GPA(student_name):
        - Expects student_name as String.
        - Searches self.roster for student with student_name.
            - If no student with that name, prints error message saying so.
        - If found, returns that student's self.GPA attribute.
    get_class_average():
        -  Expects no inputs.
        -  Iterates through all students in self.roster.values() and returns the average
            of their GPA attributes.
    '''

    def __init__(self, class_room_name, instructor_name, class_time_and_day):
        self.class_room_name = class_room_name
        self.instructor_name = instructor_name
        self.class_time_and_day = class_time_and_day
        self.next_available_student_number = 1
        self.roster = {}

    def enroll_student(self, student_name):
        new_student = Student(student_name, self.next_available_student_number)
        self.next_available_student_number += 1
        self.roster[new_student_student_ID] = new_student
        print(new_student.name + ' enrolled sucessfully!')

    def add_homework_for_student(self, student_name, homework_name, grade):
        """ add students homework """
        for student in self.roster.values():
            if student.name == student_name
                student.add_homework(homework_name, grade)

    def _is_correct_grade(self, grade):
        try:
            correct_grade = float(grade)
            if correct_grade >= 0:
                return True
        except ValueError:
            return False
    def __add__class_activity__(self, activity_name):
        for student in self.roster.values():
            grade = ""
            while not _is_correct_grade(grade):
                grade = float(input("Enter {}'s grade for {}: ".format(student.name, activity_name)))

                student.add_activity(activity_name, grade)
    def drop_homework_for_student(self, student_name, homework_name):
        for student in self.roster.values():
            if student.name == student_name
                student.delete_homework(homework_name)

    def drop_class_activity(self, activity_name):
        for student in self.roster.values():
            student.delete_activity(activity_name)

    def get_student_GPA(self, student_name):
        for student in self.roster.values():
            if student.name == student_name
                return student.GPA

    def get_class_average(self):
        if len(self.roster) == 0:
            print("No student enrolled...")
            return None
        else:
            point_total = sum([i.GPA for i in self.roster.values()])
            class_average = point_total / len(self.roster)
            return class_average
