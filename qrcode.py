import pyqrcode
import png
from pyqrcode import QRCode
from lib.utilidade import cor
from time import sleep
import os
import shutil
from tkinter import filedialog, messagebox
from pathlib import Path
from errno import *

from PIL import Image  # PIP INSTALL PILLOW

# nomeando arquivo
s = input ( str ( f'{cor.azul}Qual site quer gerar qrcode?' ) )

# gerando QR CODE
url = pyqrcode.create ( s )

# setando nomes
nome = input ( str ( f'{cor.azul}Nome do arquivo ' ) )
sleep ( 0.5 )
print ( f'{cor.amarelo}Gerando {nome} QRcode' )
sleep ( 0.5 )


#criando pasta por cada codigo gerado
while True:
    folder = input('Nome da pasta: ')
    try:
        directory = folder
        parent_dir = 'save_qr_code'
        path = os.path.join ( parent_dir , directory )
        os.mkdir ( path )
    except (FileExistsError ,) :
        directory = os.path.exists ( 'save_qr_code' )
        print ( f'{cor.vermelho}Erro! Diretorio ja existe,  tente novamente.  ' )
    else :

        print ( f'{cor.amarelo}Gerando pasta...' )
        break

# criando e salvando arquivo QR

url.svg ( f'{nome}.svg' , scale = 8 )
print ( f'{cor.verde}QRcode .svg gerado com sucesso. ' )
sleep ( 1 )

url.png ( f'{nome}.png' , scale = 6 )
print ( f'{cor.verde}QRcode .png gerado com sucesso. ' )
sleep ( 1 )


r = messagebox.askyesno(title='Adiconar logo?', message='Quer adicioanr um logo ao seu codigo QR?')
if r == True :
    print ( f'{cor.vermelho}Selecione o codigo QR.' )
    origem = filedialog.askopenfilename ( )  # seletor codigo qr
    im = Image.open ( f'{origem}' )
    im = im.convert ( 'RGBA' )
    width , height = im.size
    logo_size = 50
    print ( f'{cor.vermelho}Selecione o logo ' )
    destino = filedialog.askopenfilename ( )  # seletor do logo
    logo = Image.open ( f'{destino}' )

    # redirecionamento de logo
    xmin = ymin = int ( (width / 2) - (logo_size / 2) )
    xmax = ymax = int ( (width / 2) + (logo_size / 2) )
    logo = logo.resize ( (xmax - xmin , ymax - ymin) )
    im.paste ( logo , (xmin , ymin , xmax , ymax) )
    im.show ( )

print(f'{cor.vermelho}Aguarda mais um minuto...\n Finalizando')
sleep(0.8)

source = f'{nome}.svg'
destination = f'save_qr_code\{folder}'
shutil.move(source,destination)

source = f'{nome}.png'
destination = f'save_qr_code\{folder}'
shutil.move(source,destination)