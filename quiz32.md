# quiz 32



## paper solution
![photo_5249020691293006768_y](https://github.com/user-attachments/assets/eb8346a0-f1e0-4323-9a3d-84690df059f8)


## UML diagram
![image](https://github.com/user-attachments/assets/f280b2ec-7a73-470b-b3e5-3ade1d477ff6)


## code
            class HumanResources:
                def __init__(self, name:str, email:str, nationality:str, occupation:str):
                    self.name = name
                    self.email = email
                    self.nationality = nationality
                    self.occupation = occupation
            
                def get_email(self):
                    return self.email
            
                def set_nationality(self, nationality: str):
                    self.nationality = nationality
            
                def set_email(self, email: str):
                    self.email = email
            
                def greet(self) -> str:
                    return f"Hello, my name is {self.name} and I work as a {self.occupation}. My contact information is email: {self.email}"


## proof of work
![image](https://github.com/user-attachments/assets/2f6d7906-6e6d-4337-bf11-6155d6c40e7d)

