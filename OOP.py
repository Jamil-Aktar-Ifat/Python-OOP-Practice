def method_name(a, b):
    print("A method!")

class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht=None) -> None:
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht
    

    def get_name(self):
        return self.__name
    
    def get_year_of_birth(self):
       return self.__date_of_birth
    
    def set_name(self, new_name):
        if(self._has_any_number(new_name)):
            print("Sorry! person name cant't  have number.")
            return
        self.__name = new_name

    def _has_any_number(self, string):
        return any(char.isdigit() for char in string)
    
    
 
    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invaild'}"


method_name(10, 20)
a_person = Person("Jamil", 2002, 72)
# b_person = Person("Ifat")


person_list = [Person("Jamil", 2002, 74),
               Person("Aktar", 2003),
               Person("Ifat", 2004, 75),
               Person("Zora", 2005 ),
               Person("Pamiri", 2006, 77)]


# for person in person_list:
    # if person.get_year_of_birth() >=  2003:
        # print(person.get_summary())
        
        
        
        
class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str) -> None:
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email = email_id
        
    def get_summary(self):
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"
    
    def __str__(self) -> str:
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"
    
    def __repr__(self) -> str:
        return self.get_summary()
    
student = Student("Jamil", 2002, "jamil@meta.com", "1101A")
# print(student.get_summary())
student.set_name("Ifat")
# print(student)


class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, department: str) -> None:
        super().__init__(person_name, year_of_birth)
        self.dept = department
    def get_summary(self):
        return f"{self.get_name()} is a teacher of {self.dept} department!"
        
    
        
    
new_person_list = [
    Person("Jamil", 2002),
    Student("Faisal", 2004, "f@mail.com", "1001E"),
    Teacher("Paul", 1980, "CS")
]

for p in new_person_list:
    print(p.get_summary())
    # print(p.get_name())
    
    
class PlainClass:
    pass

abc = PlainClass()
abc.age = 30
abc.name = "Music"

print(abc.age)