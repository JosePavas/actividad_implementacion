class Student:
    def __init__(self, name, age, grades:list) -> None:
        self.name = name
        self.age = age 
        self.grades:list = grades
    
    def add_grade(self, suma_grades, promedio, contar_grades):
        self.suma_grades = suma_grades
        self.promedio = promedio
        self.contar_grades = contar_grades
        suma_grades = 0
        for nota in self.grades:
            suma_grades += nota
        contar_grades = self.grades.__len__
        promedio = suma_grades / contar_grades
    
    def avarge_grades(seld):
        pass        
               