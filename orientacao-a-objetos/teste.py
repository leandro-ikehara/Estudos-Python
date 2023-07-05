

def cria_conta(numero, titular, saldo, limite):
    conta = {"conta": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo: {}".format(conta["saldo"]))