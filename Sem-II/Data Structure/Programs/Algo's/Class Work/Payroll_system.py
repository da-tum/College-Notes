# Payroll system using OOP in Python
# Problem Statement:
'''
Employee Payroll Management System
Design and implement an Employee Payroll Management System using Object Oriented Programming (OOPS) concepts.
System Requirements:
Create an abstract class Employee that contains:
Employee ID
Employee Name
Basic Salary
An abstract method calculate_salary().
Implement encapsulation by keeping data members private/protected and providing appropriate getter and setter methods.
Create two derived classes using inheritance:
PermanentEmployee
ContractEmployee
Override the calculate_salary() method in both derived classes to demonstrate polymorphism:
Permanent employee salary includes basic salary + allowances.
Contract employee salary is calculated on hourly basis.

Use runtime polymorphism by creating base class references to derived class objects.
Create a separate class PayrollSystem that:
Stores employee objects.
Displays employee details and calculated salary.
Demonstrate object creation, method calling, and data hiding in the main program.

class Employee:
    def __init__ (self,Employee_ID, Employee_Name, Basic_Salary):
        self.__Employee_ID = Employee_ID
        self.__Employee_Name = Employee_Name
        self.__Basic_Salary = Basic_Salary
        
    def calculate_salary(self):
        pass

class PermanenetEmployee(Employee):
    def __init__(self,Employee_ID,Employee_Name,Basic_Salary,Allowances):
        super().__init__(self,Employee_ID, Employee_Name, Basic_Salary)
        self.Allowances = Allowances
        
    def calculate_salary(self):
        pass

    
class ContractEmployee(Employee):
    def __init__(self, Employee_ID,Employee_Name,Basic_Salary,Hours_Worked,Hourly_Rate):
        super().__init__(self,Employee_ID, Employee_Name, Basic_Salary)
        self.Hours_Worked = Hours_Worked
        self.Hourly_Rate = Hourly_Rate
    
    def calculate_salary(self):
        pass
        
class PayrollSystem(Employee):
    def __init__(self,Employee_ID,Employee_Name):
        super().__init__(Employee_ID,Employee_Name)
'''

# ---------------------------------------------------------
# STEP 1: Import ABC and abstractmethod for ABSTRACTION
# ABC = Abstract Base Class
# abstractmethod = decorator used to define abstract methods
# ---------------------------------------------------------
from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 2: Create an ABSTRACT CLASS named Employee
# This class cannot be instantiated directly
# It acts as a blueprint for child classes
# ---------------------------------------------------------
class Employee(ABC):

    # -----------------------------------------------------
    # Constructor method
    # __init__ is automatically called when object is created
    # self represents the current object
    # -----------------------------------------------------
    def __init__(self, emp_id, name, basic_salary):
        self._emp_id = emp_id          # Protected variable (Encapsulation)
        self._name = name              # Protected variable
        self._basic_salary = basic_salary

    # -----------------------------------------------------
    # Abstract method
    # Child classes MUST implement this method
    # Demonstrates ABSTRACTION
    # -----------------------------------------------------
    @abstractmethod
    def calculate_salary(self):
        pass    # pass means "no implementation here"


# ---------------------------------------------------------
# STEP 3: Create PermanentEmployee class
# Inherits Employee class (INHERITANCE)
# ---------------------------------------------------------
class PermanentEmployee(Employee):

    # -----------------------------------------------------
    # calculate_salary method
    # Overrides abstract method (POLYMORPHISM)
    # -----------------------------------------------------
    def calculate_salary(self):
        hra = self._basic_salary * 0.20     # HRA = 20% of basic salary
        da = self._basic_salary * 0.10      # DA = 10% of basic salary
        total_salary = self._basic_salary + hra + da
        return total_salary


# ---------------------------------------------------------
# STEP 4: Create ContractEmployee class
# Also inherits Employee class
# ---------------------------------------------------------
class ContractEmployee(Employee):

    # -----------------------------------------------------
    # Constructor with extra parameter hours_worked
    # super() calls parent class constructor
    # -----------------------------------------------------
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, hourly_rate)
        self._hours_worked = hours_worked   # Protected variable

    # -----------------------------------------------------
    # Overridden method for salary calculation
    # Demonstrates RUNTIME POLYMORPHISM
    # -----------------------------------------------------
    def calculate_salary(self):
        return self._basic_salary * self._hours_worked


# ---------------------------------------------------------
# STEP 5: PayrollSystem class
# Handles multiple employees
# ---------------------------------------------------------
class PayrollSystem:

    # -----------------------------------------------------
    # Constructor initializes empty employee list
    # -----------------------------------------------------
    def __init__(self):
        self.employee_list = []   # List to store employee objects

    # -----------------------------------------------------
    # Method to add employee object to list
    # -----------------------------------------------------
    def add_employee(self, employee):
        self.employee_list.append(employee)

    # -----------------------------------------------------
    # Method to display salary details
    # -----------------------------------------------------
    def show_payroll(self):
        for emp in self.employee_list:
            print("Employee ID   :", emp._emp_id)
            print("Employee Name :", emp._name)
            print("Salary        :", emp.calculate_salary())
            print("-------------------------------")


# ---------------------------------------------------------
# STEP 6: MAIN PROGRAM
# Object creation and method calling
# ---------------------------------------------------------

# Create PayrollSystem object
payroll = PayrollSystem()

# Create PermanentEmployee object
emp1 = PermanentEmployee(101, "Rahul", 30000)

# Create ContractEmployee object
emp2 = ContractEmployee(102, "Amit", 500, 40)

# Add employees to payroll system
payroll.add_employee(emp1)
payroll.add_employee(emp2)

# Display payroll details
payroll.show_payroll()