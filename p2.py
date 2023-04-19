import csv

class Employee:
    def __init__(self, name, id, hourly_rate):
        self.name = name
        self.id = id
        self.hourly_rate = hourly_rate

class Payroll:
    def __init__(self):
        self.employees = []
        # automatically create employee_data.csv file if it doesn't exist
        with open('employee_data.csv', mode='a', newline='') as file:
            pass

    def load_data(self):
        with open('employee_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, id, hourly_rate = row
                self.employees.append(Employee(name, id, float(hourly_rate)))
        print("Employee data loaded.")
        self.display_employees()

    def add_employee(self):
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        hourly_rate = float(input("Enter employee hourly rate: "))
        self.employees.append(Employee(name, id, hourly_rate))

        # write employee data to CSV file
        with open('employee_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, id, hourly_rate])
        print("Employee added successfully.")
        self.display_employees()

    def calculate_payroll(self):
        total_payroll = sum([employee.hourly_rate for employee in self.employees])
        print("Total payroll: $", total_payroll)

    def display_employees(self):
        print("Employee Data:")
        print("Name\tID\tHourly Rate")
        for employee in self.employees:
            print(f"{employee.name}\t{employee.id}\t{employee.hourly_rate}")

if __name__ == "__main__":
    payroll = Payroll()
    payroll.load_data()
    while True:
        print("Select an option:")
        print("1. Add Employee")
        print("2. Calculate Payroll")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            payroll.add_employee()
        elif choice == '2':
            payroll.calculate_payroll()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
