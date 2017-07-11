# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    
class Pupil(Person):
    def __init__(self, id, first_name, last_name, father, mother, grade):
        Person.__init__(self, id, first_name, last_name)
        self.father = father
        self.mother = mother
        self.grade = grade    
    

class Teacher(Person):
    def __init__(self, id, first_name, last_name, subjects):
        Person.__init__(self, id, first_name, last_name)
        self.subjects = subjects

    def __str__(self):
        return "{} {}. {}".format(self.first_name, self.last_name, self.subjects)

    def __repr__(self):
        return "{} {}. {}".format(self.first_name, self.last_name,self.subjects)



    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name, self.father,
                              self.mother)

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Grade:
    def __init__(self, id, number, letter, pupils, teachers):
        self.id = id
        self.number = number
        self.letter = letter
        self.pupils = pupils
        self.teachers = teachers

    def __str__(self):
        return "{}{}. {}. {}".format(self.number, self.letter, self.schoolboys, self.teachers)

    def __repr__(self):
        return "{}{}. {}. {}".format(self.number, self.letter, self.schoolboys, self.teachers)


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class School:
    def __init__(self, name, teachers, grades, pupils):
        self.name = name
        self.teachers = teachers
        self.levels = levels
        self.pupils = pupils

    def __str__(self):
        return "{}".format(self.name)

    def show_all_grades(self):
        for grade in grades:
            print("{}{}. List of schoolboys: /n {}".format(grade.number, drade.letter, grade.pupils))

    def show_all_pupils_in_grade(self, grade_id):
        print(self.grades[grade_id].pupils)

    def show_pupil_subjects(self, pupil_id):
        grade = self.pupil[pupil_id].grade
        teachers = self.grades[grade].teachers
        for t in teachers:
            print(teachers[t].subjects)

    def get_teachers_by_grade(self, grade_id):
        grade = self.grades[grade_id]
        print(grade.teachers)