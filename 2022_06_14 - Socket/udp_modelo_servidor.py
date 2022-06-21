# Importando a biblioteca socket e sys
import sys, socket

# Definindo as constantes do programa
HOST        = 'localhost'   # Definindo o IP do servidor
PORT        = 50000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 512           # Definindo o tamanho do buffer

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST, PORT)) 

print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        # Recebendo os dados do cliente
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        # Convertendo a mensagem recebida de bytes para string
        mensagem = mensagem.decode(CODE_PAGE)
        # Imprimindo a mensagem recebida 
        if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            print(f'{ip_cliente}->  {mensagem}')
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()