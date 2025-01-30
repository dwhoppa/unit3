# quiz 34



## paper solution
![image](https://github.com/user-attachments/assets/da1a9a45-9b31-4e2a-91a6-854396e39489)


## UML diagram
![image](https://github.com/user-attachments/assets/9fe3a37c-c1ad-4a04-9016-92a8229c802c)


## code

        class Flight:
            def __init__(self, row: int, seat: str):
                self.row = row
                self.seat = seat
        
            def greet(self) -> str:
                return f"Welcome aboard! Your seat is in row {self.row}, seat {self.seat}."
        
        
        flight = Flight(12, "B")
        print(flight.greet())


## proof of work
<img width="1440" alt="Screenshot 2025-01-31 at 2 00 17" src="https://github.com/user-attachments/assets/258a4e2b-f309-4e2f-a4d0-f32507c0f975" />


