# a = [1, 2, 3, 4, 5, 6]
# b = a.__iter__()
# b = iter(a)

# print(next(b))
# print(next(b))
# print(next(b))

# while True:
#     try:
#         x = next(b)
#         if x % 2 == 0:
#             print(x)
#     except StopIteration:
#         break

# 100_000 
# a = [1, 2, 3, 9, 23, 88]
# b = iter(a)


# while True:
#     try:
#         x = next(b)
#         if x % 2 == 0:
#             print(x)
#     except StopIteration:
#         break

# i = len(a)
# while i > 0:
#     i -= 1
#     print(a[i])




# print(next(b))
# print(next(b))
# print(next(b))










# def my_generator():
#     for i in range(1, 16):
#         yield i
# gen = my_generator()
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 2
# print(next(gen))  # 2
# print(next(gen))  # 2
# print(next(gen))  # 2

# print(my_generator())


# Qolgan elementlarni for yordamida chiqarish
# for item in gen:
#     print(item)





# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = simple_generator()

# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # StopIteration istisnosi

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# x = count_up_to(3)

# print(next(x))
# print(next(x))

# for number in count_up_to(5):
#     print(number)

# mylist = [i for i in range(1, 1000001)]
# def generator(lst):
#     for i in lst:
#         if str(i)[0] == str(i)[-1] and i > 9:
#             yield i

# result = generator(mylist)
# print(next(result))
# print(next(result))

filename = "tub.txt"

# def tubs_son(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True




def tubs_son(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tub_son_from_file(oraliq: int):
    with open("tub.txt", "r") as file:
        for _ in range(oraliq):
            data = file.readline().strip()   # bo‘sh joylarni olib tashlaydi
            if not data:                     # agar bo‘sh bo‘lsa, o‘tkazib yubor
                continue
            if data.isdigit():               # faqat son bo‘lsa
                if tubs_son(int(data)):
                    yield int(data)
