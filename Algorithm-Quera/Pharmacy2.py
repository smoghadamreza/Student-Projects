class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = list()
        self.employees = list()

    def add_drug(self, drug):
        self.drugs.append(drug)
        return self.name

    def add_employee(self, first_name, last_name, age):
        detail = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }
        self.employees.append(detail)

    def total_value(self):
        sum = 0
        for drug in self.drugs:
            z = drug.price * drug.amount
            sum += z
        return sum

    def employees_summary(self):
        lst = ""
        lst += "Employees:\n"
        j = 0
        for i in self.employees:
            j += 1
            lst += "The employee number {} is {} {} who is {} years old.\n".format((j), (i["first_name"]),
                                                                                   (i["last_name"]), (i["age"]))
        return lst


d1 = Drug('Vyas', 20, 12)
d2 = Drug('Ritalin', 10, 12)
ph1 = Pharmacy("Khodayar")
print(ph1.add_drug(d1))
ph1.add_drug(d2)
print(ph1.total_value())
