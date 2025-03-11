
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

**Success Criterion: The application should allow users to securely access the system using a username and password.**

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
**Code Partial Overview: In the first line of the code, we must include the DHT.h library, in this case we will be using the Adafruit DHT Sensor Library. This library is essential for the program as it makes the arduino to identify the and send the commands to the DHT sensors connected to it. In the lines 3 and 4, we defined the pin the sensor is connected to and the type of sensor it is being used in this case scenario. The sensors being used for our project are the DHT11 type, and they are connected to pin 2. The pin and sensor can be seen in the fig.2 located in the Criteria B. On the line 7, the sensor's identity is created so later on the sensor can be called on other programs. Finally, on the line 8, the variable "startTime" is declared and assigned to the type Unsigned long, which permits the variable to store a large amount of non-negative integer values. The word static ensures that the variable retainsits value between function calls. This last line is used to store the timestamp of the data collect, to be exact the start of the collection.**

```.C++
void setup() {
  Serial.begin(9600);
  while (!Serial) delay(10); // Wait for Serial monitor to be ready
  // Serial.println("DHTxx start!");

  dht.begin();
  startTime = millis();
}
```

**Code Partial Overview: Next, in this section




