class School:
    def __init__(self, Number):
        self.number = Number
        self.height = []
        self.age = []
        self.weight = []

    def get_heights(self):
        count = 0
        while count != self.number:
            hei = int(input())
            self.height.append(hei)
            count += 1

    def get_age(self):
        count = 0
        while count != self.number:
            ag = int(input())
            self.age.append(ag)
            count += 1

    def get_wei(self):
        count = 0
        while count != self.number:
            wei = int(input())
            self.weight.append(wei)
            count += 1

class A(School):
    def average(self):



class B(School):
    pass
