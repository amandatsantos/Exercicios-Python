import random
from time import sleep 


print('\nPEDRA PAPEL TESOURA \njogue contra o bot e veja quem ganha\n')
usuario = input ('insira o seu nome para jogar:\n')
opcao = input(f'{usuario} deseja jogar ? sim - 1  não - 2:\n')

while True:
    if opcao == '1':
        while True:

            entrada_usuario = input('\nESCOLHA: pedra, papel, tesoura :\n').strip().upper()

            if entrada_usuario != 'PEDRA' and entrada_usuario != 'TESOURA' and entrada_usuario!= 'PAPEL':
                print('digitou algo de errado tente novamente')
                continue
            else:
                dados = random.choice(['pedra','papel','tesoura']).upper()
                print('aguarde um momento, processando ...\n')
                sleep(0.5)

                print (f'O BOT ESCOLHEU -> {dados} x {entrada_usuario} <- {usuario} ESCOLHEU')

            while True:

                if entrada_usuario == dados:
                    print(f'EMPATE¹!!!! você e o bot empataram\n')
                    break


                elif entrada_usuario == 'TESOURA' and  dados =='PEDRA' :
                    print(f'o BOT ganhou\n ')
                    break
                elif entrada_usuario == 'PAPEL' and  dados == 'TESOURA' :
                    print(f'BOT ganhou\n ')  
                    break  
                elif entrada_usuario == 'PEDRA' and  dados == 'PAPEL' :
                    print(f'BOT ganhou\n ')
                    break


                elif dados == 'TESOURA' and  entrada_usuario =='PEDRA' :
                    print(f'{usuario} ganhou\n ')
                    break
                elif dados == 'PAPEL' and  entrada_usuario == 'TESOURA' :
                    print(f'{usuario} ganhou\n ')   
                    break 
                elif dados == 'PEDRA' and  entrada_usuario == 'PAPEL' :
                    print(f'{usuario} ganhou\n ')
                    break



    elif opcao == '2':

              print('finalizando ...') 
              sleep(0.5)     
    else:
        print('opção invalida, tente novamente')

    print('fim do programa')
    break
