# quiz 46

## UML diagram
![image](https://github.com/user-attachments/assets/42a45bac-81c7-4cd3-9d0d-bf2c19d7dbd9)

## code
            class Citizen:
                def __init__(self, name: str, city: str, status: str):
                    self.name = name
                    self.city = city
                    self.status = status
            
                def get_name(self) -> str:
                    return self.name
            
                def get_city(self) -> str:
                    return self.city
            
                def get_status(self) -> str:
                    return self.status
            
            
            class Employee(Citizen):
                def __init__(self, name: str, city: str, status: str, annual_salary: float):
                    super().__init__(name, city, status)
                    self.annual_salary = annual_salary
            
                def get_annual_salary(self) -> float:
                    return self.annual_salary
            
            
            class PartTimeEmployee(Employee):
                def __init__(self, name: str, city: str, status: str, annual_salary: float, fraction: float, union_member: bool):
                    super().__init__(name, city, status, annual_salary)
                    self.fraction = fraction
                    self.union_member = union_member
            
                def get_fraction(self) -> float:
                    return self.fraction
            
                def is_union_member(self) -> bool:
                    return self.union_member


## proof of work
![image](https://github.com/user-attachments/assets/0adbdc0c-3ec0-4d47-a42a-af3a8024ea12)
