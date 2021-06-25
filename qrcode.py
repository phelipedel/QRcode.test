import pyqrcode
import png
from pyqrcode import QRCode
from lib.utilidade import cor
from time import sleep
import os
import shutil
from tkinter import filedialog
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

# criando e salvando arquivo svg

url.svg ( f'{nome}.svg' , scale = 8 )
print ( f'{cor.verde}QRcode .svg gerado com sucesso. ' )
sleep ( 0.1 )
url.png ( f'{nome}.png' , scale = 6 )
print ( f'{cor.verde}QRcode .png gerado com sucesso. ' )
sleep ( 0.1 )

r = str ( input ( 'Quer adicionar uma imagem ? [S/N]' ) ).upper ( ) [ 0 ]
if r == 'S' :
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
