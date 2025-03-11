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
| 1       | Consultation with my client | I interviewed my client and defined the problem that they had.                                                                                                 | 30                  | Feb 12                 | A        |
| 2       | Planning the solution       | Defined the problem more clearly and proposed a solution. Got it approved and made a success criteria.                                                         | 40                  | Feb 14                 | A        |
| 3       | Justification of tools      | I searched for the advantages and disadvantages of the tools I can use and chose the best ones for solving the defined problem.                                | 30                  | Feb 20                 | A        |
| 4       | ER diagram                  | I created an ER diagram to determine what data I needed to collect.                                                      | 30                  | Feb 22                 | B        |
| 5       | UML diagram                 | I created a UML diagram of a relational database to visualize the relationship of each table.                                                                  | 30                  | Feb 24                 | B        |
| 6       | Sketch                      | I created a sketch of a GUI application to offer it to my client.                                                                                              | 60                  | Feb 26                 | B        |
| 7       | Home Screen (SignUp/Login)  | I made a welcoming Home Screen with a signup button and a login button, allowing users to move between the pages by clicking.                                 | 20                  | Feb 28                 | C        |
| 8       | Sign Up Function            | I created a signup function that collects a username and password from a user and adds the user into the database.                                            | 40                  | Mar 1                  | C        |
| 9       | Login Function              | I created a login function that validates the username and password entered.                                                                                   | 30                  | Mar 1                  | C        |
| 10      | Menu Screen                 | I created a menu screen with 4 items from which the customer can choose.                                                                                       | 40                  | Mar 2                  | C        |
| 11      | Specific Details            | I created a function that asks the user specific details about their order, such as ice level, sweetness level, and quantity.                                | 120                 | Mar 2                  | C        |
| 12      | Go to Cart Button           | I created a "Go to Cart" button that leads the user from the menu page to the cart.                                                                           | 120                 | Mar 2                  | C        |
| 13      | Back to Menu Button         | I made a "Back to Menu" button that allows the user to return from the cart to the menu to choose more items if needed.                                      | 15                  | Mar 4                  | C        |
| 14      | Check Out Button            | I created a "Check Out" button that allows the customer to complete their order.                                                                             | 40                  | Mar 4                  | C        |
| 15      | Test Plan                   | I made a test plan table.                                                                                                                                     | 70                  | Mar 6                  | C        |
| 16      | Last Details                | I edited the KV file to improve the UI by changing colors, repositioning components, and adding images.                                                      | 40                  | Mar 9                  | C        |
| 17      | Final Product               | I made a video to introduce my development.                                                                                                                   | 40                  | Mar 10                 | C        |







