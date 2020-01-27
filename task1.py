class Student:
    def __init__(self, name, lastname, year_of_entrance, department):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        result = (f"{self.name.title()} {self.lastname.title()}, поступил в {self.year_of_entrance}, на факультет {self.department.title()}")
        return result

i_am_student = Student('semetei', 'abaildaev', 2008, 'geology')
print(i_am_student.get_student_info())