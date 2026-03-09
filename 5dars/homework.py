import threading
import queue
from multiprocessing import Queue, Process, Pool
import math

"""1.  1 dan 100 gacha sonlarni chiqarish Ikki ta thread yarating: 1-thread
    1 dan 50 gacha sonlarni chiqarsin. 2-thread 51 dan 100 gacha
    sonlarni chiqarsin."""

# def show_numbers(n1, n2):
#     for i in range(n1, n2):
#         print(i)

# t1 = threading.Thread(target = show_numbers, args = (1, 51))
# t2 = threading.Thread(target = show_numbers, args = (51, 101))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

"""2.  Juft va toq sonlar Ikki thread yarating: Biri juft sonlarni
    chiqarsin. Biri toq sonlarni chiqarsin. Range: 1 dan 100 gacha."""

# def show_even_odd_numbers(n, even):
#     if even:
#         for i in range(1, n + 1):
#             if i % 2 == 0:
#                 print(i)
#     else:
#         for i in range(1, n + 1):
#             if i % 2 == 1:
#                 print(i)

# t1 = threading.Thread(target =show_even_odd_numbers, args = (100, True))
# t2 = threading.Thread(target =show_even_odd_numbers, args = (100, False))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

"""3.  Sonlar yig‘indisi List beriladi: nums = [1,2,3,4,5,6,7,8,9,10] 2
    thread yarating: 1-thread listning birinchi yarmini yig‘indisini
    hisoblasin. 2-thread listning ikkinchi yarmini yig‘indisini
    hisoblasin. Oxirida umumiy yig‘indini toping.
"""

# nums = [1,2,3,4,5,6,7,8,9,10]

# def sum_numbers(lst, q):
#     q.put(sum(lst))

# q = queue.Queue()

# t1 = threading.Thread(target =sum_numbers, args = (nums[:len(nums) // 2], q))
# t2 = threading.Thread(target =sum_numbers, args = (nums[len(nums) // 2: ], q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(natija1 + natija2)

"""4.  Faktorial hisoblash Ikki thread yarating: Biri 5 faktorialni
    hisoblasin. Biri 7 faktorialni hisoblasin."""

# def factorial_n(n):
#     print(math.factorial(n))

# t1 = threading.Thread(target =factorial_n, args = (5, ))
# t2 = threading.Thread(target =factorial_n, args = (7, ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

"""5.  Matndagi harflarni sanash Matn beriladi: text = “python
    multithreading” 2 thread yarating: Biri unli harflar sonini
    hisoblasin. Biri undosh harflar sonini hisoblasin."""

# def check_length_vowel_con(text:str, vowel:bool):
#     unli = ["a", "u", "i", "o", "e", "o'"]
#     new_text = ''
#     if vowel:
#         for i in text:
#             if i in unli:
#                 new_text += i

#         print(f"Matndagi unlilar soni: {len(new_text)}")
#     else:
#         for i in text:
#             if i not in unli:
#                 new_text += i
#         print(f"Matndagi undosh;ar soni: {len(new_text)}")

# t1 = threading.Thread(target = check_length_vowel_con, args = ("matn",True ))
# t2 = threading.Thread(target = check_length_vowel_con, args = ("matn",False ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


"""6.  Listdagi eng katta son List: [23,54,12,76,89,33,45,90] 2 thread
    yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
    yarmini tekshiradi. Oxirida eng katta sonni toping."""

# nums = [23,54,12,76,89,33,45,90]

# def max_numbers(lst, q):
#     q.put(max(lst))

# q = queue.Queue()

# t1 = threading.Thread(target =max_numbers, args = (nums[:len(nums) // 2], q))
# t2 = threading.Thread(target =max_numbers, args = (nums[len(nums) // 2: ], q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(max(natija1, natija2))

"""7.  Listni sort qilish List: [34,12,76,23,89,11,90,45] 2 process
    yarating: Har biri listning yarmini sort qiladi. Keyin natijalar
    birlashtiriladi."""

# nums = [34,12,76,23,89,11,90,45]

# def sort_numbers(lst, q):
#     q.put(sorted(lst))

# q = queue.Queue()

# t1 = threading.Thread(target =sort_numbers, args = (nums[:len(nums) // 2], q))
# t2 = threading.Thread(target =sort_numbers, args = (nums[len(nums) // 2: ], q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(sorted(natija1 + natija2))

"""8.  Tub sonlarni topish 1 dan 100 gacha tub sonlarni toping. 1-thread 1
    dan 50 gacha tekshiradi. 2-thread 51 dan 100 gacha tekshiradi."""

# q = queue.Queue()

# def is_prime(num):
#     if num < 2: return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def tub_sonlar_top(n1, n2, q):
#     tub_list = []
#     for i in range(n1, n2 + 1):
#         if is_prime(i):
#             tub_list.append(i)
#     q.put(tub_list)

# t1 = threading.Thread(target=tub_sonlar_top, args=(1, 50, q))
# t2 = threading.Thread(target=tub_sonlar_top, args=(51, 100, q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(f"1-thread topgan tub sonlar soni: {natija1}")
# print(f"2-thread topgan tub sonlar soni:{natija2}")
# print(f"Barcha topilgan sonlar: {natija1 + natija2}")


"""9.  Stringlarni katta harfga o‘tkazish List:
    [“python”,“django”,“fastapi”,“backend”] 2 thread yarating: Biri
    birinchi 2 elementni upper qiladi. Biri qolgan elementlarni upper
    qiladi."""

# words = ["python","django","fastapi","backend"]

# def upper_words(lst, q):
#     new_list = []
#     for i in lst:
#         new_list.append(i.upper())

#     q.put(new_list)
# q = queue.Queue()

# t1 = threading.Thread(target = upper_words, args = (words[:len(words) // 2], q))
# t2 = threading.Thread(target = upper_words, args = (words[len(words) // 2: ], q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(f"1-thread natijasi: {natija1}")
# print(f"2-thread natijasi:{natija2}")
# print(natija1 + natija2)

"""10. Palindrom tekshirish List: [“level”,“python”,“radar”,“hello”] 2
    thread yarating: Biri birinchi 2 so‘zni tekshiradi. Biri qolgan 2
    so‘zni tekshiradi. Har bir so‘z palindrom yoki yo‘qligini aniqlang."""

# words = ["level", "python", "radar", "hello"]

# def check_palindrome(lst, q):
#     new_list = []
#     for i in lst:
#         if i == i[::-1]:
#             new_list.append(i)

#     q.put(new_list)
# q = queue.Queue()

# t1 = threading.Thread(target = check_palindrome, args = (words[:len(words) // 2], q))
# t2 = threading.Thread(target = check_palindrome, args = (words[len(words) // 2: ], q))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# natija1 = q.get()
# natija2 = q.get()

# print(f"1-thread natijasi: {natija1}")
# print(f"2-thread natijasi:{natija2}")
# print(natija1 + natija2)

#######################################################################################################################################
#######################################################################################################################################

#      MultiProcessing bo‘yicha 10 ta masala 


"""1.  1 dan N gacha yig‘indi 2 ta process yarating: Biri 1 dan 500_000
    gacha sonlar yig‘indisini hisoblasin. Biri 500001 dan 1000000 gacha
    sonlar yig‘indisini hisoblasin."""

# def sum_numbers(n1, n2, q):    
#     total = sum(range(n1, n2 + 1))
#     q.put(total)

# if __name__ == "__main__":
#     q = Queue() 

#     p1 = Process(target=sum_numbers, args=(1, 500_000, q))
#     p2 = Process(target=sum_numbers, args=(500_001, 1_000_000, q))

#     p1.start()
#     p2.start()

#     natija1 = q.get()
#     natija2 = q.get()

#     p1.join()
#     p2.join()

#     print(f"Jami yig'indi: {natija1 + natija2}")


# def calc_sum(numbers):
#     return sum(numbers)

# if __name__ == "__main__":

#     tasks = [range(1, 500_001), range(500_001, 1_000_001)]
    
#     with Pool(processes=2) as pool:
#         results = pool.map(calc_sum, tasks)
    
#     print(f"Natijalar: {results}")
#     print(f"Umumiy summa: {sum(results)}")

"""2.  Faktorial 2 ta process yarating: Biri 10 faktorialni hisoblasin.
    Biri 12 faktorialni hisoblasin"""

# def fact(n):
#     return math.factorial(n)

# if __name__ == "__main__":

#     tasks = [10, 12]
    
#     with Pool(processes=2) as pool:
#         results = pool.map(fact, tasks)
    
#     print(f"Natijalar: {results}")
   

"""3.  Tub sonlarni topish 1 dan 10000 gacha tub sonlarni toping. 1-process
    1 dan 5000 gacha tekshiradi. 2-process 5001 dan 10000 gacha
    tekshiradi."""

# def is_prime(num):
#     if num < 2: return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def tub_sonlar_top(n1, n2, q):
#     tub_list = []
#     for i in range(n1, n2 + 1):
#         if is_prime(i):
#             tub_list.append(i)
#     q.put(tub_list) 

# if __name__ == "__main__":
#     q = Queue() 

#     p1 = Process(target=tub_sonlar_top, args=(1, 5000, q))
#     p2 = Process(target=tub_sonlar_top, args=(5001, 10_000, q))

#     p1.start()
#     p2.start()

#     natija1 = q.get()
#     natija2 = q.get()

#     p1.join()
#     p2.join()

#     print(f"1-chi process javobi: {natija1}")
#     print(f"2-chi process javobi: {natija2}")
#     print(f"Umumiy: {natija1 + natija2}")

"""4.  Fibonacci 2 ta process yarating: Biri Fibonacci(30) ni hisoblasin.
    Biri Fibonacci(35) ni hisoblasin."""
# def fibonacci(n):
#     a, b = 0, 1
#     result = []
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result


# if __name__ == "__main__":

#     tasks = [30, 35]
    
#     with Pool(processes=2) as pool:
#         results = pool.map(fibonacci, tasks)
    
#     print(f"Natijalar: {results}")


"""5.  Eng katta sonni topish List: [12,45,67,23,89,90,34,22] 2 process
    yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
    yarmini tekshiradi. Oxirida eng katta sonni toping."""

# nums = [12,45,67,23,89,90,34,22]

# def max_number(lst):
#     return max(lst)

# if __name__ == "__main__":

#     tasks = [nums[:len(nums) // 2], nums[len(nums) // 2:]]
#     with Pool(processes=2) as pool:
#         results = pool.map(max_number, tasks)


#     print(f"1-chi process natijasi: {results[0]}")
#     print(f"2-chi process natijasi: {results[1]}")
#     print(f"Umumiy natija: {max(results)}")

"""# 6.  Kvadratlar yig‘indisi 1 dan 100000 gacha sonlarning kvadratlari
#     yig‘indisini hisoblang. 2 process yarating: Biri 1 dan 50000 gacha
#     hisoblaydi. Biri 50001 dan 100000 gacha hisoblaydi.
"""

# def sum_square_num(numbers):
#     return sum(i**2 for i in numbers)

# if __name__ == "__main__":

#     tasks = [range(1, 50_001), range(50_001, 100_001)]
    
#     with Pool(processes=2) as pool:
#         results = pool.map(sum_square_num, tasks)
    
#     print(f"Natijalar: {results}")
#     print(f"Umumiy summa: {sum(results)}")

"""7.  Listni sort qilish List: [34,12,76,23,89,11,90,45] 2 process
    yarating: Har biri listning yarmini sort qiladi. Keyin natijalar
    birlashtiriladi.
"""
# nums = [34,12,76,23,89,11,90,45]

# def sort_numbers(lst):
#     return sorted(lst)

# if __name__ == "__main__":

#     tasks = [nums[:len(nums) // 2], nums[len(nums) // 2:]]
#     with Pool(processes=2) as pool:
#         results = pool.map(sort_numbers, tasks)


#     print(f"1-chi process natijasi: {results[0]}")
#     print(f"2-chi process natijasi: {results[1]}")


"""8.  Digit yig‘indisi Katta sonlar listi: [123456, 987654, 567890,
    345678] 2 process yarating: Har biri listning yarmini ishlaydi. Har
    sonning raqamlari yig‘indisini toping."""


# sonlar = [123456, 987654, 567890,345678]

# def str_summa(text):
#     summa = 0
#     for i in str(text):
#         summa += int(i)
     
#     return summa

# def map_result(sonlar):
#     return list(map(lambda x: str_summa(x),sonlar))

# if __name__ == "__main__":

#     tasks = [sonlar[:len(sonlar) // 2], sonlar[len(sonlar) // 2:]]
#     with Pool(processes=2) as pool:
#         results = pool.map(map_result, tasks)


#     print(f"1-chi process natijasi: {results[0]}")
#     print(f"2-chi process natijasi: {results[1]}")

"""9.  Eng kichik sonni topish List: [45,23,67,12,89,34,10] 2 process
    yarating: Biri listning birinchi yarmini tekshiradi. Biri ikkinchi
    yarmini tekshiradi. Oxirida eng kichik sonni toping."""

# nums = [45,23,67,12,89,34,10]

# def min_number(numbers:list):
#     return min(numbers)

# if __name__ == "__main__":

#     tasks = [nums[:len(nums) // 2], nums[len(nums) // 2:]]
#     with Pool(processes=2) as pool:
#         results = pool.map(min_number, tasks)


#     print(f"1-chi process natijasi: {results[0]}")
#     print(f"2-chi process natijasi: {results[1]}")

"""10. Tub sonlar sonini hisoblash 1 dan 20000 gacha nechta tub son
    borligini toping. 2 process yarating: 1-process 1 dan 10000 gacha
    tekshiradi. 2-process 10001 dan 20000 gacha tekshiradi."""

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def tub_sonlar_top(n1, n2, q):
    tub_list = []
    for i in range(n1, n2 + 1):
        if is_prime(i):
            tub_list.append(i)
    q.put(tub_list) 

if __name__ == "__main__":
    q = Queue() 

    p1 = Process(target=tub_sonlar_top, args=(1, 10000, q))
    p2 = Process(target=tub_sonlar_top, args=(10_001, 20_000, q))

    p1.start()
    p2.start()

    natija1 = q.get()
    natija2 = q.get()

    p1.join()
    p2.join()

    print(f"1-chi process javobi: {len(natija1)}")
    print(f"2-chi process javobi: {len(natija2)}")
    print(f"Umumiy: {len(natija1 + natija2)}")
