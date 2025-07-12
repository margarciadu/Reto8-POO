import random

# Base class for menu items
class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_price(self, quantity: int) -> float:
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size_ml: int):
        super().__init__(name, price)
        self.size_ml = size_ml

    def total_price(self, quantity: int) -> float:
        tax = 0.1
        return super().total_price(quantity) * (1 + tax)

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_fried: bool):
        super().__init__(name, price)
        self.is_fried = is_fried

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, origin: str):
        super().__init__(name, price)
        self.origin = origin

class OrderIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item

# Order class
class Order:
    def __init__(self):
        self.order_number = random.randint(1000, 9999)
        self.items = []

    def add(self, item: "MenuItem", quantity: int):
        self.items.append((item, quantity))

    def total(self) -> float:
        return sum(item.total_price(quantity) for item, quantity in self.items)

    def apply_discount(self) -> float:
        subtotal = self.total()
        discount = 0
        if subtotal > 100000:
            discount = subtotal * 0.15
        elif subtotal > 50000:
            discount = subtotal * 0.10
        elif subtotal > 30000:
            discount = subtotal * 0.05
        return subtotal - discount
    
    def summary(self) -> str:
        print(f"\nPedido #{self.order_number}")
        print("Resumen del pedido:")
        for item, quantity in self.items:
            print(f" - {item.name} x{quantity} = ${item.total_price(quantity):,.2f}")
        print(f"Subtotal: ${self.total():,.2f}")
        print(f"Total con descuento: ${self.apply_discount():,.2f}")

    def __iter__(self):
        return OrderIterator(self.items)

# Menu items
coca_cola = Beverage("CocaCola", 5000, 350)
lemonade = Beverage("Limonada", 4000, 300)
beer = Beverage("Cerveza", 7000, 330)
water = Beverage("Agua", 2000, 500)

stuffed_arepa = Appetizer("Arepa Rellena", 6000, True)
empanada = Appetizer("Empanada", 2500, True)
patacon = Appetizer("Patacón", 3000, True)
nachos = Appetizer("Nachos", 5500, False)

spaguetti = MainCourse("Spaguetti", 18000, "Italiana")
grilled_beef = MainCourse("Carne Asada", 25000, "Colombiana")
pork_loin = MainCourse("Lomo de Cerdo", 23000, "Internacional")
hamburger = MainCourse("Hamburguesa", 20000, "Americana")
bandeja_paisa = MainCourse("Bandeja Paisa", 30000, "Colombiana")

# Menu dictionary by category
menu = {
    "Bebidas": [coca_cola, lemonade, beer, water],
    "Aperitivos": [stuffed_arepa, empanada, patacon, nachos],
    "Platos Fuertes": [spaguetti, grilled_beef, pork_loin, hamburger, bandeja_paisa]
}

# Display menu with continuous numbering per category
def display_menu(menu_dict):
    print("\n-- MENÚ --")
    full_menu = []
    counter = 1
    for category, items in menu_dict.items():
        print(f"\n{category.upper()}:")
        for item in items:
            item_type = type(item).__name__
            extra = ""
            if isinstance(item, Beverage):
                extra = f"({item.size_ml}ml)"
            elif isinstance(item, Appetizer):
                extra = "(Frito)" if item.is_fried else "(No frito)"
            elif isinstance(item, MainCourse):
                extra = f"(Origen: {item.origin})"
            print(f"{counter}. {item.name} - ${item.price:.2f} {extra} [{item_type}]")
            full_menu.append(item)
            counter += 1
    return full_menu

# Get product by index
def get_product_by_index(menu_list, index: int) -> MenuItem:
    if 1 <= index <= len(menu_list):
        return menu_list[index - 1]
    else:
        return None

# Main program
order = Order()

while True:
    menu_list = display_menu(menu)

    try:
        selection = int(input("\nSeleccione un producto por número (0 para finalizar): "))
        if selection == 0:
            break
        product = get_product_by_index(menu_list, selection)
        if product:
            quantity = int(input(f"Ingrese la cantidad de {product.name}: "))
            order.add(product, quantity)
            print(f"{quantity} x {product.name} añadido(s) al pedido.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

# Show order summary
order.summary()

# Iterate through the order
print("\nRecorriendo los ítems del pedido:")
for item, quantity in order:
    print(f"{quantity} x {item.name} ({type(item).__name__}) - Total: ${item.total_price(quantity):,.2f}")

        