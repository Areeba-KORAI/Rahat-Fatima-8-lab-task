def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee(name="Areeb", age=20, salary=5000000, department="artificial intelligence")