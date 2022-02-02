
import random
from palavras import *
import string




def palavra_valida(palavras):
    palavra = random.choice(palavras)  # escolher aleatoriamente alguma palavra da lista
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()


def forca():
    palavra = palavra_valida(palavras)
    palavra_letras = set(palavra)  #letras dentro de cada palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  # palpites para o usuario

    vidas = 7
    #obtenção da entrada do usuario
    while len(palavra_letras) > 0 and vidas> 0:
        # letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print()
        print('Você têm', vidas, 'vidas : ', ' '.join(letras_usadas))

        #que palavra atual é (ie P - L A V R - )
        palavra_list = [letra if letra in letras_usadas else '-' for letra in palavra]
        print()
        print('palavra atual é : ', ' '.join(palavra_list))

        letra_usuario = input('palpite de letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in palavra_letras:
                palavra_letras.remove(letra_usuario)
                print('')

            else:
                vidas = vidas - 1  # tira uma caso a letra esteja errada
                #print(f'\nSua letra,{ letra_usuario} não faz parte da palavra. {lives_visual_dict[vidasalt]} ')
                if  vidas == 1 :print(f"""
                            ___________
                        | /        | 
                        |/        ( )
                        |          |
                        |         / 
                        |
                        \nSua letra, {letra_usuario}' não faz parte da palavra.""")
                    

                elif  vidas == 2 :print(f"""
                            ___________
                        | /        | 
                        |/        ( )
                        |          |
                        |          
                        |
                        \nSua letra,{ letra_usuario} não faz parte da palavra.""")
                    
                elif  vidas == 3 :print(f"""
                            ___________
                        | /        | 
                        |/        ( )
                        |          
                        |          
                        |
                        
                        \nSua letra,{ letra_usuario} não faz parte da palavra.""")
                

                elif vidas == 4: print(f"""
                            ___________
                        | /        | 
                        |/        
                        |          
                        |          
                        |
                        \nSua letra,{ letra_usuario} não faz parte da palavra.""")
                

                elif vidas == 5 :print(f"""
                            ___________
                        | /        
                        |/        
                        |          
                        |          
                        |
                        \nSua letra,{ letra_usuario} não faz parte da palavra.""")
                
                elif vidas == 6:
                        print(f"""
                        |
                        |
                        |
                        |
                        |
                        \nSua letra,{letra_usuario} não faz parte da palavra""")
                                
            
        elif letra_usuario in letras_usadas:
            print()
            print('\n já usou esta letra, tente outra.')

        else:
            print()
            print(f'\nnão é uma letra valida.')


    if vidas == 0:print(f"""
                        ___________
                    | /        | 
                    |/        ( )
                    |          |
                    |         / \\
                    |'
                    'que droga, você morreu ... a palavra era :'{palavra}'""") 
                    
    else:
        print()
        print(f'PARABÉSN ¹!!!! ACERTOU A PALAVRA !!! ! "{ palavra}" !!')
        
        
        
input()


if __name__ == '__main__':
    while True:
            forca()
            input()

   