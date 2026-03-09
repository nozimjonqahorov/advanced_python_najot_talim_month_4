from time import sleep
from multiprocessing import Pool

def hisobla(son):
    print("start")
    sleep(4)          # Kutish shu yerda bo‘lishi kerak
    return son * son

if __name__ == "__main__":
    with Pool(processes=8) as pool:
        natijalar = pool.map(hisobla, range(8))
        print(natijalar)
