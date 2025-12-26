class LoggableMixin:
    def log(self, msg):
        print(f"[INFO] {self.__class__.__name__}: {msg}")
class Employee(LoggableMixin):
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary
class Product(LoggableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
emp = Employee("Manager", 50000)
emp.log("Сотрудник создан")
prod = Product("Телефон", 30000)