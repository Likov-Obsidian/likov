class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зп не может быть отрицательной")
        self._salary = value
emp = Employee("John", 50000)
try:
    emp.salary = -100
except ValueError as e:
    print(f"Ошибка: {e}")
emp.salary = 60000
print(emp.salary)