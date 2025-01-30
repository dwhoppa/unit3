# quiz 33



## paper solution
![image](https://github.com/user-attachments/assets/cc4debef-7fbe-4e33-8e6c-dcb4e69136e5)


## UML diagram
![image](https://github.com/user-attachments/assets/0ccb0bdf-c0fc-4ce3-988a-3483b12f7b0f)



## code

        class CompoundInterest:
            def __init__(self, principal: float, rate: float):
                self.principal = principal
                self.rate = rate
        
            def calculate(self, years: int) -> float:
                return self.principal * (1 + self.rate) ** years
        
        
        ci = CompoundInterest(1000, 0.05)
        print(ci.calculate(6))


## proof of work
![image](https://github.com/user-attachments/assets/2fcc95c7-334e-4bab-8d3d-0ca1f389b6f3)


