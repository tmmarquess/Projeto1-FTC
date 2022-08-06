import re
from tkinter.messagebox import NO

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

hashes = ["cdc9686d54357c334748d80ea05c6723","57dad741117fa87011e8d54796133f0e" ,"fbec6dc5c0d5f894e4410ec0cd8645a1" ,"e25df22a1b41ec5248f5af0d8fb1c2dd" ,"e25df22a1b41ec5248f5af0d8fb1c2dj","e25df22a1b41ec5248f5af0d8fb1c2d" ,"e25df22a1b41ec5248f5af0d8fb1c2dd0" ,"e25df22a1b41ec5248f5af0d8fb1cddd", "e25df22a1b41ec5248f5af0d8fb1cdda", "e25df22a1b41ec5248f5af0d8fb1c2dj"]

regex = re.compile(r"^[a-f0-9]{32}$")

for hash in hashes:
    if regex.search(hash) != None:
        resposta = True
    else:
        resposta = False

    if resposta is False:
        print(f"{bcolors.FAIL}"+hash + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+hash + f" passou{bcolors.RESET}")
