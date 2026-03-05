import inspect

def decorator1(func):
    def wrapper(*args, **kwargs):
        print(f"Funksiya nomi: {func.__name__}")
        print(f"Argumentlari: {inspect.signature(func)}")
        return func(*args, **kwargs)
    return wrapper

@decorator1
def multiplication(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(multiplication(1, 2, 3, 4, 5))

#2
# def counter(func):
#     count = 0  
#     def wrapper(*args, **kwargs):
#         nonlocal count   
#         count += 1
#         print(f"{func.__name__} {count}-marta chaqirildi")
#         return func(*args, **kwargs)

#     return wrapper

# @counter
# def multiplication(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result

# print(multiplication(1, 2, 3))  
# print(multiplication(4, 5))      
# print(multiplication(2))         


#3

# def require_login(func):
#     def wrapper(user, *args, **kwargs):
#         if not getattr(user, "is_logged_in", False):
#             return "Iltimos avval log in qiling! "
#         return func(user, *args, **kwargs)
#     return wrapper

# class User:
#     def __init__(self, name, is_logged_in=False):
#         self.name = name
#         self.is_logged_in = is_logged_in


# @require_login
# def view_profile(user):
#     return f"Profile of {user.name}"



# u1 = User("Nozimjon", is_logged_in=True)
# u2 = User("Ali", is_logged_in=False)

# print(view_profile(u1))
# print(view_profile(u2))

#4

# def format_output(func):
#     def wrapper(a):
#         return str(func(a))
#     return wrapper

# @format_output
# def kvadrat_num(a):
#     return a * a
    
# print(kvadrat_num(3))

#5
# file_name = "log.txt"

# def write_log(func):
#     def wrapper(a, b):
#         with open(file_name, "a") as file:
#             file.write(str(func(a, b)) + "\n")
#         return "Natija log.txt filega yozildi."
#     return wrapper

# @write_log
# def add_num(a, b):
#     return a + b

# @write_log
# def minus_num(a, b):
#     return a - b

# print(add_num(2, 5))
# print(minus_num(12, 6))


# with open(file_name) as f:
#     print("Fayldagi yozuvlar:")
#     print(f.read())


#6. Funksiya nomi va natijasini txt file ga yozib boradigan decorator yozing

file_name = "natija.txt"

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        with open(file_name, "a") as file:
            file.write(f"{func.__name__} {count}-marta chaqirildi. Natija: {result}\n")
        return result
    return wrapper

@counter
def add_num(a, b):
    return a + b

print(add_num(5, 8))
print(add_num(2, 3))

@counter
def multiply(a, b):
    return a * b

print(multiply(12, 4))
print(multiply(7, 9))

with open(file_name) as f:
    print("Fayldagi yozuvlar:")
    print(f.read())


