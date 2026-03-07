# 1.  Fayldagi satrlarni generator orqali o‘qish data.txt fayli berilgan.
#    Generator yozing, u fayldagi har bir satrni bittadan qaytarsin.


# def show_content(file_name):
#     with open(file_name,"r") as file:
#         for line in file:
#             yield line
# result = show_content("data.txt")

# while True:
#     try:
#         line = next(result)
#         print(line)
#     except StopIteration as s:
#         print(f"Qatorlar tugadi! ")
#         break

# 2.  Fayldagi sonlardan juftlarini qaytarish numbers.txt faylida sonlar
#    yozilgan. Generator yozing, u faqat juft sonlarni qaytarsin.

# def show_even_number(file_name):
#     with open(file_name,"r") as file:
#         for line in file:
#                 for n in line.split(): 
#                     if int(n) % 2 == 0:
#                         yield int(n)


# result = show_even_number("numbers.txt")

# while True:
#     try:
#         line = next(result)
#         print(line)
#     except StopIteration as s:
#         print(f"Qatorlar tugadi! ")
#         break

# 3.  Fayldagi uzun satrlarni topish text.txt fayl berilgan. Generator
   # yozing, u 5 ta belgidan uzun satrlarni qaytarsin.

# def show_long_lines(file_name):
#     with open(file_name,"r") as file:
#         for line in file:
#             if len(line) > 5:
#                 yield line
# result = show_long_lines("data.txt")

# while True:
#     try:
#         line = next(result)
#         print(line)
#     except StopIteration as s:
#         print(f"Qatorlar tugadi! ")
#         break


#4.  Fayldagi sonlarning kvadratini qaytarish nums.txt faylida sonlar
  #  bor. Generator yozing, u har bir sonning kvadratini qaytarsin.

# def show_squared_number(file_name):
#     with open(file_name,"r") as file:
#         for line in file:
#                 for n in line.split(): 
#                         yield int(n) ** 2

# result = show_squared_number("numbers.txt")

# while True:
#     try:
#         line = next(result)
#         print(line)
#     except StopIteration as s:
#         print(f"Qatorlar tugadi! ")
#         break

# 5.  Fayldagi barcha so‘zlarni generator orqali ajratish words.txt fayl
#     berilgan. Generator yozing, u fayldagi barcha so‘zlarni bittadan
#     qaytarsin

# def show_every_word(file_name):
#     with open(file_name,"r") as file:
#         for line in file:
#                 for n in line.split(): 
#                         yield n

# result = show_every_word("data.txt")

# while True:
#     try:
#         line = next(result)
#         print(line)
#     except StopIteration as s:
#         print(f"Qatorlar tugadi! ")
#         break


import psycopg2

conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="advanced",
        user="postgres",
        password=170879
)

cur = conn.cursor()
"""6.  Database dan user nomlarini generator orqali olish users jadvali
    berilgan."""
# def get_user_generator():
#     cur.execute("SELECT name FROM users;")
#     while True:
#         try:
#             users = cur.fetchone()
#             if users == None:
#                 break

#             yield users

#         except StopIteration:
#             break

# users = get_user_generator()
# for user in users:
#     print(user)

# print(next(users))
# print(next(users))
# print(next(users))

"""7.  Database dan narxi katta mahsulotlarni chiqarish products jadvali
    berilgan."""

# def get_expensive_product():
#     cur.execute("SELECT * FROM products WHERE price > 10000;")
#     while True:
#         try:
#             users = cur.fetchone()
#             if users == None:
#                 break

#             yield users

#         except StopIteration:
#             break
        
# products = get_expensive_product()
# # for product in products:
# #     print(product)

# print(next(products))
# print(next(products))
# print(next(products))

"""8.  Database dan faqat email larni olish users jadvali berilgan.."""

# def get_email_generator():
#     cur.execute("SELECT email FROM students;")
#     while True:
#         try:
#             users = cur.fetchone()
#             if users == None:
#                 break

#             yield users

#         except StopIteration:
#             break

# users = get_email_generator()
# # for user in users:
# #     print(user)

# print(next(users))
# print(next(users))
# print(next(users))

"""9.  Database dan eng uzun ismli userni topish Generator yozing, u
    database dagi userlarni bittadan olib, eng uzun ismni topishga
    yordam bersin.
"""
# def longest_name_generator(cur):
#     cur.execute("SELECT name FROM students;")
#     longest = ""
#     for (name,) in cur:
#         if len(name) > len(longest):
#             longest = name
#         yield longest  


# current_longest = longest_name_generator(cur)

# print(next(current_longest))  


"""10. Database dan pagination generator products jadvali berilgan.
Generator yozing, u mahsulotlarni 5 tadan qilib qaytarsin.
Misol: 1-5 6-10 11-15
"""

def pagination_generator():
    cur.execute("SELECT * FROM products;")
    while True:
        try:
            users = cur.fetchmany(5)
            if users == None:
                break

            yield users

        except StopIteration:
            break

products = pagination_generator()
# for product in products:
#     print(product)

print(next(products))
print(next(products))
print(next(products))
