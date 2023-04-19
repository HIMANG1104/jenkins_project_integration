import csv


class Employee:
    def __init__(self, name, id, hourly_rate):
        self.name = name
        self.id = id
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours(self, hours):
        self.hours_worked += hours

    def calculate_salary(self):
        overtime_rate = 1.5 * self.hourly_rate
        if self.hours_worked <= 40:
            salary = self.hours_worked * self.hourly_rate
        else:
            salary = (40 * self.hourly_rate) + ((self.hours_worked - 40) * overtime_rate)
        return salary


class Payroll:
    def __init__(self):
        self.employees = []

    def load_data(self):
        with open('employee_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, id, hourly_rate = row
                self.employees.append(Employee(name, id, float(hourly_rate)))

    def add_employee(self):
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        hourly_rate = float(input("Enter hourly rate: "))
        self.employees.append(Employee(name, id, hourly_rate))

    def add_hours(self):
        id = input("Enter employee ID: ")
        hours = float(input("Enter number of hours worked: "))
        for employee in self.employees:
            if employee.id == id:
                employee.add_hours(hours)
                break
        else:
            print("Employee not found.")

    def calculate_payroll(self):
        if not self.employees:
            print("No employees found.")
            return
        print("Payroll Summary:")
        print("================")
        for employee in self.employees:
            salary = employee.calculate_salary()
            print(f"{employee.name} with ID {employee.id} earned {salary} this week.")

    def save_data(self):
        with open('employee_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for employee in self.employees:
                writer.writerow([employee.name, employee.id, employee.hourly_rate])


payroll = Payroll()
payroll.load_data()

while True:
    print("\n1. Add employee\n2. Add hours worked\n3. Calculate payroll\n4. Save employee data to file\n5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        payroll.add_employee()
        print("Employee added.")
    elif choice == "2":
        payroll.add_hours()
    elif choice == "3":
        payroll.calculate_payroll()
    elif choice == "4":
        payroll.save_data()
        print("Employee data saved.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

    # display employee data on the terminal
    print("\nEmployee Data:")
    print("==============")
    for employee in payroll.employees:
        print(f"{employee.name} with ID {employee.id} and hourly rate {employee.hourly_rate}")

