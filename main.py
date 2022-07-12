from pystyle import *
import os
import ctypes
import requests
import keep_alive
import random
import string
import time


print(Colorate.Horizontal(Colors.blue_to_red, """


███████╗████████╗ █████╗ ██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║████╗  ██║██║ ██╔╝
███████╗   ██║   ███████║██████╔╝██║     ██║██╔██╗ ██║█████╔╝ 
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║╚██╗██║██╔═██╗ 
███████║   ██║   ██║  ██║██║  ██║███████╗██║██║ ╚████║██║  ██╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                              
   
                                                                                        
"""))
print(Colorate.Horizontal(Colors.blue_to_red,"Version 2 : Advanced checker and generator"))
time.sleep(0.1)
print(Colorate.Horizontal(Colors.blue_to_red,"Discord Nitro Generator and Checker"))
time.sleep(0.1)
print(Colorate.Horizontal(Colors.blue_to_red,"Good Luck..\n"))
time.sleep(0.1)

num = int(input(Colorate.Horizontal(Colors.blue_to_red,'Input How Many Codes to Generate and Check: ')))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print(Colorate.Horizontal(Colors.blue_to_red, "Your nitro codes are being generated, be patient if you have entered a high number!"))
    

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(Colorate.Horizontal(Colors.blue_to_red,f"Generating {num} codes...\n"))

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Colorate.Horizontal(Colors.blue_to_red, f" Valid | {nitro} "))
            break
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, f" Invalid | {nitro} "))




time.sleep(0.2)

print(Colorate.Horizontal(Colors.blue_to_red, f"You Have generated {num} codes. | Time taken: {time.time() - start}\n"))
input(Colorate.Horizontal(Colors.blue_to_red, f"To Keep Alive, enter a number: \n"))

keep_alive.keep_alive()

