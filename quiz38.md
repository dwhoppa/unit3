# quiz 38

## Python code

              from kivymd.app import MDApp
              from kivy.uix.screenmanager import ScreenManager, Screen
              from kivy.lang import Builder
              
              class MysteryPageA(Screen):
                  pass
              
              class MysteryPageB(Screen):
                  pass
              
              class MysteryApp(MDApp):
                  def build(self):
                      return Builder.load_file("mystery.kv")  # Load KV file
              
                  def message1(self):
                      print("This is mystery page A, you pressed the button")
              
                  def message2(self):
                      print("This is mystery page B, you pressed the button")
              
              MysteryApp().run()
              
## Layout code
              ScreenManager:
                  MysteryPageA:
                  MysteryPageB:
              
              <MysteryPageA>:
                  name: "page_a"
                  BoxLayout:
                      orientation: "vertical"
                      spacing: "20dp"
                      padding: "20dp"
                      pos_hint: {"center_x": 0.5, "center_y": 0.5}
              
                      MDRaisedButton:
                          text: "Go to Page B"
                          size_hint_x: 0.6
                          pos_hint: {"center_x": 0.5}
                          on_press: app.root.current = "page_b"
              
                      MDRaisedButton:
                          text: "Press me"
                          size_hint_x: 0.6
                          pos_hint: {"center_x": 0.5}
                          on_press: app.message1()
              
              <MysteryPageB>:
                  name: "page_b"
                  BoxLayout:
                      orientation: "vertical"
                      spacing: "20dp"
                      padding: "20dp"
                      pos_hint: {"center_x": 0.5, "center_y": 0.5}
              
                      MDRaisedButton:
                          text: "Go to Page A"
                          size_hint_x: 0.6
                          pos_hint: {"center_x": 0.5}
                          on_press: app.root.current = "page_a"
              
                      MDRaisedButton:
                          text: "Press me"
                          size_hint_x: 0.6
                          pos_hint: {"center_x": 0.5}
                          on_press: app.message2()

## proof of work
<img width="809" alt="Screenshot 2025-01-31 at 8 13 17" src="https://github.com/user-attachments/assets/e52af54c-13a4-49f3-8702-740b480ab3ad" />
<img width="807" alt="Screenshot 2025-01-31 at 8 13 39" src="https://github.com/user-attachments/assets/53194304-f0bc-4c82-9cdb-e131ad4da1ea"/>
<img width="1440" alt="Screenshot 2025-01-31 at 8 16 15" src="https://github.com/user-attachments/assets/2d3eee0a-df70-4cd9-a9ec-5dfb71e3fc42" />


