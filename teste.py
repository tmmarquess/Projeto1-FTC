import re

# string = "a testa do teste do testador testou positivo para testão"

# regex = re.compile(r"test")

# print(regex.search(string))
# print(regex.findall(string))
# print(regex.sub('ABC', string))

email = ["thiago.uchoa18@gmail.com.br", "ebgcosta@uea.edu.br", "elloa.uea@gmail.com", "c4rl0s@teste.com.au", "thiago@gmail.com", "1thiago@gmail.com"]

regex = re.compile(r"^[a-zA-Z][^\s]*@.+\..+")
# regex = re.compile(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")

print(regex)
for i in email:
    print(regex.findall(i))


