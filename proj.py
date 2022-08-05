import re


# autor, Senha, IP, email, transação, repositório, Hash
def valida_autor(autor : str): # faltando
    regex = re.compile(r"^[a-zA-Z]\w*")


def valida_senha(senha : str): # acho que ta ok
    regex = re.compile(r"^[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}$")
    correspondencias = regex.search(senha)
    return correspondencias != None

def valida_ip(ip : str): # faltando
    regex = re.compile(r"")

def valida_email(email : str): # faltando
    regex = re.compile(r"^[a-zA-Z][^@]*@.+\..+")


def valida_transacao(transacao : str): # acho que ta ok
    regex = re.compile(r"pull|push|stash|fork|pop")
    correspondencias = regex.search(transacao)
    return correspondencias != None


def valida_repositorio(repositorio : str): #faltando
    regex = re.compile(r"^[a-z0-9]+_*[a-z0-9]+")
    # correspondencias = regex.search(repositorio)
    # print(correspondencias)
    # return correspondencias != None


def valida_hash(hash : str): # acho que ta ok
    regex = re.compile(r"^[a-f0-9]{32}$")
    correspondencias = regex.search(hash)
    return correspondencias != None


valores = input().split(" ")

if len(valores) != 7:
    print(False)

validacoes = []
validacoes.append(valida_senha(valores[1]))
validacoes.append(valida_transacao(valores[4]))
validacoes.append(valida_hash(valores[6]))

if(False in validacoes):
    print(False)
else:
    print(True)