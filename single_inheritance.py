class single_inheritance:
    def __init__(self,name,city,mobile_no):
        self.name =name
        self.city =city
        self.mobile_no=mobile_no
    def display_company_details(self):
        print("Company Name:",self.name)    
        print("City:",self.city)
        print("Mobile No:",self.mobile_no) 
class Employee(single_inheritance):
    def __init__(sel,emp_name,desination,salary,company_name,city,mobile_no):
        super() __init__(company_name,city,mobile_no)
        self.emp_name=emp_name
        self.desination=desination
        self.salary=salary
    def display_details(self):
        self.display_company_details()
        print("Employee Name:",self.emp_name)
        print("Designation:",self.designation)
        print("Salary:",self.salary)
emp1=Employee("isha pipaliya","Manager","70000"."abc","Rajkot",3243758532)
emp1.display_details()  