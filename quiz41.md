# quiz 41

## ER diagram
![image](https://github.com/user-attachments/assets/67856ff9-571b-4331-8140-ba403938e556)

## code
              class database_worker:
                  def __init__(self, name):
                      self.connection = sqlite3.connect(name)
                      self.cursor = self.connection.cursor()
              
                  def search(self, query):
                      result = self.cursor.execute(query).fetchall()
                      return result
              
                  def run_save(self, query):
                      self.cursor.execute(query)
                      self.connection.commit()
              
                  def close(self):
                      self.connection.close()
              
              
              class quiz047(MDApp):
                  def __init__(self, **kwargs):
                      super().__init__(**kwargs)
                      self.components = {"basic":0}
              
                  def build(self):
                      return
              
                  def save(self):
                      pass
              
                  def update(self):
                      #This function updates all the labels in the form using the base salary and the percentage
                      # Pseudocode
                      # 1- get the base salary from the GUI
                      # 2- if base salary define total=int(base) and an empty string to store build a hash (for_hash="") if no base then end the function
                      # 3- for Each TextField with ids: "inhabitant","income_tax","pension","health" get the text property
                      # 4- if the TextField.text has a number (value), calculate the equation new_value="(base*int(value)//100) JPY" and subbctract the equation to the total
                      # 5- if no: then new_value = " JPY"
                      # 6- set the label next to the TextField (inhabitant_label, income_tax_label, etc) to the variable new_value
                      # 7- concatenate to the hash variable the f"{id}{value}"
                      # 8- set the text of the element id=total to the total with the JPY symbol
                      # 9- encrypt the hash and change the text of the label with id=hash to the last 50 characters of the hash
              
                      #calculate total
                      ids = ["inhabitant", "income_tax", "pension", "health"]
              
                      # update the percentage
              
              
              
                  def save(self):
                      #repeat the algorithm in update but create variables to save the amount of each item:
                      #base = int(base)
                      #inhabitant = amount in JPY to remove from base for inhabitant tax
                      #income_tax = amount in JPY to remove from base for income tax
                      #pension = amount in JPY to remove from base for pension tax
                      #health = amount in JPY to remove from base for health tax
                      #total = total net salary
                      #hahs = hash of the calcualtions in the format
                      #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)
              
                      # query = f"""INSERT into payments
                      # --here complete the code
                      #
                      # """
                      # db = database_worker("payments.db")
                      # db.run_save(query)
                      # db.close()
                      self.root.ids.hash.text = f"Payment saved"
              
                  def clear(self):
                      for label in ["base", "inhabitant","income_tax","pension","health"]:
                          self.root.ids[label].text = ""
                          self.root.ids[label+"_label"].text = " JPY"
              
                      self.root.ids["salary_label"].text = " JPY"
                      self.root.ids.hash.text = "----"
              
              
              test = quiz047()
              # create = """CREATE TABLE if not exists payments(
              #
              #
              # --- Complete here the table
              #
              #
              #     )"""
              # db = database_worker("payments.db")
              # db.run_save(create)
              # db.close()
              test.run()
                
                MDScreen:
                    id:bck
                    size: 200, 500
                
                    MDBoxLayout:
                        id: bck
                        size_hint: .8,.9
                        md_bg_color: "#F2F2F2"
                        orientation: "vertical"
                        pos_hint: {"center_x":.5, "center_y":.5}
                        spacing: dp(10)
                
                        MDLabel:
                            text:"Compensation Calculator"
                            halign: "center"
                            font_style:"H4"
                            color: "#222222"
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                            MDIcon:
                                icon: "plus-circle"
                                pos_hint: {"center_x": .5, "center_y": .5}
                            MDLabel:
                                text:"Base Salary"
                                size_hint_x: .4
                            MDTextField:
                                id:base
                                mode: "rectangle"
                                input_filter:"int"
                                text_color_normal: "#222222"
                                line_color_normal: "#222222"
                                hint_text: "Base Salary"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_text:
                                    root.ids.base_label.text = f"{self.text} JPY"
                                    app.update()
                            MDLabel:
                                id: base_label
                                text:" JPY"
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                
                            MDIcon:
                                icon: "minus-circle"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                color: "#9d0208"
                            MDLabel:
                                text:"Health"
                                size_hint_x: .4
                                color: "#6a040f"
                            MDTextField:
                                id:health
                                mode: "rectangle"
                                input_filter:"int"
                                hint_text: "% Health"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                text_color_normal: "#9d0208"
                                line_color_normal: "#9d0208"
                                on_text:
                                    self.text = str(max(0, min(100, int(self.text or 0))))
                                    app.update()
                            MDLabel:
                                id: health_label
                                text:" JPY"
                                color: "#9d0208"
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                
                            MDIcon:
                                icon: "minus-circle"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                color: "#9d0208"
                            MDLabel:
                                text: "Pension"
                                size_hint_x: .4
                                color: "#9d0208"
                            MDTextField:
                                id:pension
                                mode: "rectangle"
                                input_filter:"int"
                                hint_text: "% Pension"
                                text_color_normal: "#9d0208"
                                line_color_normal: "#9d0208"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_text:
                                    self.text = str(max(0, min(100, int(self.text or 0))))
                                    app.update()
                            MDLabel:
                                id: pension_label
                                text:" JPY"
                                color: "#9d0208"
                
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                            MDIcon:
                                icon: "minus-circle"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                color: "#9d0208"
                            MDLabel:
                                text:"Income Tax"
                                size_hint_x: .4
                                color: "#9d0208"
                            MDTextField:
                                id:income_tax
                                mode: "rectangle"
                                input_filter:"int"
                                hint_text: "% Income"
                                text_color_normal: "#9d0208"
                                line_color_normal: "#9d0208"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_text:
                                    self.text = str(max(0, min(100, int(self.text or 0))))
                                    app.update()
                            MDLabel:
                                id: income_tax_label
                                text:" JPY"
                                color: "#9d0208"
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                
                            MDIcon:
                                icon: "minus-circle"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                color: "#9d0208"
                            MDLabel:
                                text:"Inhabitant Tax"
                                size_hint_x: .4
                                color: "#9d0208"
                            MDTextField:
                                id:inhabitant
                                mode: "rectangle"
                                input_filter:"int"
                                hint_text: "%  Income"
                                text_color_normal: "#9d0208"
                                line_color_normal: "#9d0208"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_text:
                                    self.text = str(max(0, min(100, int(self.text or 0))))
                                    app.update()
                            MDLabel:
                                id: inhabitant_label
                                text:" JPY"
                                color: "#9d0208"
                
                
                        MDBoxLayout:
                            size_hint_x: .8
                            height: dp(46)
                            valign: "center"
                            md_bg_color: "#22223b"
                            pos_hint: {"center_x":.5, "center_y":.5}
                            spacing: dp(10)
                
                            MDLabel:
                                size_hint_x: .5
                            MDIcon:
                                icon: "calculator"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                color: "#F2F2F2"
                            MDLabel:
                                text:"Net Salary"
                                size_hint_x: .4
                                color: "#F2F2F2"
                            MDLabel:
                                id: salary_label
                                text:" JPY"
                                color: "#F2F2F2"
                            MDFloatingActionButton:
                                icon:"content-save-plus"
                                md_bg_color:"#ffc300"
                                icon_color:"#222222"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press:
                                    app.save()
                
                            MDFloatingActionButton:
                                icon:"autorenew"
                                md_bg_color:"#2a9d8f"
                                icon_color:"#222222"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press:
                                    app.clear()
                
                        MDBoxLayout:
                            size_hint: .8, .2
                            valign: "center"
                            md_bg_color: "#FFFFFF"
                            pos_hint: {"center_x":.5, "center_y":.5}
                
                            MDLabel:
                                id: hash
                                halign: "center"
                                text: "----"
                                font_style: "Caption"
              
## proof of work
![image](https://github.com/user-attachments/assets/44465d6c-fe4f-4db3-abfb-5f5de0c8a285)
