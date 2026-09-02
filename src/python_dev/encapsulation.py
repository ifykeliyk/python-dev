class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.__salary = salary  # Private attribute

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def get_salary(self):
        return self.__salary  # Public method to access private attribute

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary  # Public method to modify private attribute
        else:
            raise ValueError("Salary must be positive")


emp = Employee("John", "Doe", 50000)
emp.set_salary(60000)
emp.full_name = "Jane Smith"
print(emp.full_name)
print(emp.get_salary())
