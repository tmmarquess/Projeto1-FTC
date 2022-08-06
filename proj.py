import re


# autor, Senha, IP, email, transação, repositório, Hash
def valida_autor(autor: str):  # acho que ta ok
    regex_geral = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*$")
    regex_letras = re.compile(r"[a-zA-Z]")
    regex_numeros = re.compile(r"[0-9]")

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
        return False
    else:
        return True


def valida_senha(senha: str):  # acho que ta ok
    regex_geral = re.compile(r"^[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}$")
    regex_repeticao = re.compile(r"(.)\1")
    regex_letras = re.compile(r"[A-F][A-F]")

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
        return False
    else:
        return True


def valida_ip(ip: str):  # acho que ta ok
    regex_geral = re.compile(r"^[12]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}\.[0-2]?[0-9]{0,2}$")
    regex_problemas = re.compile(r"^0|^127|^255|255$|0$")

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
        return False
    else:
        return True


def valida_email(email: str):  # faltando
    regex = re.compile(r"^[a-zA-Z][^@()*]*@.+\..+")


def valida_transacao(transacao: str):  # acho que ta ok
    regex = re.compile(r"^pull$|^push$|^stash$|^fork$|^pop$")
    correspondencias = regex.search(transacao)
    return correspondencias != None


def valida_repositorio(repositorio: str):  # acho que ta ok
    regex = re.compile(r"^[a-z]+(_?[a-z0-9])*$")
    if regex.search(repositorio) != None:
        return True
    else:
        return False


def valida_hash(hash: str):  # acho que ta ok
    regex = re.compile(r"^[a-f0-9]{32}$")
    if regex.search(hash) != None:
        return True
    else:
        return False


valores = input().split()

if len(valores) != 7:
    print(False)

validacoes = []
validacoes.append(valida_autor(valores[0]))
validacoes.append(valida_senha(valores[1]))
validacoes.append(valida_ip(valores[2]))
# validacoes.append(valida_email(valores[3]))
validacoes.append(valida_transacao(valores[4]))
validacoes.append(valida_repositorio(valores[5]))
validacoes.append(valida_hash(valores[6]))

if False in validacoes:
    print(False)
else:
    print(True)
