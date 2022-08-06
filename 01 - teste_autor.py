import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

autores = ["elloa", "jessicaLopes", "ell04", "el104h", "elloaBGuedes", "Elloa", "3ll04", "3lloa", "el104"]
# autores = ["elloa", "jessicaLopes", "ell04", "el104h", "elloaBGuedes", "Elloa"]

regex_geral = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*$")
regex_letras = re.compile(r"[a-zA-Z]")
regex_numeros = re.compile(r"[0-9]")

for autor in autores:
    respostas = []
    if regex_geral.search(autor) != None:
        respostas.append(True)
    else:
        respostas.append(False)
    
    if len(regex_letras.findall(autor)) >= len(regex_numeros.findall(autor)):
        respostas.append(True)
    else:
        respostas.append(False)

    if False in respostas:
        print(f"{bcolors.FAIL}"+autor + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+autor + f" passou{bcolors.RESET}")