from pypresence import Presence
import time
import random
import ctypes
import json
import requests
import os

ctypes.windll.kernel32.SetConsoleTitleW("CatRPC by uwue")

# Set the Client ID
cid = int(820573529438289940)
rpc = Presence(cid)
rpc.connect()

cats = (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14)

loops = 0

# RPC Loop
while True:

    data = requests.get('https://catfact.ninja/fact')
    cat_fact = data.json()["fact"]
    random_cat = random.choice(cats)
    rpc.update(small_image = 'cat', large_image = str(random_cat), small_text= 'another cat!', large_text= str(cat_fact)[:128])
    print('Looped ' + str(loops) + ' times!')
    loops = loops+1
    time.sleep(10)
    os.system('cls')
