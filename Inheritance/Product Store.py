# Write a class Product that has three attributes: type name price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All
# methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
# additional
# classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
# identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other
# case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.product_store = []
        self.profit = 0

    def add(self, product, amount):
        try:
            if int(amount) > 0:
                self.product_store.append({"type": product.type, "name": product.name,
                                          "price": round(product.price * 1.3, 2), "amount": amount})
                print(f"Product added {product.name} {product.type} in quantity {amount} "
                      f"with price: {product.price}")
            else:
                print("No product")
        except ValueError:
            print("Quantity must be a number")

    def set_discount(self, identifier, percent, identifier_type="name"):
        for product in self.product_store:
            if identifier in product[identifier_type]:
                product["price"] *= (1 - percent / 100)
                product["price"] = round(product["price"], 2)
                print(f"Oferta: {product['name']} ({product['type']}), "
                      f" new price: {product['price']}. "
                      f"quantity: {product['amount']}.")
        try:
            if int(percent) < 0:
                print(f'Wrong number this  product will be without discount')
                percent = 0
        except ValueError:
            print("Write a number")

    def sell_product(self, product_name, amount):
        for product in self.product_store:
            if product['name'] == product_name:
                if product['amount'] > amount:
                    product['amount'] -= amount
                    print(f"You selled: {product['name']} ({product['type']}) in quantity: {amount}.")
                    self.profit += round(amount * product['price'], 2)
                    print(f"Profit: {round(amount * product['price'], 2)}.")
                elif product['amount'] > 0:
                    print(f"Product {product['name']} ({product['type']}) are less {product['amount']}, "
                          f"than {amount}. Selling what's left")
                    self.profit += round(product['amount'] * product['price'], 2)
                    print(f"Profit with this action: {round(product['amount'] * product['price'], 2)}.")
                    product['amount'] = 0
                else:
                    print(
                        f"Product {product['name']} {product['type']} not left")
        try:
            if int(amount) < 0:
                print("wrong number")
        except ValueError:
            print("Write a number")

    def get_income(self):
        return self.profit

    def get_all_products(self):
        return self.product_store

    def get_product_info(self, product_name):
        product_info = []
        for product in self.product_store:
            if product['name'] == product_name:
                product_info.append((product['name'], product['amount']))
        return product_info


product_1 = Product('Sport', 'Football T-Shirt', 100)
product_2 = Product('Food', 'Ramen', 1)

store = ProductStore()

store.add(product_1, 10)
store.add(product_2, 300)
store.set_discount('Food', 20, 'type')
store.sell_product('Ramen', 10)
store.sell_product('Ramen', 300)
store.sell_product('Ramen', 20)
print(f'Total profit — {store.get_income()}')
print(f'All products: {store.get_all_products()}.')
print(f"Information about product: {store.get_product_info('Ramen')}")