# quiz 44

## UML diagram
![image](https://github.com/user-attachments/assets/6168653d-adf5-481d-b0d6-019ea5cf12d7)

## code
              class rainDrops:
                  def pour(self, n: int) -> str:
                      result = ""
                      if n % 3 == 0:
                          result += "Pling"
                      if n % 5 == 0:
                          result += "Plang"
                      if n % 7 == 0:
                          result += "Plong"
                      return result if result else str(n)
              
              rd = rainDrops()
              print(rd.pour(28))
              print(rd.pour(30))
              print(rd.pour(34))

## proof of work
![image](https://github.com/user-attachments/assets/593c012e-75c1-4b71-9573-5dd56e592523)
