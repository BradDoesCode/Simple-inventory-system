# Simple inventory management script with a product and inventory class to allow
# users to add/remove products and calculate the total value of an inventory
from random import randint

"""Creates an empty list to store product objects."""
product_list = []


class Product:
    """class for products, each class has an id number, name and price"""
    def __init__(self, item_id=int, name=str, price=float) -> None:
        self.id = item_id
        self.name = name
        self.price = price

    @staticmethod
    def add_new() -> None:
        """adds a new product to product class, then appends onto inventory"""
        try:
            """tries to get the id of the last item in the list of products"""
            item_id = product_list[-1].id + 1
        except IndexError:
            """if list is empty"""
            item_id = 0
        finally:
            """asks the user for product name and price and adds it to product list and inventory"""
            item_name = input('Please enter item name: ')
            item_price = float(input('Please enter item price: '))
            product_list.append(Product(item_id, item_name, item_price))
            quantity = int(input(f'Enter quantity amount for item {product_list[item_id].name}: '))
            new_inventory.add_item(item_id, quantity)
            item_id += 1

    @staticmethod
    def display_all():
        for product in product_list:
            print('name: ' + product.name + ', Price: ' + str(product.price) + ", ID: " + str(product.id))


class Inventory:
    """inventory class that holds a list with each product id and its quantity"""
    def __init__(self) -> None:
        self.inventory = []

    def __str__(self) -> str:
        """returns each item id and its quantity"""
        items_in_inv = ""
        for item in self.inventory:
            items_in_inv += f'{product_list[item[0]].name}, quantity is {item[1]}\n'
        return items_in_inv

    def __getitem__(self, item_id=int) -> list:
        return self.inventory[item_id]

    def add_item(self, item_id=int, quantity=int) -> None:
        """add an item to the inventory"""
        try:
            """update the quantity amount if the item is already in inventory"""
            if item_id in self.inventory[item_id]:
                self.inventory.add_quantity(item_id, quantity)
        except IndexError:
            """else add new item with starting quantity"""
            self.inventory.append([item_id, quantity])

    def add_quantity(self, id_quantity=tuple) -> None:
        """updates the current stock amount with new amount"""
        self.inventory[id_quantity[0]][1] += id_quantity[1]

    def remove_quantity(self, id_quantity=tuple) -> None:
        """updates the current stock amount with new amount"""
        self.inventory[id_quantity[0]][1] -= id_quantity[1]

    def calculate_value(self) -> str:
        total_value = 0
        for item in self.inventory:
            item_id = item[0]
            quantity = item[1]
            value = product_list[item_id].price * quantity
            total_value += value
        return f'total_value: {total_value}'


# Functions


def generate_test_products() -> None:
    """generates products for testing purposes"""
    sample_names = ['bread', 'milk', 'chocolate', 'sweets', 'crisps', 'rice', 'pasta', 'cereal', 'tea', 'coffee']
    """try block checks if list is empty"""
    try:
        item_id = product_list[-1].id + 1
    except IndexError:
        item_id = 0
    finally:
        """creates products with random price"""
        for x in range(len(sample_names)):
            product_list.append(Product(item_id, sample_names[x], randint(0, 10)))
            new_inventory.add_item(item_id, randint(1, 10))
            item_id += 1


def ask_for_itemID():
    item_id = int(input('enter product ID'))
    quantity = int(input('enter quantity'))
    return item_id, quantity


if __name__ == '__main__':
    new_inventory = Inventory()
    while True:
        user_choice = str(input('''Enter your choice:
        1, add a new product.
        2, add more stock to a product.
        3, remove stock from a product
        4, view the inventory.
        5, display all products.
        6, Calculate value of inventory.
        7, generate random products.
        '''))
        match user_choice:
            case '1': Product.add_new()
            case '2': new_inventory.add_quantity(ask_for_itemID())
            case '3': new_inventory.remove_quantity(ask_for_itemID())
            case '4': print(new_inventory)
            case '5': Product.display_all()
            case '6': print(new_inventory.calculate_value())
            case '7': generate_test_products()
