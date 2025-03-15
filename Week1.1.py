class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        if product.product_id not in self.stock:
            self.stock[product.product_id] = {"product": product, "quantity": 0}
        self.stock[product.product_id]["quantity"] += quantity

    def is_available(self, product_id, quantity):
        return self.stock.get(product_id, {}).get("quantity", 0) >= quantity

    def deduct_stock(self, product_id, quantity):
        if self.is_available(product_id, quantity):
            self.stock[product_id]["quantity"] -= quantity
            return True
        return False

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Order:
    order_counter = 1  # Static counter for order IDs

    def __init__(self, customer, items):
        self.order_id = Order.order_counter
        Order.order_counter += 1  # Increment order ID for next order
        self.customer = customer
        self.items = items
        self.total = sum(product.price * quantity for product, quantity in items)
        self.paid = False
        self.payment_details = None

    def mark_paid(self, payment_details):
        self.paid = True
        self.payment_details = payment_details

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name} ({self.customer.email})")
        print("Items:")
        for product, quantity in self.items:
            print(f"  {quantity} x {product.name} (${product.price}) = ${product.price * quantity}")
        print(f"Total: ${self.total}")
        print(f"Status: {'Paid' if self.paid else 'Unpaid'}")
        if self.paid:
            print(f"Payment Details: {self.payment_details}")

class PaymentProcessor:
    def process_payment(self, order, payment_type, payment_details):
        if payment_type == "credit_card":
            card_number = payment_details.get("card_number")
            if not card_number:
                raise ValueError("Missing card number")
            print(f"Processing ${order.total} with credit card ending in {card_number[-4:]}")
        elif payment_type == "paypal":
            email = payment_details.get("email")
            if not email:
                raise ValueError("Missing PayPal email")
            print(f"Processing ${order.total} with PayPal account {email}")
        else:
            raise ValueError("Unknown payment type")
        order.mark_paid(payment_details)
        return True

class ECommerceSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.customers = {}
        self.orders = []
        self.payment_processor = PaymentProcessor()

    def add_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.inventory.add_product(product, 0)

    def add_inventory(self, product_id, quantity):
        if product_id not in self.inventory.stock:
            print("Product doesn't exist")
            return False
        self.inventory.stock[product_id]["quantity"] += quantity
        return True

    def add_customer(self, customer_id, name, email):
        self.customers[customer_id] = Customer(customer_id, name, email)

    def create_order(self, customer_id, product_quantities):
        if customer_id not in self.customers:
            print("Customer doesn't exist")
            return None
        items = []
        for product_id, quantity in product_quantities:
            if not self.inventory.is_available(product_id, quantity):
                print(f"Not enough inventory for product {product_id}")
                return None
            product = self.inventory.stock[product_id]["product"]
            items.append((product, quantity))
        for product, quantity in items:
            self.inventory.deduct_stock(product.product_id, quantity)
        order = Order(self.customers[customer_id], items)
        self.orders.append(order)
        return order

    def process_payment(self, order, payment_type, payment_details):
        return self.payment_processor.process_payment(order, payment_type, payment_details)

if __name__ == "__main__":
    system = ECommerceSystem()
    system.add_product(1, "Laptop", 1200)
    system.add_product(2, "Smartphone", 800)
    system.add_product(3, "Wireless Headphones", 200)
    system.add_inventory(1, 5)
    system.add_inventory(2, 10)
    system.add_inventory(3, 20)
    system.add_customer(101, "John Doe", "john@example.com")
    order = system.create_order(101, [(1, 1), (3, 2)])
    if order:
        system.process_payment(order, "credit_card", {"card_number": "4111111111111111"})
        order.print_order()
    another_order = system.create_order(101, [(2, 1)])
    if another_order:
        system.process_payment(another_order, "paypal", {"email": "john@example.com"})
        another_order.print_order()