# Functions with keyworded arguments
def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('safi', age=30, city='Bhavnagr', Mob=8866351120)
