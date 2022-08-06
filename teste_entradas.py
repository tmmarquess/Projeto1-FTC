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
    regex_problemas = re.compile(r"^0|^127|^255|255$")

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


def valida_email(email: str):  # acho que ta ok
    regex = re.compile(r"^[a-zA-Z](\.*\w*)*@\w+\.[a-zA-Z0-9]+(\.*[a-zA-Z0-9])*$")
    correspondencia = regex.search(email)
    return correspondencia is not None


def valida_transacao(transacao: str):  # acho que ta ok
    regex = re.compile(r"^pull$|^push$|^stash$|^fork$|^pop$")
    correspondencias = regex.search(transacao)
    return correspondencias is not None


def valida_repositorio(repositorio: str):  # acho que ta ok
    regex = re.compile(r"^[a-z]+(_*[a-z0-9])*$")
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


entradas = [
    "wallace2017 E2.56.32.A8 158.208.189.45 wallgen@hotmail.com pull zooctec_tcc cdc9686d54357c334748d80ea05c6723",
    "Let1c14 10.A4.6B.54 126.1.12.34 lbp.7@outlook.com pull biomassa_da_banana 57dad741117fa87011e8d54796133f0e",
    "jessicctavares A3.67.12.C0 208.183.34.89 jessicctavares@outlook.com.br push ftc_projeto fbec6dc5c0d5f894e4410ec0cd8645a1",
    "elloa A6.B7.C8.F5 192.168.11.0 elloa@github.com push dominar e25df22a1b41ec5248f5af0d8fb1c2dd",
    "ell04 A6.B7.C8.F9 192.168.11.0 elloa@github.com push dominar_o_mundo e25df22a1b41ec5248f5af0d8fb1c2dd",
    "m3l1nn3 03.A5.2B.F8 254.168.11.0 menina.sla@gmail.com.br push projeto_de_ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 A6.B7.F1.C8 1.0.0.0 melinnediniz@gmail.com.br stash projeto__ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 A6.B7.F2.C1 254.168.11.0 melinnediniz@gmail.com.br fork projeto_ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 A6.B7.F4.C5 254.1.1.0 melinnediniz@gmail.com.br pop projeto_ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 14.35.28.92 254.168.11.0 melinnediniz@gmail.com.br pull projeto_ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 A1.12.F5.C7 1.1.1.0 melinnediniz@gmail.com.br pop projeto_ftc cdc9686d54357c334748d80ea05c6723",
    "m3l1nn3 A6.B7.F4.C5 1.0.0.0 melinnediniz@gmail.com.br pop projeto_ftc cdc9686d54357c334748d80ea05c6723",
]
i = 1
for entrada in entradas:
    valores = entrada.split()

    if len(valores) != 7:
        print(False)

    # print(f"Caso {i}:")
    i += 1

    validacoes = []
    validacoes.append(valida_autor(valores[0]))
    # print(f"Autor: {validacoes[0]}")
    validacoes.append(valida_senha(valores[1]))
    # print(f"senha: {validacoes[1]}")
    validacoes.append(valida_ip(valores[2]))
    # print(f"ip: {validacoes[2]}")
    validacoes.append(valida_email(valores[3]))
    # print(f"email: {validacoes[3]}")
    validacoes.append(valida_transacao(valores[4]))
    # print(f"transacao: {validacoes[4]}")
    validacoes.append(valida_repositorio(valores[5]))
    # print(f"repo: {validacoes[5]}")
    validacoes.append(valida_hash(valores[6]))
    # print(f"hash: {validacoes[6]}")

    if False in validacoes:
        print(False)
    else:
        print(True)
