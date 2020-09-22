class employee:
    def __init__(self, name, sal):
        #public accessmodifier
        self.name=name
        self.salary=sal

e1 = employee("rohit",2323)
print(e1.salary)
print(e1.name)

class employee1:
    def __init__(self, name, sal):
        self._name=name  # protected attribute
        self._salary=sal # protected attribute
e2 = employee1("Rohit",43432432)
print(e2._name)
print(e2._salary)

class employee2:
    def __init__(self, name, sal):
        self.__name=name  # private attribute
        self.__salary=sal # private attribute

e3 = employee2("rr",333)
print(e3.employee2__name)
print(e3.employee2__salary)
