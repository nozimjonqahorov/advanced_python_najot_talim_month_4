import csv

# filename = "students.csv"

# students = [
#     ["Ali", 18, "Python"],
#     ["Vali", 20, "Django"],
#     ["Hasan", 19, "FastAPI"]
# ]


# with open(filename, "w", newline = "") as file:
#     writer = csv.writer(file)
#     writer.writerows(students)

# with open(filename, "r", newline = "") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#2 masala

# filename = "products.csv"

# products = [
#     {"name": "Laptop", "price": 1200, "qty": 5},
#     {"name": "Phone", "price": 800, "qty": 10},
#     {"name": "Mouse", "price": 20, "qty": 50}
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["name", "price", "qty"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(products)

# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     mylist = []
#     for row in reader:
#         mylist.append(row)

#     print(mylist)

# 3 masala

# filename = "users.csv"

# users = [
     
#     {"id": 1, "username":"nozim", "email": "nozimjonkahhorov@gmail.com", "age": 20},
#     {"id": 2, "username":"nizom", "email": "sobiroorov@gmail.com", "age": 50},
#     {"id": 3, "username":"jasurbek", "email": "qodirov@gmail.com", "age": 30},
#     {"id": 4, "username":"husan", "email": "husan@gmail.com", "age": 24} 
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["id", "username", "email", "age"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(users)

# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     mylist = []
#     for row in reader:
#         mylist.append({ "username": row["username"], "email": row["email"] })
#     print(mylist)

#4 masala

# filename = "numbers.csv"

# numbers = [
#     [2, 5, 8],
#     [10, 3, 7],
#     [6, 6, 6]
# ]

# with open(filename, "w", newline = "") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)

# with open(filename, "r", newline = "") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open(filename, "r", newline = "") as file:
#     reader = csv.reader(file)
#     for n, row in enumerate(reader, 1):
#         print(f"{n}-chi qator summasi: {sum(int(i) for i in row)}")

# 5-masala. CSV dan filter qilish  

# CSV fayl name,score
# Ali,78
# Vali,45
# Hasan,90
# Olim,60

# Vazifa:
# - CSV fayldan o‘qing
# - score >= 60 bo‘lganlarni ajrating
# - Natijani list of dict ko‘rinishida chiqaring

# filename = "results.csv"

# results = [
#     {"name": "Ali", "score": 78},
#     {"name": "Vali", "score": 45},
#     {"name": "Hasan", "score": 90},
#     {"name": "Olim", "score": 60}
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["name", "score"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(results)

# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     mylist = []
#     for row in reader:
#         mylist.append({ "name": row["name"], "score": row["score"] }) if int(row["score"]) >= 60 else None
#     print(mylist)

#6-masala. CSV + Sort

# filename = "students_2.csv"

# students = [
#     {"name": "Ali", "age": 18, "score": 75},
#     {"name": "Vali", "age": 19, "score": 90},
#     {"name": "Hasan", "age": 18, "score": 60},
#     {"name": "Olim", "age": 20, "score": 85}
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["name", "age", "score"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(students)

# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     mylist = []
#     for row in reader:
#         mylist.append({ "name": row["name"], "age": row["age"], "score": row["score"] })

#     mylist = sorted(mylist, key=lambda x: int(x["score"]), reverse=True)
#     print(mylist)

#8 masala 
 
# employees.csv:
# id,name,salary
# 1,Ali,1000
# 2,Vali,1200
# 3,Hasan,900

# Vazifa:
# - CSV dan o‘qing
# - salary < 1000 bo‘lganlarga 20% qo‘shing
# - Yangilangan ma’lumotni yana CSV faylga yozing

# filename = "employee.csv"

# employee = [
#     {"id":1, "name":"Ali", "salary":1000},
#     {"id":2, "name":"Vali", "salary":1200},
#    {"id":3, "name":"Hasan", "salary":900}
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["id", "name", "salary"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(employee)

# filename = "employee.csv"
# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     mylist = []
#     for row in reader:
#         if int(row["salary"]) < 1000:
#             row["salary"] = int(row["salary"]) + int(row["salary"]) * 0.2
#         mylist.append({ "id": row["id"], "name": row["name"], "salary": row["salary"] })

#     print(mylist)

# filename = "employee_added_salary.csv"

# with open(filename, "w", newline="") as file:
#     ustunlar = ["id", "name", "salary"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(mylist)

# 9-masala. CSV dan GROUP BY qilish
# ------------------------------------
# orders.csv:
# user,amount
# Ali,200
# Vali,150
# Ali,300
# Vali,100
# Hasan,400

# Vazifa:
# - CSV fayldan o‘qing
# - Har bir foydalanuvchi bo‘yicha umumiy summani hisoblang
# - Natijani dict ko‘rinishida chiqaring:

# filename = "orders.csv"

# orders = [
#     {"user":"Ali", "amount":200},
#     {"user":"Vali", "amount":150},
#     {"user":"Ali", "amount":300},
#     {"user":"Vali", "amount":100},
#     {"user":"Hasan", "amount":400}
# ]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["user", "amount"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(orders)

# with open(filename, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     rows = list(reader)
    
# totals = {}

# for row in rows:
#     user = row['user']
#     amount = int(row['amount'])

#     if user not in totals:
#         totals[user] = 0
    
#     totals[user] += amount

# print(totals)
    
# 10-masala. CSV + Validatsiya
# ------------------------------------
# students.csv:
# name,age,score
# Ali,18,90
# Vali,-2,70
# Hasan,20,150
# Olim,19,80

# Vazifa:
# - CSV fayldan o‘qing
# - age < 0 yoki score > 100 bo‘lgan qatorlarni xato deb ajrating
# - To‘g‘ri ma’lumotlarni clean_students.csv ga yozing
# - Xato qatorlarni errors.csv ga yozing

filename = "students_2.csv"

students = [
    {"name":"Alli", "age":18, "score": 90},
    {"name":"Vali", "age":-2, "score": 70},
    {"name":"Hasan", "age":20, "score": 150},
    {"name":"Olim", "age":19, "score": 80}
]

# with open(filename, "w", newline="") as file:
#     ustunlar = ["name", "age", "score"]
#     writer = csv.DictWriter(file, fieldnames=ustunlar)
#     writer.writeheader()
#     writer.writerows(students)

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
    clean_rows = []
    error_rows = []
    for row in rows:
        if int(row["age"]) < 0:
            error_rows.append(row)
        elif int(row["score"]) > 100:
            error_rows.append(row)
        else:
            clean_rows.append(row)
print(clean_rows)
print(error_rows)

filename = "clean_students.csv"

with open(filename, "w", newline="") as file:
    ustunlar = ["name", "age", "score"]
    writer = csv.DictWriter(file, fieldnames=ustunlar)
    writer.writeheader()
    writer.writerows(clean_rows)

filename = "errors.csv"

with open(filename, "w", newline="") as file:
    ustunlar = ["name", "age", "score"]
    writer = csv.DictWriter(file, fieldnames=ustunlar)
    writer.writeheader()
    writer.writerows(error_rows)