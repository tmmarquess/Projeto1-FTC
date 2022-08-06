import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

senhas = ["A6.B7.C8.F9", "A6.B7.C8.FF", "A3.67.12.C0", "E2.56.32.A8", "10.A4.6B.54", "A6.B7.C8.F9.A6.B7.C8.F9", "AB.B7.C8.F2", "33.67.12.C0", "43.67.12.C0","AA.B7.C8.FF" ,"A5.B7.C8.F3.75" ,"A6.BB.C8.F9" ,"A6.B7C8.F9"]

regex_geral = re.compile(r"^[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}$")
regex_repeticao = re.compile(r"(.)\1")
regex_letras = re.compile(r"[A-F][A-F]")

for senha in senhas:
    respostas = []
    if regex_geral.search(senha) != None:
        respostas.append(True)
    else:
        respostas.append(False)

    if regex_repeticao.search(senha) == None:
        respostas.append(True)
    else:
        respostas.append(False)

    if regex_letras.search(senha) == None:
        respostas.append(True)
    else:
        respostas.append(False)

    if False in respostas:
        print(f"{bcolors.FAIL}"+senha + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+senha + f" passou{bcolors.RESET}")