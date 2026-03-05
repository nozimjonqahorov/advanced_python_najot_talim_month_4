# def hello(name = "Jasur"):
#     print(f"Hello {name}!")

#     def greet():
#         print("This is the greet function inside the hello function.")

#     def welcome():
#         print("This is the welcome function inside the hello function.")

#     print("Im going to return a function.")
#     if name == "Jasur":
#         return welcome
#     else:
#         return greet

# new_func = hello("Jasur")   
# new_func()                         ###    Hello Jasur! Im going to return a function. This is the welcome function inside the hello function.

# new_func2 = hello("John")
# new_func2()                        ###    Hello John! Im going to return a function. This is the greet function inside the hello function.


# def hello():
#     return "Hello Jasur!"

# def other(some_def_func):
#     print("Other code runs here!")
#     print(some_def_func())

# other(hello)   #giving the hello() function as an argument to the other() function.
#  ###   
# # Other code runs here! 
# # Hello Jasur! 

# #passing a function in another function as an argument


# def new_decorator(original_func):
#     def wrap_func():
#         #the main part
#         print("Some extra code, before the original function.")
#         original_func()
#         print("Some extra code, after the original function.")
#     return wrap_func

# def func_needs_decorator():
#     print("I want to be decorated!!")
#     print("I need some extra functionality!!")

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()    
### #                                            logic of creating a decorator :def new_decorator(original_func):
    
# def new_decorator(original_func): 
#     def wrap_func():
#         print("Some extra code, before the original function.")
#         original_func()
#         print("Some extra code, after the original function.")
#         return wrap_func

# @new_decorator
# def func_needs_decorator():
#     print("I want to be decorated!!")
#     print("I need some extra functionality!!")

# func_needs_decorator()

# Some extra code, before the original function. 
# I want to be decorated!! 
# I need some extra functionality!! 
# Some extra code, after the original function.
 

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function.")
        original_func()
        print("Some extra code, after the original function.")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")
    print("I need some extra functionality!!")

func_needs_decorator()

# In professional code,  we do not just use decorators to print text. Mostly decorators are used for:

# Logging: Record when a function was called.

# Authentication: Check if a user is logged in before letting them run a function.

# Timing: Measure how many seconds a function takes to run.

# Validation: Ensure the data being passed to a function is correct.