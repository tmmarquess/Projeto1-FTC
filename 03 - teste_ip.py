import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

ips = ["0", "192.168.0.1.5.6", "1.", "1", "0.168.0.1", "127.168.0.1", "255.168.0.1", "192.255.255.255", "192.168.255.255", "192.0.0.0", "192.168.0.0", "192.168.0.255", "192.168.1.0", "192.168.0.1", "192.255.0.1", "192.0.0.1", "192.255.255.1""158.208.189.45" ,"126.1.12.34" ,"208.183.34.89" ,"192.168.11.0" ,"255.168.11.0" ,"1.0.0.0" ,"255.168.11.0" ,"255.1.1.0" ,"255.168.11.0" ,"1.1.1.0" ,"1.0.0.0", "158.208.189.45" ,"126.1.12.34" ,"208.183.34.89" ,"192.168.11.0" ,"255.168.11.0" ,"1.0.0.0" ,"255.168.11.0" ,"255.1.1.0" ,"255.168.11.0" ,"1.1.1.0" ,"1.0.0.0"]

regex_geral = re.compile(r"^[12]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}$")
regex_problemas = re.compile(r"^0|^127|^255|255$|0$")

for ip in ips:
    respostas = []
    if regex_geral.search(ip) != None:
        respostas.append(True)
    else:
        respostas.append(False)

    if regex_problemas.search(ip) == None:
        respostas.append(True)
    else:
        respostas.append(False)

    if False in respostas:
        print(f"{bcolors.FAIL}"+ip + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+ip + f" passou{bcolors.RESET}")