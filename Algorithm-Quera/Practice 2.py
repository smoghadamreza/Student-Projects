string = "Test"


def test(string):
    string = "For Practice"
    print("Inside Function:", string)

# call by reference
def add_more(list):
    list.append(50)
    print("Inside Function", list)
