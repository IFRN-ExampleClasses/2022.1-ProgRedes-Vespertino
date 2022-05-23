import sys,os 

# Obtendo o diretório corrente
diretorio_atual = os.path.realpath(__file__)
diretorio_atual = os.path.dirname(diretorio_atual)

nome_arquivo_input  = diretorio_atual + '\\servidores.csv'
nome_arquivo_output = diretorio_atual + '\\servidores_2.txt'
try:
    print('Abrindo o arquivo: {0}'.format(nome_arquivo_input))
    arquivo_input = open(nome_arquivo_input, 'r', encoding='utf-8')
except FileNotFoundError:
    print('\nDeu ERRO...\nArquivo NÃO EXISTE...')
except PermissionError:
    print('\nDeu ERRO...\nArquivo JÁ ABERTO...')
except:
    print('\nDeu ERRO...\n', sys.exc_info()[0])
else:
    # Lendo os dados do arquivo de input e adicionando em uma lista
    print('\nLendo os dados do arquivo...\n')
    dados_input = dict()
    while True:
        linha = arquivo_input.readline()[:-1]
        if linha == '': break
        linha = linha.split(';')
        chave = linha[0]
        dados_input[chave] = {  'nome' : linha[1], 
                                'area' : linha[12],
                                'email': linha[2], 
                            }
    # Fechando o arquivo
    print('\nFechando o arquivo: {0}'.format(nome_arquivo_input))
    arquivo_input.close()

    # Salvando os dados tratados em arquivo
    print('Salvando o arquivo: {0}'.format(nome_arquivo_output))
    arquivo_output = open(nome_arquivo_output, 'w', encoding='utf-8')
    arquivo_output.write('siape#nome#area#email')
    chaves = dados_input.keys()
    contador = 0
    for i in dados_input:
        linha = '{0}#{1}#{2}#{3}'
        siape = chaves[contador]
        nome  = i['nome']
        area  = i['area']
        email = i['email']
        linha = linha.format(siape, nome, area, email)
        arquivo_output.write(linha)
        contador += 1
    arquivo_output.close()
finally:
     print('\nPrograma Encerrado...\n')
