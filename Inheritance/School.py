# Make a class structure in python representing people at school. Make a base class called Person, a class called
# Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong
# to different classes, and keep in mind which are common and which are not. For example, the name should be a Person
# attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, name, last_name, city, age):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.age = age


class Student(Person):
    def __init__(self, name, last_name, city, age, study_year, grade, marks):
        Person.__init__(self, name, last_name, city, age)
        self.study_year = study_year
        self.grade = grade
        self.marks = marks


class Teacher(Person):
    def __init__(self, name, last_name, city, age, work_experience, sallary, responsibility):
        Person.__init__(self, name, last_name, city, age)
        self.work_experience = work_experience
        self.sallary = sallary
        self.responsibility = responsibility


vlad = Person("Vlad", "Hladkyi", "Kiev", "28")
print(vlad.name, vlad.last_name, vlad.city, vlad.age)
daria = Student("Daria", "Hladka", "Lutsk", 18, "second", "bachelor", "12, 10, 11")
print(daria.name, daria.last_name, daria.city, daria.age, daria.study_year, daria.grade, daria.marks)
olena = Teacher("Olena", "Kushniruk", "Luboml", "40", "20", "3000", "2 classes")
print(olena.name, olena.last_name, olena.city, olena.age, olena.work_experience, olena.sallary, olena.responsibility)
