from datetime import datetime, date

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
NUMERO_TRANSACAO = 0



while True:
    op= input(menu)
        
    if op == "d":
    
        valor = float(input('insira o valor a ser depositado '))

        if valor > 0:
                
            saldo += valor
            extrato += f"\nData da transaçaõ : {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}\n" + f"\n Valor do Deposito : R$ {valor:.2f}\n" + f"~"*25
            NUMERO_TRANSACAO += 1
            if NUMERO_TRANSACAO >= 10:
                print("Numero limite de Transações diarias alcançado. ")

        else: print ('Operação falha, informe o valor corretamente.')        

    elif op == "s":
        valor = float(input('defina o valor do saque: '))

        exc_saldo = valor > saldo

        exc_limite = valor > limite   
        if exc_saldo:
            print('Saldo insuficiente, operação cancelada')

        elif exc_limite:
            print('o limite por saque de R$500,00 foi excedido, tente um valor menor ou igual.')        

        elif valor > 0:
            saldo -= valor

            extrato += f"\nData da transação : {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}\n" + f"\n Valor do Saque : R$ {valor:.2f}\n" + f"~"*25

            NUMERO_TRANSACAO += 1
            if NUMERO_TRANSACAO >= 10:
                print("Numero limite de Transações diarias alcançado. ")


        else :
            print ("operação falha, o valor informado é invalido")

    elif op == "e":
        print ("---------extrato----------")

        print ("Não houveram movimentações" if not extrato else extrato)

        print ("="*25)

        print (f"\nSaldo: R$ {saldo:.2f}")

        print (datetime.today().strftime('%d/%m/%Y %H:%M:%S'),"\n")  

        print ("="*25)


    else:  print ("operação invalida, selecione uma opção do menu")
    
    if op == "q":
        break
   

