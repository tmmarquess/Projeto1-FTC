import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

repositorios = ["zooctec_tcc","biomassa_da_banana" ,"ftc_projeto" ,"dominar" ,"dominar_o_mundo" ,"projeto_de_ftc" ,"projeto__ftc" ,"projeto_ftc","dominar.o.mundo" ,"dominar-o-mundo", "dominar_o_mundo_", "a", 'aa']

regex_geral = re.compile(r"^[a-z]+(_*[a-z0-9])*$")

for repo in repositorios:
    resposta = regex_geral.search(repo)

    if resposta == None:
        print(f"{bcolors.FAIL}"+repo + f" não passou{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}"+repo + f" passou{bcolors.RESET}")