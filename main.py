class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} so'm"

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_menu(self):
        print("\n--- Menyu ---")
        for dish in self.dishes:
            print(dish)

class Order:
    s = 1
    def __init__(self, customer, selected_dishes):
        self.order_id = Order.s
        self.customer = customer
        self.selected_dishes = selected_dishes
        Order.s += 1

    def total_price(self):
        """Umumiy summani hisoblash."""
        return sum(dish.price for dish in self.selected_dishes)

    def show_order(self):
        print(f"\n--- Buyurtma ---")
        print(f"Buyurtma ID: {self.order_id}")
        print(f"Mijoz: {self.customer.name} - {self.customer.phone}")
        print("Tanlangan ovqatlar:")
        for dish in self.selected_dishes:
            print(dish)
        total_price = self.total_price()
        print(f"Umumiy summa: {total_price} so'm")

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class DeliveryPerson:
    def __init__(self, name, vehicle_number):
        self.name = name
        self.vehicle_number = vehicle_number

    def deliver_order(self, order):
        print(f"Buyurtma {order.order_id} mijozga yetkazildi.")

class DeliverySystem:
    def __init__(self):
        self.menu = Menu()

    def create_menu(self):
        dish1 = Dish("Pizza", 100000)
        dish2 = Dish("Burger", 35000)
        dish3 = Dish("Salad", 15000)
        self.menu.add_dish(dish1)
        self.menu.add_dish(dish2)
        self.menu.add_dish(dish3)

    def buyurtma_qabul_qilish(self, customer, selected_dishes):
        order = Order(customer, selected_dishes)
        return order

    def buyurtmani_yetqazish(self, order, delivery_person):
        delivery_person.deliver_order(order)

system = DeliverySystem()
system.create_menu()

system.menu.show_menu()

customer_name = input("\nMijoz ismini kiriting: ")
customer_phone = input("Mijoz telefon raqamini kiriting: ")
customer = Customer(customer_name, customer_phone)

selected_dishes = []
while True:
    a = input("\nOvqat raqamini tanlang (chiqish uchun 'q' ni bosing): ")
    if a == 'q':
        break
    try:
        a = int(a) - 1
        if 0 <= a < len(system.menu.dishes):
            selected_dishes.append(system.menu.dishes[a])
            print(f"{system.menu.dishes[a]} qo'shildi.")
        else:
            print("Noto'g'ri raqam.")
    except ValueError:
        print("Noto'g'ri kiritish.")

if selected_dishes:
    order = system.buyurtma_qabul_qilish(customer, selected_dishes)
    order.show_order()

    delivery_person = DeliveryPerson("Hasan", "01A234BC")

    system.buyurtmani_yetqazish(order, delivery_person)
else:
    print("\nBuyurtma berilmadi.")


