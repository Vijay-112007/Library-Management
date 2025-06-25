class Book():
    def __init__(self, name, author, price, id, charge):
        self.name = name
        self.author = author
        self.__price = price
        self.id = id
        self.charge = charge

    def get_price(self):
        return self.__price