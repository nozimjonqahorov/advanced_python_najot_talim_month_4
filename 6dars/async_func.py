import asyncio

async def hisobla(son):
    print(f"1chi funksiya {son} ning kvadrati hisoblanmoqda...")
    await asyncio.sleep(0)
    print(f" 1chi funksiya {son} kvadrati = {son**2}")



async def test():
    print(f"2chi funksiya Test ishga tushdi")
    await asyncio.sleep(0)
    print(f"2chi funksiya Test tugadi")


async def test2():
    print(f"3chi funksiya T Test2 ishga tushdi")
    await asyncio.sleep(0)
    print(f"3chi funksiya Test2 tugadi")

async def main():
    # 3 ta vazifani parallel bajarish
    await asyncio.gather(
        hisobla(2),
        test(),
        test2()
    )

asyncio.run(main())