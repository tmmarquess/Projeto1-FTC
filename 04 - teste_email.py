import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

emails = ["mkyong","mkyong@a.com.my" ,"mkyong123@gmail.a" ,"mkyong123@b.com" ,"mkyong123@c.com.com" ,".mkyong@mkyong.com" ,"mkyong.@gmail.com" ,"mkyong@%.com" ,"mkyong..2002@gmail.com" ,"mkyong.@gmail.com" ,"mkyong@mkyong@gmail.com" ,"mkyong@gmail.com.1a", "mkyong@d.com.my.","_lloa@github.com" ,"3lloa@github.com" ,"elloa@ github.com" , "ell@oa@github.com","wallgen@hotmail.com" ,"lbp.7@outlook.com" ,"jessicctavares@outlook.com.br" ,"elloa@github.com" ,"menina.sla@gmail.com.br" ,"melinnediniz@gmail.com.br", "mkyong@d.com.my", "mkyong@dcommy", "mkyong@dcom.my"]

esperado = [False, True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, False, True, True, True, True, True, True, True, False, True]

regex = re.compile(r"^[a-zA-Z](\.*\w*)*@\w+\.[a-zA-Z0-9]+(\.*[a-zA-Z0-9])*$")
i = 0

for email in emails:
    validou = regex.search(email)
    if validou is not None:
        # if esperado[i] == False:
            print(f"{bcolors.OK}"+email + f" passou{bcolors.RESET}", end=" - ")
            print(validou, end=" - ")
            print(esperado[i])
        
    else:
        # if esperado[i] == True:
            print(f"{bcolors.FAIL}"+email + f" não passou{bcolors.RESET}", end=" - ")
            print(esperado[i])

    i += 1

