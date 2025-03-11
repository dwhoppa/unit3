import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

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
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.manager.current = 'menu'
        else:
            self.show_popup('Error', 'Invalid username or password.')

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message)
        popup.open()

class SignupScreen(Screen):
    def signup(self):
        username = self.ids.username.text
        password = self.ids.password.text

        conn = sqlite3.connect('moonlight_bubbles.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
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

class MenuScreen(Screen):
    cart = []

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

        content.add_widget(self.sweetness)
        content.add_widget(self.ice)
        content.add_widget(self.quantity)
        content.add_widget(price_label)
        content.add_widget(add_to_cart_btn)
        self.popup.content = content
        self.popup.open()

    def add_to_cart(self, instance):
        quantity = int(self.quantity.text) if self.quantity.text.isdigit() else 0
        if quantity <= 0:
            self.show_popup('Error', 'Please enter a valid quantity.')
            return

        price = 600 * quantity
        self.cart.append({
            'drink': self.drink_name,
            'sweetness': self.sweetness.text,
            'ice': self.ice.text,
            'quantity': quantity,
            'price': price
        })
        self.popup.dismiss()
        self.show_popup('Success', 'Added to cart!')

    def go_to_cart(self):
        self.manager.current = 'cart'

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message)
        popup.open()

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
        for item in MenuScreen.cart:
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
        if len(MenuScreen.cart) >= 10:
            self.show_popup('Order Placed', 'Thank you for your order!')
            MenuScreen.cart.clear()
            self.manager.current = 'menu'
        else:
            self.show_popup('Error', 'Minimum 10 drinks required to checkout.')

    def back_to_menu(self, instance):
        self.manager.current = 'menu'

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message)
        popup.open()

class MoonlightBubblesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CartScreen(name='cart'))
        return sm

if __name__ == '__main__':
    MoonlightBubblesApp().run()
