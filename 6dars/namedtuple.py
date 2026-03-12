from collections import namedtuple

# Car = namedtuple('Car', ('model', 'make', 'price'))


# Dorixona = namedtuple("Dorixona", ("dorinomi", "soni", "narxi"))

# def create_object():
#     data = []
#     while True:
#         for field_name in Dorixona._fields:
#             obct = input(f"{field_name} ni kiriting: ")
#             data.append(obct)
#         break

#     new_list = Dorixona._make(data)
#     print(new_list)
# create_object()

Dog = namedtuple("Dog",["age", "breed", "name"])

sammy = Dog(age = 4, breed = "Husky", name = "Sam")

print(sammy[0])                              # 4
print(sammy[1])                              # Husky
print(sammy[-1]) #print(sammy[2])            # Sam


print(sammy.age)                              # 4
print(sammy.breed)                            # Husky
print(sammy.name)                             # Sam

print(sammy._asdict())                        # {'age': 4, 'breed': 'Husky', 'name': 'Sam'}

Cat = namedtuple("Cat", ["age", "breed", "name"], defaults=[0, "Unknown", "Unnamed"])
print(Cat())                                    # Cat(age=0, breed='Unknown', name='Unnamed')

cat1 = Cat(age = 3, name = "Pismat")

print(cat1)                                    # Cat(age=3, breed='Unknown', name='Pismat')
