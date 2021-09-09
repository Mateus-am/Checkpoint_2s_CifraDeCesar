'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Checkpoint 1 - 2° Semestre
Alunos:
João Paulo Silva de Queiroz - RM86376
Mateus Amado Monteiro da Silva - RM87974
'''

alfabeto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")  # lista de caracteres presentes no metodo de codificacao.
arquivo = open('arquivo.txt', 'r')
mensagem = arquivo.read()
mensagem2 = ''
cod = ''
cod2 = ''
chave = 4

print('Criptografando...')

def encod(mensagem, cod):
    for caractere in mensagem:  # para cada caracter presente na mensagem o programa fara algo
        if caractere in alfabeto:  # se o caracter que estiver presente na mensagem tambem estiver no alfabeto declarado...
            ordem = alfabeto.index(caractere)  # adiciona os caracteres a uma ordem.
            cod += alfabeto[(ordem + chave) % len(alfabeto)]  # a variavel recebera a codificacao da mensagem.
        else:
            cod += caractere  # caso o caracter nao seja identificado no alfabeto determinado, ele sera adicionado diretamente.

    arquivo = open('arquivo.txt', 'w')  # arquivo aberto em modo escrita
    arquivo.write(cod)  # escrita da codificacao ao arquivo.
    arquivo.close()  # fechando o arquivo


def decod(mensagem2, cod2):
    arquivo = open('arquivo.txt', 'r')
    mensagem2 = arquivo.read()
    for caractere in mensagem2:
        if caractere in alfabeto:
            ordem = alfabeto.index(caractere)
            cod2 += alfabeto[(ordem - chave) % len(alfabeto)]
        else:
            cod2 += caractere

    arquivo = open('arquivo.txt', 'w')  # arquivo aberto em modo escrita
    arquivo.write(cod2)  # escrita da codificacao ao arquivo.
    arquivo.close()  # fechando o arquivo


encod(mensagem, cod)

print("Arquivo Criptografrado")
key = int(input("Para descriptografar o arquivo insira a chave correta: "))

if key == chave:
    decod(mensagem2, cod2)
else:
    print("Chave incorreta")
