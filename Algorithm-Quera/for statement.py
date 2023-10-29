for i in range(100, 1000):
    c=i % 10
    a=i / 100
    b = ((i % 100) - c) / 10
    d = (a + b + c) * 100
    if (i == d):
        print(i)
