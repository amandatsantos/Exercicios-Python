import random 
from time import sleep



input('aperte enter para começar ...')
print('so um segundo... processando... ')
sleep(0.5)
print('...')



while True:
    print('UM NUMERO FOI GERADO DE 0 A 50\nTENTE ACERTAR O NUMERO\n')

    while True:
        numero_sorteado= random.randrange( 0,  50)
        try :
            numero_usuario = int(input('insira um numero no limite de 0 a 50:'))
            
        except (ValueError , NameError):
            print('apenas valores numericos inteiros')
            print()

        else:
            if numero_usuario > 3 :
                print(' ENTRADA INVALIDA !!!! apenas numero dentro do limite de 0 a 50, tente novamente ... ')
               
                break
            elif numero_sorteado == numero_usuario:
                print(f"PARABENS!!!! VOCê ACERTOU! o numero do usuario foi {numero_usuario} e o numero sorteado foi {numero_sorteado} ")
                print()
                break
                
            elif numero_sorteado < numero_usuario:
                print(f'Que pena, não foi dessa vez... o numero chutado pelo usuario é maior que o numero sorteado ... tente novamente')
                print()
                continue
            elif numero_sorteado >  numero_usuario:
                print(f'Que pena, não foi dessa vez... o numero chutado pelo usuario é menor que o numero sorteado ... tente novamente')
                print()
                continue
            else:
                print('entrada invalida, tente novamente')
                break

