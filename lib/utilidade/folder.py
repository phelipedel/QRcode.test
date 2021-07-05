import cor
import os


def verificar(msg):
    while True :
        folder = input ( msg )
        try :
            directory = folder
            parent_dir = 'Nova pasta' #deve adicionar o diretorio que deseja criar pasta
            path = os.path.join ( parent_dir , directory )
            os.mkdir ( path )
        except (FileExistsError ,) :
            directory = os.path.exists ( 'save_qr_code' )
            print ( f'{cor.vermelho}Erro! Diretorio ja existe,  tente novamente.  ' )
        else :

            print ( f'{cor.amarelo}Gerando pasta...' )
            break
    return folder

