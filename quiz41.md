# quiz 41

## ER diagram
![image](https://github.com/user-attachments/assets/67856ff9-571b-4331-8140-ba403938e556)

## code

              from kivymd.app import MDApp
              from my_lib import DatabaseManager
              
              class quiz047(MDApp):
                  def __init__(self, **kwargs):
                      super().__init__(**kwargs)
                      self.components = {"basic": 0, "health": 0, "income_tax": 0, "inhabitant": 0, "total": 0, "pension": 0}
                      self.db_connection = DatabaseManager("payments.db")
              
                  def build(self):
                      return
              
                  def update(self):
                      ids = ["inhabitant", "income_tax", "pension", "health"]
                      base = self.root.ids.base.text
                      if base:
                          base_int = int(base)
              
                          pension = int(self.root.ids.pension.text or '0')
                          health = int(self.root.ids.health.text or '0')
                          income_tax = int(self.root.ids.income_tax.text or '0')
                          inhabitant = int(self.root.ids.inhabitant.text or '0')
              
                          pension_jpy = base_int * pension // 100
                          health_jpy = base_int * health // 100
                          income_tax_jpy = base_int * income_tax // 100
                          inhabitant_jpy = base_int * inhabitant // 100
              
                          self.root.ids.pension_label.text = f"{pension_jpy} JPY"
                          self.root.ids.health_label.text = f"{health_jpy} JPY"
                          self.root.ids.income_tax_label.text = f"{income_tax_jpy} JPY"
                          self.root.ids.inhabitant_label.text = f"{inhabitant_jpy} JPY"
                          total = base_int - pension_jpy - health_jpy - income_tax_jpy - inhabitant_jpy
                          self.root.ids.salary_label.text = f"{total} JPY"
              
                          self.components['total'] = total
                          self.components['base'] = base_int
                          self.components['pension'] = pension_jpy
                          self.components['health'] = health_jpy
                          self.components['income_tax'] = income_tax_jpy
                          self.components['inhabitant'] = inhabitant_jpy
              
                  def save(self):
                      total = self.components['total']
                      base_int = self.components['base']
                      pension_jpy = self.components['pension']
                      health_jpy = self.components['health']
                      income_tax_jpy = self.components['income_tax']
                      inhabitant_jpy = self.components['inhabitant']
              
                      query = f"""INSERT INTO payments (base, inhabitant, income_tax, pension, health, total)
                      VALUES ({base_int}, {inhabitant_jpy}, {income_tax_jpy}, {pension_jpy}, {health_jpy}, {total})
                      """
                      self.db_connection.run_query(query)
                      self.root.ids.hash.text = f"Payment saved"
              
                  def clear(self):
                      for label in ["base", "inhabitant", "income_tax", "pension", "health"]:
                          self.root.ids[label].text = ""
                          self.root.ids[label + "_label"].text = " JPY"
              
                      self.root.ids["salary_label"].text = " JPY"
              
              test = quiz047()
              create = """CREATE TABLE IF NOT EXISTS payments (
                      id INTEGER PRIMARY KEY,
                      base INT,
                      health INT,
                      pension INT,
                      income_tax INT,
                      inhabitant INT,
                      total INT
                  )"""
              
              my_db = DatabaseManager("payments.db")
              my_db.run_save(query=create)
              
              sql_query = "SELECT * FROM payments"
              
              results = my_db.search(query=sql_query)
              
              for row in results:
                  base_int = row[1]
                  health_jpy = row[2]
                  pension_jpy = row[3]
                  income_tax_jpy = row[4]
                  inhabitant_jpy = row[5]
                  total = row[6]
                  print(f"Base: {base_int}, Health: {health_jpy}, Pension: {pension_jpy}, Income Tax: {income_tax_jpy}, Inhabitant: {inhabitant_jpy}, Total: {total}")
              
              my_db.close()
              test.run()
              test.db_connection.close()

                
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
![image](https://github.com/user-attachments/assets/a38fd1ff-78c9-4ad5-89e3-79a969d0175d)

