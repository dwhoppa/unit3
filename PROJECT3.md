
# Unit 3: Moonlight bublles

## Criteria A: Planning

## Problem definition

The client, A.N., is the owner of Moonlight Bubbles, a popular Taiwanese drink shop in Japan. The shop, known for its classic boba milk tea, lemon black tea with jelly, mango green tea and matcha milk tea has gained a strong reputation. However, its rural location near Nagano, with the main factory in Suwa, makes it difficult for customers in major cities like Tokyo, Osaka, and Kyoto to access the drinks. Currently, there is no efficient way for customers outside the local area to place orders. Due to high demand, many customers are interested in bulk orders (over 10 cups), but the lack of a structured ordering system limits accessibility and sales growth. Without a dedicated platform, customers must visit the physical store or rely on indirect ordering methods, leading to inconvenience, lost sales opportunities, and limited market expansion. 

![giphy](https://github.com/user-attachments/assets/c5bbc0d3-5584-4584-ae2c-239722b97d51)


## Proposed Solution

I propose a solution for the problem by developing an application for Moonlight Bubbles, a store that aims to provide a bulk ordering platform, allowing customers in Tokyo, Osaka, and Kyoto to place large orders for delivery. The platform will feature a blue-themed, soft color design to match the brand’s aesthetic and provide a simple, user-friendly ordering process:
Drink Selection – Customers can choose from the four available drinks (classic boba milk tea, lemon black tea with jelly, mango green tea and matcha milk tea).
 - Customization Options – Users can adjust sweetness levels and ice levels to their preferences.
 - Bulk Ordering – Orders must be at least 10 cups, ensuring efficiency in delivery logistics.
 - Cart & Checkout System – Customers can add items to their cart and complete their purchase seamlessly.
 - Home Screen Navigation – After placing an order, users can return to the home screen for additional transactions.

## Tools of my solution

For the development of the ordering system, I decided to use a GUI (Graphical User Interface) application to provide an intuitive and user-friendly experience for customers. Unlike web-based solutions, a desktop GUI application does not require an internet connection, ensuring smooth operation even in remote areas. Python was chosen as the programming language due to its flexibility and extensive libraries, which allow for seamless integration of the user interface, backend processes, and database management. For storing data, I opted for SQLite, a lightweight and reliable relational database management system. SQLite enables secure local storage without the need for cloud-based services, reducing security risks and ensuring fast data access. This combination of tools makes the application efficient, secure, and scalable for future improvements

## Success Criteria

1. User Authentication System.
  The application includes a signup and login system that allows shop staff to securely access the system using a username and password. 
  (Prevents unauthorized access)
2. Bulk Order Management System.
  The application allows users to place bulk orders (minimum 10 drinks) by selecting a drink and specifying the quantity. (Simplifies the - 
  ordering process for customers ordering in large quantities)
3. Drink Customization Feature.
  Customers can customize their drinks by choosing sweetness levels and ice levels before adding them to their order. (Enhances customer 
  experience by allowing personalization)
4. Cart Storage and Display.
  The cart stores selected items and displays them in a structured list, showing drink name, customizations, quantity, and total price. 
  (Provides a clear overview of the order before checkout)
5. Visual Display of Total Drinks.
  The application displays the total number of drinks in a clear and visible section of the cart. (Provides an easy way for users to review 
  their order)
6. User-Friendly Interface.
  The application features a clean and easy-to-navigate design with a blue-themed, soft color palette. (Ensures a smooth and enjoyable user 
  experience) 

## Criteria B: Design

## ER Diagram:
<img width="655" alt="Screenshot 2025-03-12 at 8 06 05" src="https://github.com/user-attachments/assets/040225c0-3dfb-4e8f-ad02-92c33e935575" />

The ER diagram for Moonlight Bubbles includes four main tables: users, orders, order_items, and drinks. Primary key of each table is shown with an underline. A one-to-many relationship exists between users and orders, as each user can place multiple orders. The orders table links to order_items in a one-to-many relationship since each order can contain multiple drinks. The order_items table records drink details and connects to the drinks table in a many-to-one relationship, as multiple orders can include the same drink. This structure ensures efficient order tracking and management.

## UML Diagram:
<img width="556" alt="Screenshot 2025-03-12 at 8 10 03" src="https://github.com/user-attachments/assets/ef4e8ca2-3158-46e1-9d4f-139a6c498310" />

The UML diagram of the Moonlight Bubbles GUI application consists of four main classes: MoonlightBubblesApp, LoginScreen, SignupScreen, MenuScreen, and CartScreen. The MoonlightBubblesApp class inherits from App and serves as the main application controller. The screen classes (LoginScreen, SignupScreen, MenuScreen, and CartScreen) inherit from Screen and manage different user interfaces. The MenuScreen class handles drink customization and manages the global cart list, which is accessed by CartScreen to display order details. Each screen interacts with the Kivy .kv file for UI elements and receives user input dynamically.

## Wireframe:
<img width="637" alt="Screenshot 2025-03-12 at 8 11 34" src="https://github.com/user-attachments/assets/d26ff22b-83de-44e5-8cec-de0e7a2b3833" />

This is the wireframe of the GUI application. The screen flow follows the arrows in the figure.

## Records of Tasks:
| Task No | Planned Action              | Planned Outcome                                                                                                                                                  | Time estimate (min) | Target completion date | Criteria |
|---------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|----------|
| 1       | Consultation with my client | I interviewed my client and defined the problem that they had.                                                                                                 | 35                  | Feb 12                 | A        |
| 2       | Planning the solution       | Defined the problem more clearly and proposed a solution. Got it approved and made a success criteria.                                                         | 40                  | Feb 14                 | A        |
| 3       | Justification of tools      | I searched for the advantages and disadvantages of the tools I can use and chose the best ones for solving the defined problem.                                | 40                  | Feb 20                 | A        |
| 4       | ER diagram                  | I created an ER diagram to determine what data I needed to collect.                                                      | 30                  | Feb 22                 | B        |
| 5       | UML diagram                 | I created a UML diagram of a relational database to visualize the relationship of each table.                                                                  | 60                  | Feb 24                 | B        |
| 6       | Sketch                      | I created a sketch of a GUI application to offer it to my client.                                                                                              | 60                  | Feb 26                 | B        |
| 7       | Home Screen (SignUp/Login)  | I made a welcoming Home Screen with a signup button and a login button, allowing users to move between the pages by clicking.                                 | 60                  | Feb 28                 | C        |
| 8       | Sign Up Function            | I created a signup function that collects a username and password from a user and adds the user into the database.                                            | 40                  | Mar 1                  | C        |
| 9       | Login Function              | I created a login function that validates the username and password entered.                                                                                   | 60                  | Mar 1                  | C        |
| 10      | Menu Screen                 | I created a menu screen with 4 items from which the customer can choose.                                                                                       | 120                  | Mar 2                  | C        |
| 11      | Specific Details            | I created a function that asks the user specific details about their order, such as ice level, sweetness level, and quantity.                                | 120                 | Mar 2                  | C        |
| 12      | Go to Cart Button           | I created a "Go to Cart" button that leads the user from the menu page to the cart.                                                                           | 40                 | Mar 2                  | C        |
| 13      | Back to Menu Button         | I made a "Back to Menu" button that allows the user to return from the cart to the menu to choose more items if needed.                                      | 40                  | Mar 4                  | C        |
| 14      | Check Out Button            | I created a "Check Out" button that allows the customer to complete their order.                                                                             | 40                  | Mar 4                  | C        |
| 15      | Test Plan                   | I made a test plan table.                                                                                                                                     | 70                  | Mar 6                  | C        |
| 16      | Last Details                | I edited the KV file to improve the UI by changing colors, repositioning components, and adding images.                                                      | 40                  | Mar 9                  | C        |
| 17      | Final Product               | I made a video to introduce my development.                                                                                                                   | 10                  | Mar 10                 | C        |

## Test Plan:

| Test                          | Type            | Process (Input)                                                                                                      | Expected Output                                                                                     |
|--------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Login Functionality            | Functional Test | Enter a valid username and password in the Login screen. Click "Login" button.                                      | Successful login redirects to the Menu screen. If invalid credentials, a popup displays: "Invalid username or password." |
| Signup Functionality           | Functional Test | Enter a new username and password in the Signup screen. Click "Sign Up" button.                                     | If username is available, a popup displays: "Account created successfully!" and redirects to Login screen. If taken, a popup displays: "Username already exists." |
| Drink Customization and Cart Addition | Functional Test | In the Menu screen, select a drink (e.g., Classic Milk Tea). Choose sweetness, ice level, and quantity. Click "Add to Cart." | The selected drink with customization options is added to the cart. A success popup shows: "Added to cart!" |
| Quantity Validation            | Boundary Test  | In the Menu screen, select a drink and set quantity to 0 or an invalid value. Click "Add to Cart."                   | A popup shows: "Please enter a valid quantity." |
| Cart Screen Display            | Functional Test | Navigate to the Cart screen after adding items to the cart.                                                          | The Cart screen displays the added items with details: drink name, sweetness, ice level, quantity, and price. The total price is calculated correctly. |
| Back to Menu Button Functionality | Functional Test | In the Cart screen, click "Back to Menu."                                                                          | The app redirects to the Menu screen without saving the cart. |
| Checkout Button Functionality  | Functional Test | In the Cart screen, click the "Checkout" button with less than 10 items in the cart.                                 | A popup shows: "Minimum 10 drinks required to checkout." |
| Successful Checkout            | Functional Test | In the Cart screen, add 10 or more items to the cart. Click the "Checkout" button.                                   | The app closes. |
| UI Element Display             | UI/UX Test     | Navigate through the app to ensure that all UI elements (e.g., buttons, labels, input fields) are properly displayed. | All UI elements are visible, appropriately sized, and interactive on different screen sizes. |
| Database Operations (Signup/Login) | Database Test | Verify that user data is correctly added and retrieved from the SQLite database during signup and login.             | When signing up, the new user data is stored in the database. During login, credentials are validated against the database. |
| Menu Layout and Drink Buttons  | UI/UX Test     | Verify that all drink buttons in the Menu screen are visible and properly positioned.                                | Drink buttons are displayed with the appropriate images and the grid layout is responsive. |

## Criteria A: Developement

**Success Criterion 1: 1. User Authentication System. The application should allow users to securely access the system using a username and password.**

**Code Implementation: The authentication system typically consists of user login and signup mechanisms that ensure only authorized users can access the system.**

**Example Code:
File: bubble_tea.py**

```.C++
def init_db():
   conn = sqlite3.connect('moonlight_bubbles.db')
   cursor = conn.cursor()
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL
       )
   ''')
   conn.commit()
   conn.close()


init_db()


cart = []


class LoginScreen(Screen):
   def login(self):
       username = self.ids.username.text
       password = self.ids.password.text


       conn = sqlite3.connect('moonlight_bubbles.db')
       cursor = conn.cursor()
       cursor.execute('SELECT * FROM users WHERE username=?', (username,))
       user = cursor.fetchone()
       conn.close()


       if user and self.check_password(password, user[2]):
           self.manager.current = 'menu'
       else:
           self.show_popup('Error', 'Invalid username or password.')


   def check_password(self, input_password, stored_password):
       return hashlib.sha256(input_password.encode()).hexdigest() == stored_password


   def show_popup(self, title, message):
       popup = Popup(title=title, size_hint=(0.8, 0.4))
       popup.content = Label(text=message)
       popup.open()


class SignupScreen(Screen):
   def signup(self):
       username = self.ids.username.text
       password = self.ids.password.text


       hashed_password = hashlib.sha256(password.encode()).hexdigest()


       conn = sqlite3.connect('moonlight_bubbles.db')
       cursor = conn.cursor()
       try:
           cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
           conn.commit()
           self.show_popup('Success', 'Account created successfully!')
           self.manager.current = 'login'
       except sqlite3.IntegrityError:
           self.show_popup('Error', 'Username already exists.')
       finally:
           conn.close()


   def show_popup(self, title, message):
       popup = Popup(title=title, size_hint=(0.8, 0.4))
       popup.content = Label(text=message)
       popup.open()

```

**Success Criterion 2: Bulk Order Management System. The application allows users to place bulk orders by selecting a drink and specifying the quantity (minimum 10 drinks).**

**Code Implementation: To implement bulk ordering, I need to validate the quantity input and allow the customer to specify the drink type and the number of drinks to order. If the quantity is below the minimum, the system should reject the order and prompt the user.**

**Example Code:
File: bubble_tea.py**

```.C++
Example Code:
File: bubble_tea.py
def display_cart(self):
   self.layout.clear_widgets()


   min_drinks_label = Label(text="Minimum 10 drinks required", font_size=22, color=(1, 0, 0, 1), size_hint_y=None, height=40)
   self.layout.add_widget(min_drinks_label)

```

**Success Criterion 3: Drink Customization Feature. Success Criterion: Customers can customize their drinks by choosing sweetness levels and ice levels before adding them to the order.**

**Code Implementation: Drink customization involves allowing the customer to select various preferences (like sweetness or ice level) before the item is added to the order. The code needs to capture these preferences and store them with the drink in the cart.**

**Example Code:
File: bubble_tea.py**

```.C++
class MenuScreen(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.drink_name = None


   def show_drink_options(self, drink_name):
       self.drink_name = drink_name
       self.popup = Popup(title=f"Customize {drink_name}", size_hint=(0.8, 0.6))
       content = GridLayout(rows=5, spacing=10, padding=10)


       self.sweetness = Spinner(text='Sweetness Level', values=('0%', '25%', '50%', '75%', '100%'))
       self.ice = Spinner(text='Ice Level', values=('0%', '25%', '50%', '75%', '100%'))
       self.quantity = TextInput(hint_text='Quantity', input_type='number')
       price_label = Label(text="Price: 600¥", size_hint_y=None, height=30)
       add_to_cart_btn = Button(text='Add to Cart', size_hint_y=None, height=50)
       add_to_cart_btn.bind(on_press=self.add_to_cart)

```

**Success Criterion 4: Cart Storage and Display. The cart should store selected items and display them in a structured list, showing drink name, customizations, quantity, and total price.**

**Code Implementation: My cart management system should be capable of storing items with all relevant details like the drink name, customization (sweetness, ice level), quantity, and the total price for each item. The cart should then be displayed in a structured format for the user to review.**

**Example Code:
File: bubble_tea.py**

```.C++
class CartScreen(Screen):
   def on_enter(self):
       self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
       self.add_widget(self.layout)


       self.display_cart()


   def display_cart(self):
       self.layout.clear_widgets()


       min_drinks_label = Label(text="Minimum 10 drinks required", font_size=22, color=(1, 0, 0, 1), size_hint_y=None, height=40)
       self.layout.add_widget(min_drinks_label)


       total_price = 0


       cart_item_data = []
       for item in cart:
           cart_item_text = f"{item['drink']}  |  Sweetness: {item['sweetness']}  |  Ice: {item['ice']}  |  Qty: {item['quantity']}  |  Price: {item['price']}¥"
           cart_item_data.append({'text': cart_item_text, 'font_size': 18})
           total_price += item['price']


       self.ids.cart_items.data = cart_item_data


       final_price_label = Label(text=f"Final Price: {total_price}¥", font_size=24, bold=True, color=(0, 0, 0, 1))
       self.layout.add_widget(final_price_label)


       checkout_btn = Button(text='Checkout', size_hint_y=None, height=50)
       checkout_btn.bind(on_press=self.checkout)
       self.layout.add_widget(checkout_btn)


       back_to_menu_btn = Button(text='Back to Menu', size_hint_y=None, height=50)
       back_to_menu_btn.bind(on_press=self.back_to_menu)
       self.layout.add_widget(back_to_menu_btn)


   def checkout(self, instance):
       if len(cart) >= 10:
           self.show_popup('Order Placed', 'Thank you for your order!')
           cart.clear()
           self.manager.current = 'menu'
       else:
           self.show_popup('Error', 'Minimum 10 drinks required to checkout.')


   def back_to_menu(self, instance):
       self.manager.current = 'menu'


   def show_popup(self, title, message):
       popup = Popup(title=title, size_hint=(0.8, 0.4))
       popup.content = Label(text=message)
       popup.open()

```
**Success Criterion 5: Visual Display of Total Drinks. The application should display the total number of drinks in a clear and visible section of the cart.**

**Code Implementation: The application needs to provide an easy way to track how many drinks are in the cart. This requires a function that sums up the quantities of all items in the cart.**

**Example Code:
File: bubble_tea.py**

```.C++
total_price = 0


cart_item_data = []
for item in cart:
   cart_item_text = f"{item['drink']}  |  Sweetness: {item['sweetness']}  |  Ice: {item['ice']}  |  Qty: {item['quantity']}  |  Price: {item['price']}¥"
   cart_item_data.append({'text': cart_item_text, 'font_size': 18})
   total_price += item['price']


self.ids.cart_items.data = cart_item_data


final_price_label = Label(text=f"Final Price: {total_price}¥", font_size=24, bold=True, color=(0, 0, 0, 1))
self.layout.add_widget(final_price_label)

```

**Success Criterion 6: User-Friendly Interface. Success Criterion: The application features are clean and easy-to-navigate design with a blue-themed, soft color palette.**

**Code Implementation: I applied a user-friendly design to ensure a smooth and visually appealing experience. A blue-themed color palette with clear visual elements will help users navigate the app effortlessly.**

**Example Code:
File: bubble_tea.py**

```.C++

<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgb: 1, 1, 1  # White background
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Moonlight Bubbles Login'
            font_size: 45
            color: 0.117, 0.565, 1, 1  # Black text
            size_hint_y: None
            height: 50

        TextInput:
            id: username
            hint_text: 'Username'
            multiline: False
            background_color: 0, 0, 0, 0  # Transparent background
            foreground_color: 0, 0, 0, 1  # Black text
            size_hint_y: None
            height: 40
            canvas.after:
                Color:
                    rgba: input_line_color
                Line:
                    points: self.x, self.y, self.x + self.width, self.y
                    width: 1

        TextInput:
            id: password
            hint_text: 'Password'
            password: True
            multiline: False
            background_color: 0, 0, 0, 0  # Transparent background
            foreground_color: 0, 0, 0, 1  # Black text
            size_hint_y: None
            height: 40
            canvas.after:
                Color:
                    rgba: input_line_color
                Line:
                    points: self.x, self.y, self.x + self.width, self.y
                    width: 1

        Button:
            text: 'Login'
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1  # Light grey background
            size_hint_y: None
            height: 50
            on_press: root.login()

        Button:
            text: 'Sign Up'
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1  # Light grey background
            size_hint_y: None
            height: 50
            on_press: root.manager.current = 'signup'

<SignupScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgb: 1, 1, 1  # White background
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Moonlight Bubbles Sign Up'
            font_size: 28
            color: 0, 0, 0, 1  # Black text
            size_hint_y: None
            height: 50

        TextInput:
            id: username
            hint_text: 'Username'
            multiline: False
            background_color: 0, 0, 0, 0  # Transparent background
            foreground_color: 0, 0, 0, 1  # Black text
            size_hint_y: None
            height: 40
            canvas.after:
                Color:
                    rgba: input_line_color
                Line:
                    points: self.x, self.y, self.x + self.width, self.y
                    width: 1

        TextInput:
            id: password
            hint_text: 'Password'
            password: True
            multiline: False
            background_color: 0, 0, 0, 0  # Transparent background
            foreground_color: 0, 0, 0, 1  # Black text
            size_hint_y: None
            height: 40
            canvas.after:
                Color:
                    rgba: input_line_color
                Line:
                    points: self.x, self.y, self.x + self.width, self.y
                    width: 1

        Button:
            text: 'Sign Up'
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1  # Light grey background
            size_hint_y: None
            height: 50
            on_press: root.signup()

        Button:
            text: 'Back to Login'
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1  # Light grey background
            size_hint_y: None
            height: 50
            on_press: root.manager.current = 'login'

<MenuScreen>:
    GridLayout:
        cols: 1  # One column for the overall structure
        rows: 3  # 3 rows in total (2 for the drink images, 1 for the Go to Cart button)
        spacing: 10  # Space between buttons
        padding: 10  # Padding around the grid
        size_hint: 1, 1  # Fill the entire screen
        canvas.before:
            Color:
                rgb: 1, 1, 1  # White background
            Rectangle:
                pos: self.pos
                size: self.size


        # Grid for drink images (2 rows, 2 columns)
        GridLayout:
            cols: 2  # 2 columns for the drink images
            rows: 2  # 2 rows for the drink images
            size_hint: 1, None
            height: self.parent.height * 0.94  # Use 70% of the height for the drink images
            padding: 10
            spacing: 10

            # Classic Milk Tea Button
            Button:
                background_normal: ''
                background_color: (0.529, 0.808, 0.980, 1)
                on_press: root.show_drink_options('Classic Milk Tea')
                size_hint: 1, 1  # Fill the grid cell
                Image:
                    source: 'classic_milk_tea1.jpg'
                    allow_stretch: True
                    keep_ratio: False
                    size_hint: 1, 1
                    pos: self.parent.pos
                    size: self.parent.size

            # Matcha Milk Tea Button
            Button:
                background_normal: ''
                background_color: (0.529, 0.808, 0.980, 1)
                on_press: root.show_drink_options('Matcha Milk Tea')
                size_hint: 1, 1  # Fill the grid cell
                Image:
                    source: 'matcha_milk_tea.png'
                    allow_stretch: True
                    keep_ratio: False
                    size_hint: 1, 1
                    pos: self.parent.pos
                    size: self.parent.size

            # Mango Green Tea Button
            Button:
                background_normal: ''
                background_color: (0.529, 0.808, 0.980, 1)
                on_press: root.show_drink_options('Mango Green Tea')
                size_hint: 1, 1  # Fill the grid cell
                Image:
                    source: 'mango_green_tea.png'
                    allow_stretch: True
                    keep_ratio: False
                    size_hint: 1, 1
                    pos: self.parent.pos
                    size: self.parent.size

            # Lemon Black Tea Button
            Button:
                background_normal: ''
                background_color: (0.529, 0.808, 0.980, 1)
                on_press: root.show_drink_options('Lemon Black Tea')
                size_hint: 1, 1  # Fill the grid cell
                Image:
                    source: 'lemon_black_tea.png'
                    allow_stretch: True
                    keep_ratio: False
                    size_hint: 1, 1
                    pos: self.parent.pos
                    size: self.parent.size

        # Go to Cart Button (at the very bottom)
        Button:
            text: "Go to Cart"
            size_hint_y: None
            size_hint_x: 1  # Full width
            height: 50
            on_press: root.go_to_cart()
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1


<CartScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        background_color: 0.529, 0.808, 0.980, 1
        canvas.before:
            Color:
                rgb: 1, 1, 1  # White background
            Rectangle:
                pos: self.pos
                size: self.size

        # Minimum drinks required label
        Label:
            text: "Minimum 10 drinks required"
            font_size: 22
            color: (0, 0, 0, 1)
            size_hint_y: None
            height: 40

        # Scrollable area for cart items
        ScrollView:
            RecycleView:
                id: cart_items
                viewclass: 'Label'  # Make sure items are displayed as Labels
                RecycleBoxLayout:
                    default_size: None, 40
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'

        # Final Price Label
        Label:
            id: final_price
            text: "Final Price: 0¥"
            font_size: 24
            bold: True
            color: (0, 0, 0, 1)
            size_hint_y: None
            height: 50

        # Checkout Button
        Button:
            text: 'Checkout'
            size_hint_y: None
            height: 50
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1
            on_press: root.checkout()

        # Go Back to Menu Button
        Button:
            text: 'Back to Menu'
            size_hint_y: None
            height: 50
            background_normal: ''  # Remove default button background
            background_color: 0.529, 0.808, 0.980, 1
            on_press: root.back_to_menu()


```
