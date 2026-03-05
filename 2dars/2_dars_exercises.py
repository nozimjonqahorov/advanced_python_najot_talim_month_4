from functools import reduce

# 1 Berilgan sonlar ro‘yxatidagi har bir songa 2 qo‘shing.
#  Input: [1, 2, 3, 4]   Output: [3, 4, 5, 6]

# def add_num(n):
#     return n + 2
# data = [1, 2, 3, 4]
# result = list(map(add_num, data))
# print(result)




### 2️⃣ Berilgan sonlar ro‘yxatidan faqat juft sonlarni ajrating.
# 📌 Input: [1, 2, 3, 4, 5, 6]
# 📌 Output: [2, 4, 6]

# def remove_odd(lst):
#     return [i for i in lst if i % 2 == 0] 
# print(remove_odd([1, 2, 3, 4, 5, 6]))

# def remove_odd(n):
#     return n % 2 == 0      

# data = [1, 2, 3, 4, 5, 6]
# result = list(filter(remove_odd, data))
# print(result)  


### 3️⃣  Berilgan sonlar ro‘yxatidagi barcha sonlar yig‘indisini toping.
# 📌 Input: [10, 20, 30]
# 📌 Output: 60

# def summ(lst):
#     return sum(lst)
# print(summ([10, 20, 30]))


### 4️⃣   Ismlar ro‘yxatini katta harflarga o‘tkazing.
# 📌 Input: ["ali", "vali", "hasan"]
# 📌 Output: ["ALI", "VALI", "HASAN"]

# def upper_list(lst):
#     return [i.upper() for i in lst]
# print(upper_list(["ali", "vali", "hasan"]))

# def upper_word(n):
#     return n.upper()
# data = ["ali", "vali", "hasan"]
# result = list(map(upper_word, data))
# print(result)

# ## 5️⃣ Ikki ro‘yxat berilgan: ismlar va yoshlar.
# Ularni juftlab chiqaring.
# 📌 Input:
# ["Ali", "Vali"]
# [18, 20]
# 📌 Output: [("Ali", 18), ("Vali", 20)]

# names = ["Ali", "Vali"]
# ages = [18, 20]
# result = list(zip(names, ages))
# print(result)

#  👉 Maqsad: map + filter + zip kombinatsiyasi

# ## 6️⃣   Berilgan sonlar ro‘yxatidan manfiy bo‘lmaganlarni olib, ularning kvadratini chiqaring.

# nums = [1, 2, 3, -4, 5, -6, 8]

# positive = list(filter(lambda n: n >= 0, nums))
# squared = list(map(lambda n: n ** 2, positive))

# print(squared)

# numbers = [-3, -1, 0, 2, 4]

# result = list(map(lambda n: n ** 2, filter(lambda n: n >= 0, numbers)))
# print(result)  

### 7️⃣   Ballar ro‘yxatidan 60 dan o‘tganlarni olib, har biriga 5 ball qo‘shing.

# ballar = [40, 65, 50, 70, 80, 78, 90]
# result = list(map(lambda n: n + 5, filter(lambda n: n > 60, ballar)))
# print(result)  


### 8️⃣   Narxlar ro‘yxatiga 10% chegirma qo‘llang va yangi narxlar ro‘yxatini chiqaring.

# narxlar = [700, 795, 805, 830, 950, 1000]
# result = list(map(lambda n: n - (n * 0.10), narxlar))
# print(result)  

### 9️⃣    Ismlar ro‘yxatidan faqat uzunligi 5 ta va undan katta bo‘lgan ismlarni ajrating.

# names = ["Ali", "Vali", "Hasan", "Zara", "Malika", "Bob", "Jo", "Sardor", "Nilufar", "Tim"]
# result = list(filter(lambda n: len(n) >= 5, names))
# print(result)

### 🔟  Berilgan sonlar ro‘yxatidagi eng katta sonni toping   (❗️ max() ishlatmasdan).

# nums = [40, 65, 50, 70, 80, 78, 90, 33, 45]
# result = reduce(lambda a, b: a if a > b else b, nums)
# print(result) 

### 1️⃣1️⃣  Ikki ro‘yxat berilgan: mahsulot nomlari va narxlari.
# Narxi 50000 dan katta mahsulotlarni (nom, narx) ko‘rinishida chiqaring.

# products = ["Naushnik", "Telefon", "Quloqchin", "Klaviatura", "Sichqoncha"]
# prices = [120_000, 800_000, 40_000, 35000, 15000]

# result = list(zip(products, filter(lambda n: n > 50_000, prices)))
# print(result)

### 1️⃣2️⃣  Sonlar ro‘yxatidagi toq sonlar yig‘indisini toping.

# nums = [40, 65, 50, 70, 80, 78, 90, 33, 45]
# result = reduce(lambda a, b: a+ b , filter(lambda n: n % 2 == 1, nums))
# print(result)

### 1️⃣3️⃣ Ismlar ro‘yxatini ularning uzunligiga aylantiring.    📌 ["Ali", "Hasan"] → [3, 5]

# ismlar = ["Ali", "Hasan"]

# result = list(map(lambda x: len(x), ismlar))
# print(result)

### 1️⃣4️⃣    Berilgan sonlar ro‘yxatidan musbat sonlar ko‘paytmasini toping.

# nums = [1, 2, 3, -4, 5, -6, 8]
# result = reduce(lambda a, b: a * b , filter(lambda n: n >= 0, nums))
# print(result) 

### 1️⃣5️⃣  Ikki ro‘yxat berilgan: talabalar va ularning ballari.
#    Faqat 70 dan yuqori olganlarni chiqarish.

# talabalar = ["Ali", "Vali", "Hasan", "Zara", "Malika", "Sardor", "Nilufar", "Bob"]
# ballar = [85, 92, 47, 78, 55, 90, 71, 38]

# result = list(zip(talabalar, filter(lambda n: n > 70, ballar)))
# print(result)

# 🔴 QIYIN MASALALAR (10 ta)

# 👉 Maqsad: real hayotga yaqin, kombinatsiyali masalalar

### 1️⃣6️⃣  Talabalar ballari berilgan.
# * 60 dan o‘tganlarni tanlang
# * Har biriga 10 ball qo‘shing
# * Yangi o‘rtacha ballni hisoblang

# talabalar = ["Ali", "Vali", "Hasan", "Zara", "Malika", "Sardor", "Nilufar", "Bob"]
# ballar = [85, 92, 47, 78, 55, 90, 71, 38]

# bonusli = list(map(lambda x: x + 10, filter(lambda n: n > 60, ballar)))

# yigindi  = reduce(lambda a, b: a + b, bonusli)
# ortacha  = yigindi / len(bonusli)

# print(ortacha)

### 1️⃣7️⃣  Sonlar ro‘yxatidan:
# * manfiylarni olib tashlang
# * faqat juftlarni qoldiring
# * ularning kvadratlari yig‘indisini toping

# nums = [1, 20, 3, -4, 5, -6, 8, 12, ]

# sortlangan = list(filter(lambda x: x > 0 and x % 2 == 0, nums))
# result = reduce(lambda a, b: a + b, list(map(lambda x: x ** 2, sortlangan)))
# print(result)

### 1️⃣8️⃣  Mahsulotlar va narxlar berilgan.
# * 20% chegirma qo‘llang
# * 100000 dan yuqori bo‘lganlarni chiqaring

# products = ["Naushnik", "Telefon", "Quloqchin", "Klaviatura", "Sichqoncha", "blok-sxema"]
# prices = [120_000, 800_000, 40_000, 35000, 15000, 300_000]

# juftlar  = list(zip(products, prices))
# chegirma = list(map(lambda x: (x[0], x[1] * 0.8), juftlar))
# result   = list(filter(lambda x: x[1] > 100000, chegirma))

# print(result)

### 1️⃣9️⃣  Ismlar ro‘yxatida:
# * uzunligi 4 dan katta bo‘lganlarni oling
# * katta harfga o‘tkazing
# * bitta stringga birlashtiring 

#1
# names = ["Ali", "Vali", "Hasan", "Zara", "Malika", "Bob", "Jo", "Sardor", "Nilufar", "Tim"]
# sortlangan = list(map(lambda x: x.upper(), filter(lambda n: len(n) > 4, names)))
# result = "".join(sortlangan)
# print(result)

# #2
# result = reduce(lambda a, b: a.upper() + "" + b.upper(), filter(lambda n: len(n) > 4, names))
# print(result)


### 2️⃣0️⃣   Sonlar ro‘yxatidagi eng katta va eng kichik sonlar ayirmasini toping
#  (max va min ishlatmasdan).


# nums = [40, 65, 5, 70, 8, 78, 90, 33, 45]
# katta = reduce(lambda a, b: a if a > b else b, nums)
# kichik = reduce(lambda a, b: a if a < b else b, nums)
# result = katta - kichik 
# print(katta)
# print(kichik)
# print(result)


### 2️⃣1️⃣  3 ta ro‘yxat berilgan: ism, yosh, ball.
# Faqat 18 yoshdan katta va 70 balldan yuqori bo‘lganlarni chiqaring.

# ismlar = ["Ali", "Vali", "Hasan", "Zara", "Malika", "Sardor", "Nilufar", "Bob"]
# yoshlar = [20, 17, 22, 19, 25, 16, 21, 18]
# ballar  = [85, 92, 47, 78, 55, 90, 63, 38]

# juftlar = list(zip(ismlar, yoshlar, ballar))
# result = list(filter(lambda x: x[0] and x[1] > 18 and x[2] > 70, juftlar))
# print(result)

### 2️⃣2️⃣   Matnlar ro‘yxatidan:
# * bo‘sh stringlarni olib tashlang
# * qolganlarini katta harfga o‘tkazing

# matnlar = ["salom","", "python", "", "django", "najot", "talim"]

# result = list(map(lambda x: x.upper(),filter(lambda x: x, matnlar)))
# print(result)

### 2️⃣3️⃣  Sonlar ro‘yxatini dictionary ko‘rinishiga o‘tkazing:   son → uning kvadrati
# nums = [40, 65, 5, 70, 8, 78, 90, 33, 45]
# kvadratlar = list(map(lambda x: x**2, nums))
# result = dict(zip(nums, kvadratlar))
# print(result)

### 2️⃣4️⃣  Talabalar ballaridan:
# * eng yuqori 3 tasini tanlang
# * ularning o‘rtacha qiymatini hisoblang

# ballar = [85, 92, 47, 78, 55, 90, 63, 38]

# top = sorted(ballar, reverse=True)[:3]
# ortacha = reduce(lambda a, b: a + b, top) / len(top)
# print(top)    
# print(ortacha)

### 2️⃣5️⃣  Berilgan gapdagi so‘zlar ro‘yxatidan:
# * uzunligi 3 dan katta so‘zlarni tanlang
# * ularni bitta gapga birlashtiring

gap = "men python dasturlash tilini o'rganmoqdaman"
ruyxat = gap.split()
result = reduce(lambda a, b: a + " " + b, filter(lambda n: len(n) > 3, ruyxat))
print(result)