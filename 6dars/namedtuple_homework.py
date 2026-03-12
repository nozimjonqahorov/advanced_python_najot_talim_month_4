from collections import namedtuple

Car = namedtuple('Car', ('id', 'model', 'make', 'narxi', "yili"))

all_cars = []

def add_car():
    global all_cars
    cars = []
    while True:
        for field_name in Car._fields:
            obct = input(f"{field_name} ni kiriting: ")
            cars.append(obct)
        break

    new_list = Car._make(cars)
    all_cars.append(new_list)
    print(f"Yangi mashina: {new_list.model} qushildi")


def show_cars():
    if not all_cars:
        print("Hali mashina mavjud emas! ")
    else:    
        for i, car in enumerate(all_cars, 1):
            print(f"{i} chi mashina: nomi: {car.model}, narxi: ${car.narxi}, yili: {car.yili}")

def delete_car(id):
    if not all_cars:
        print("Hali mashina mavjud emas! ")
    else:
        deleted = []
        for car in all_cars:
            if car.id == id.strip():
                all_cars.remove(car)
                deleted.append(car)
                print(f"{id} idli mashina muvaffaqiyatli  uchirildi! ")
        if not deleted:
            print(f"{id} idli mashina topilmadi! ")

def update_car(id):
    updated = False
    for index, car in enumerate(all_cars):
        if id == car.id:
            new_id = input(f"Yangi id- ni kiriting: ")
            new_model = input(f"Yangi model- ni kiriting: ")
            new_make = input(f"Yangi make- ni kiriting: ")
            new_price = input(f"Yangi narx- ni kiriting: ")
            new_year = input(f"Yangi yilini- ni kiriting: ")
            updated_car = car._replace(
                id=new_id, 
                model=new_model, 
                make=new_make, 
                narxi=new_price, 
                yili=new_year
            )
            all_cars[index] = updated_car
            
            print(f"Ma'lumotlar yangilandi!")
            updated = True
            break
    if not updated:
        print(f"Bizda {id}-idli mashina mavjud emas! ")
        
def search_car(id):
    found = False
    for car in all_cars:
        if car.id == id:
            print(f"Ma'lumot topildi\nid: {car.id}, modeli: {car.model}, make: {car.make}, narxi: {car.narxi}, yili: {car.yili}")
            found = True  
    if not found:
        print(f"Bizda {id}-idli mashina mavjud emas! ")

                

menu = "1- Mashinalarni ko'rish\n2- Mashina qushish\n3-Mashinani uchirish\n4-Mashina qidirish\n5-Mashina ma'lumotlarini yangilsh\n0-Chiqish\n>>"

while True:
    u = int(input(f"Menudan amalni tanlang:\n{menu}"))
    if u == 1:
        show_cars()
    elif u == 2:
        add_car()
    elif u == 3:
        if not all_cars:
           print("Hali mashina mavjud emas")
        else:
           user = input("Uchirish uchun mashina id-sini kiriting: ")
           delete_car(user)
    elif u == 4:
        if not all_cars:
           print("Hali mashina mavjud emas")
        else:
            user = input("Ma'lumotlarni ko'rish uchun mashina id-sini kiriting: ")
            search_car(user)
    elif u == 5:
        if not all_cars:
           print("Hali mashina mavjud emas")
        else:
           user = input("Ma'lumotlarni yangilash uchun mashina id-sini kiriting: ")
           update_car(user)
    elif u == 0:
        break       
    else:
        continue
    

