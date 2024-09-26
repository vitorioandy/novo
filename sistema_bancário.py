from datetime import datetime

menu = """
================ Menu ================

[d] Depositar
[s] Sacar
[e] Ver Extrato
[q] Sair

 ========================================


 """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    op= input(menu)
        
    if op == "d":
    
        valor = float(input('insira o valor a ser depositado '))

        if valor > 0:
                
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"+ f"{datetime.now()}\n"

        else: print ('Operação falha, informe o valor corretamente.')        

    elif op == "s":
        valor = float(input('defina o valor do saque: '))

        exc_saq = numero_saque >= LIMITE_SAQUE

        exc_saldo = valor > saldo

        exc_limite = valor > limite   
        if exc_saq: 
            print ("Você excedeu o seu limite de saques por hoje ")

        elif exc_saldo:
            print('Saldo insuficiente, operação cancelada')

        elif exc_limite:
            print('o limite por saque de R$500,00 foi excedido, tente um valor menor ou igual.')        

        elif valor > 0:
            saldo -= valor

            extrato += f"Saque: R$ {valor:.2f}\n"

            numero_saque += 1

        else :
            print ("operação falha, o valor informado é invalido")

    elif op == "e":
        print ("---------extrato----------")

        print ("Não houveram movimentações" if not extrato else extrato)

        print ("===========================")

        print (f"\nSaldo: R$ {saldo:.2f}")

        print (datetime.now() , "\n")    

        print ("============================")


    elif op == "q":
        break

else:
    print ("operação invalida, selecione uma opção do menu")

