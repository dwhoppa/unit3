# quiz 35



## paper solution
![image](https://github.com/user-attachments/assets/6c0452f1-8be4-47d4-8da4-99db54c2334b)


## UML diagram
![image](https://github.com/user-attachments/assets/3184d9ff-382c-4c7c-b2a5-a8014144a20d)


## code

            class Person:
                def __init__(self, name: str, age: int):
                    self.name = name
                    self.age = age
            
                def get_name(self) -> str:
                    return self.name
            
                def get_age(self) -> int:
                    return self.age
            
            
            class Student(Person):
                def __init__(self, name: str, age: int, grade: str):
                    super().__init__(name, age)
                    self.grade = grade
            
                def get_grade(self) -> str:
                    return self.grade
            
            
            student = Student("Bob", 18, "A")
            print(student.get_name())
            print(student.get_age())
            print(student.get_grade())


## proof of work
![image](https://github.com/user-attachments/assets/f4194d9d-d55d-4d9e-a6bb-9f58330e421f)



