class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append({
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })

    def total_value(self):
        total = 0
        for drug in self.drugs:
            total += drug.amount * drug.price
        return total

    def employees_summary(self):
        summary = "Employees:\n"
        for i, employee in enumerate(self.employees):
            summary += f"The employee number {i + 1} is {employee['first_name']} {employee['last_name']} who is {employee['age']} years old.\n"
        return summary


drug = Drug('ritalin', 20, 200000)
drug2 = Drug('vias', 10, 100000)
khodayar = Pharmacy("khodayar", [], [])
khodayar.add_drug("drug")
print(khodayar.total_value())
