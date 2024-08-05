class employee_class:
    def __init__(self,name,doj,designation,salary):
        self.name=name
        self.doj=doj
        self.designation=designation
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("date of join:",self.doj)
        print("designation:",self.designation)
        print("salary:",self.salary)
        print("--------")
emp1=employee_class('isha','20 feb 2024','senior employee',50000)
emp1.display()