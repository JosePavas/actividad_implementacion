class Student:
    def __init__(self, name, age, grades:list) -> None:
        self.name = name
        self.age = age 
        self.grades:list = grades
    
    def add_grade(self, nota):
         self.grades.append(nota)
        
    
    def avarage_grade(self):
        
        suma_grades = sum(self.grades)
        contar_grades = len(self.grades)
        promedio = suma_grades / contar_grades
        return promedio
lista = [
    {
        "name":"jose",
        "age":20, 
        "grades":[1,2,3,4,5]
    },
    {
       "name":"andres",
       "age":23,
       "grades":[3,4,5,1,1] 
        },
    {
        "name":"alejandra",
        "age":21,
        "grades":[4,4,5,3,2]
    }]

lc = [Student(name=estudiante["name"], age=estudiante["age"], grades=estudiante["grades"]) for estudiante in lista]
for elemento in lc:
    print(elemento.name)
#Student("alberto",19,[1,2,3,4,5])
lc2 = [Student(name=nota["name"], age=nota["age"], grades=nota["grades"]) for nota in lista 
       if sum(nota["grades"]) / len(nota["grades"]) <= 3]

dt = {Student(name=i["name"]) : Student(name=i["name"], age=i["age"], grades=i["grades"]) for i in lista 
      if sum(i["grades"]) / len(i["grades"]) >= 3}
    