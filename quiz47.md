# quiz 47

## UML diagram
![image](https://github.com/user-attachments/assets/587125d2-7a47-4cb8-a574-493436ea7bf8)

## code
          class CalorieCount:
              def __init__(self, daily_limit: int):
                  self.daily_limit = daily_limit
                  self.daily_intake = 0
                  self.protein = 0
                  self.carbs = 0
                  self.fat = 0
          
              def addMeal(self, cal: int, pro: int, car: int, fat: int):
                  self.daily_intake += cal
                  self.protein += pro
                  self.carbs += car
                  self.fat += fat
          
              def getProteinPercentage(self) -> float:
                  if self.daily_intake == 0:
                      return 0.0
                  return (4 * self.protein) / self.daily_intake
          
              def onTrack(self) -> bool:
                  return self.daily_intake <= self.daily_limit


## proof of work
![image](https://github.com/user-attachments/assets/1a0ec6d7-ba81-48f0-8d66-b5ddde5bec83)
