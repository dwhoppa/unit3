# quiz 43

## UML diagram
![image](https://github.com/user-attachments/assets/ad3e2182-65c6-4dc3-906f-8cbc455682e4)

## code
          class palNum:
              def __init__(self, A: int, B: int):
                  self.A = A
                  self.B = B
          
              def get_pal_list(self):
                  return [i for i in range(self.A, self.B + 1) if str(i) == str(i)[::-1]]

## proof of work
![image](https://github.com/user-attachments/assets/eb2294f3-d3d6-4cad-9445-f44c6ff63909)

