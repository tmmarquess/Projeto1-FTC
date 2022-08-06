import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

emails = ['mkyong', 'mkyong@.com.my', 'mkyong123@gmail.a', 'mkyong123@.com', 'mkyong123@.com.com', '.mkyong@mkyong.com', 'mkyong()*@gmail.com', 'mkyong@%*.com', 'mkyong..2002@gmail.com', 'mkyong.@gmail.com', 'mkyong@mkyong@gmail.com', 'mkyong@gmail.com.1a']


# regex = re.compile(r"^[a-zA-Z]")
regex = re.compile(r"^[a-zA-Z][]")

for email in emails:
    validou = regex.search(email)
    if validou is not None:
        print(f"{bcolors.OK}"+email + f" passou{bcolors.RESET}", end=" - ")
        print(validou)
    else:
        print(f"{bcolors.FAIL}"+email + f" não passou{bcolors.RESET}")


'''
mkyong
False
mkyong@.com.my
True
mkyong123@gmail.a
True
mkyong123@.com
True
mkyong123@.com.com
True
.mkyong@mkyong.com
False
mkyong()@gmail.com
True
mkyong@%.com
False
mkyong..2002@gmail.com
True
mkyong.@gmail.com
True
mkyong@mkyong@gmail.com
False
mkyong@gmail.com.1a
True
'''