import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

transacoes = ["pull","push" ,"stash" ,"fork" ,"pop", "pusho" ,"pus" ,"plof", "ofork"]

regex = re.compile(r"^pull$|^push$|^stash$|^fork$|^pop$")

for tran in transacoes:
    resp = regex.search(tran)

    if resp == None:
        print(f"{bcolors.FAIL}"+tran + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+tran + f" passou{bcolors.RESET}")