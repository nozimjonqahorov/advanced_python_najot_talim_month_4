#1 hello.txt nomli fayl yarating va ichiga:   Salom Python matnini yozing.

# a = open("hello.txt", "w")
# a.write("Salom Python")
# a.close()

#2 hello.txt faylidagi matnni ekranga chiqaring.

# a = open("C:\\Users\\user\\Desktop\\nt\\month3\\homeworks\\hello.txt", "r")
# result = a.read()
# print(result)
# a.close()


#3 names.txt faylida nechta qator borligini hisoblang.

# a = open("C:\\Users\\user\\Desktop\\nt\\month3\\homeworks\\name.txt", "r", encoding="utf-8")
# result = a.readlines()
# print(f"Name.txt filedagi qatorlar soni: {len(result)}")
# a.close()

# 4  log.txt fayliga:  Dastur ishga tushdi  qatorini o‘chirib yubormasdan qo‘shib yozing.

# a = open("C:\\Users\\user\\Desktop\\nt\\month3\\homeworks\\log.txt", "a")
# result = a.write("Dastur ishga tushdi\n")
# print(result)
# a.close()

#5 data.txt fayli mavjudmi yoki yo‘qmi — ekranga chiqaring.

# import os

# file_name = "name.txt"

# if os.path.isfile(file_name):
#     print(f"'{file_name}' fayli mavjud.")
# else:
#     print(f"'{file_name}' fayli mavjud emas.")


#6 text.txt faylidagi barcha so‘zlar sonini toping.

# a = open("log.txt", "r", encoding="utf-8")
# result = a.read().split()
# print(f"log.txt file-dagi sozlar soni: {len(result)}")
# a.close()

#7 lines.txt faylidagi eng uzun qatorni topib chiqaring.

# a = open("log.txt", "r", encoding="utf-8")
# result = a.readlines()
# max_len = ""
# for line in result:
#     if len(line) > len(max_len):
#         max_len = line
# print(f"Eng uzun qator: {max_len.strip()} uzunligi: {len(max_len)}")
# a.close()

#2 variant

# a = open("log.txt", "r", encoding="utf-8")
# result = a.readlines()

# eng_uzun = max(result, key=len) 
# print("Eng uzun qator:") 
# print(eng_uzun.strip())
# a.close()


#8 numbers.txt faylida quyidagilar bor: 5, 12, 8, 20  Ularning yig‘indisini hisoblang.

# a = open("numbers.txt", "r", encoding="utf-8")
# result = a.readlines()
# print(f"Yig'indi: {sum(int(i) for i in result)}")
# a.close()


#9 input.txt faylidagi barcha matnni katta harflarga o‘tkazib,     output.txt fayliga yozing.

# a = open("input.txt", "r", encoding="utf-8")
# result = a.read()
# b = open("output.txt", "a")
# for line in result:
#     natija = b.write(line.upper())

# print(natija)
# a.close()
# b.close()

# 10 data.txt faylidagi bo‘sh qatorlarni olib tashlab,     natijani clean.txt fayliga yozing.

# a = open("data.txt", "r", encoding="utf-8")
# b = open("clean.txt", "w") 

# for line in a:
#     print(line)
#     if line.strip() != "": 
#         b.write(line)

# a.close()
# b.close()


# 11  story.txt faylidan eng ko‘p uchraydigan so‘zni toping.

# a = open("story.txt", "r", encoding="utf-8")
# result = a.read().split()
# kup_uchragan = 0
# for word in result:
#     if kup_uchragan < result.count(word):
#         kup_uchragan = result.count(word)
#         print(f"Eng kup uchragan so'z: {word}, Ushbu so'z matnda {kup_uchragan} marotaba kelgan! ")
# a.close()


#12 mixed.txt faylida matn va sonlar aralash Ali 12 yoshda Vali 15 yoshda    Faqat sonlarni olib, numbers.txt ga yozing.

# a = open("mixed.txt", "r", encoding="utf-8")
# b = open("numbers.txt", "a")
# result = a.read().split()
# for word in result:
#     if word.isdigit():
#         b.writelines(word + "\n")
# a.close()
# b.close()


#13 Fayl nusxasini olish source.txt faylidan nusxa olib,   backup.txt fayliga aynan ko‘chiring.

# a = open("source.txt", "r", encoding="utf-8")
# result = a.read()
# b = open("backup.txt", "a")
# for line in result:
#     natija = b.write(line)
# print(natija)
# a.close()
# b.close()

#14 words.txt faylidagi eng uzun so‘zni toping.
# a = open("words.txt", "r", encoding="utf-8")
# result = a.read().split()
# uzun_soz = ""
# for word in result:
#     if len(word) > len(uzun_soz):
#         uzun_soz = word
# print(f"words.txt file-dagi eng uzun soz: {uzun_soz}, soz uzunligi: {len(uzun_soz)}")
# a.close()

# 15 Statistik hisobot 📊  numbers.txt faylidan:  eng katta son   eng kichik son    o‘rtacha qiymat    hisoblab ekranga chiqaring.

# a = open("numbers.txt", "r", encoding="utf-8")
# result = a.readlines()
# print(f"Eng kichik son: {min(int(i) for i in result)}")
# print(f"Eng katta son: {max(int(i) for i in result)} ")
# print(f"O'rta arifmetik: {sum(int(i) for i in result) / len(result) }")
# a.close()