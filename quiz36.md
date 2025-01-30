# quiz 36

## Python code

              from kivymd.app import MDApp
              from kivy.lang import Builder
              
              
              class MyNameApp(MDApp):
                  dark_mode = False
              
                  def build(self):
                      return Builder.load_file("yournamescreen.kv")
                  def toggle_mode(self):
                      screen = self.root.ids.main_screen
                      label = self.root.ids.title_label
                      button = self.root.ids.toggle_button
              
                      if self.dark_mode:
                          screen.md_bg_color = [1, 1, 1, 1]
                          label.theme_text_color = "Primary"
                          button.text = "Dark Mode"
                          button.md_bg_color = [0, 0, 1, 1]
                      else:
                          screen.md_bg_color = [0, 0, 0, 1]
                          label.theme_text_color = "Custom"
                          label.text_color = [1, 1, 1, 1]
                          button.text = "Light Mode"
                          button.md_bg_color = [1, 0, 0, 1]
              
                      self.dark_mode = not self.dark_mode
              
              MyNameApp().run()
              
## Layout code
              MDScreen:
                  id: main_screen
                  md_bg_color: 1, 1, 1, 1  
              
                  MDBoxLayout:
                      orientation: "vertical"
                      size_hint: .8, .8
                      pos_hint: {"center_x": .5, "center_y": .5}
                      spacing: "20dp"
              
                      MDLabel:
                          id: title_label
                          text: "Your Name"
                          font_style: "H4"
                          halign: "center"
                          theme_text_color: "Primary"
              
                      MDRaisedButton:
                          id: toggle_button
                          text: "Dark Mode"
                          md_bg_color: 0, 0, 1, 1  
                          size_hint_x: .6
                          pos_hint: {"center_x": 0.5}
                          on_press: app.toggle_mode()

## proof of work
![image](https://github.com/user-attachments/assets/a0f100b6-baa0-4a18-98a6-65e43eaa1015)
![image](https://github.com/user-attachments/assets/284213bd-8843-41bc-991d-521c3e2d6ccc)

