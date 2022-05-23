import sys,os 

# Obtendo o diretório corrente
diretorio_atual = os.path.realpath(__file__)
diretorio_atual = os.path.dirname(diretorio_atual)

nome_arquivo = diretorio_atual + '\\servidores.csv'

try:
    print('Abrindo o arquivo: {0}'.format(nome_arquivo))
    arquivo_input = open(nome_arquivo, 'r', encoding='utf-8')
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

    matricula = '1756858'
    print(dados_input[matricula])

    print('')
    print(dados_input[matricula]['nome'])
    print(dados_input[matricula]['email'])
    print(dados_input[matricula]['area'])
    
    # Fechando o arquivo
    print('\nFechando o arquivo: {0}'.format(nome_arquivo))
    arquivo_input.close()
finally:
     print('\nPrograma Encerrado...\n')
