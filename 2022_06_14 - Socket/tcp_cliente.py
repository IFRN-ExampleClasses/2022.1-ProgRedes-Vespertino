# Importando a biblioteca socket
import socket

# Definindo as constantes do programa
HOST        = 'localhost'   # Definindo o IP do servidor
PORT        = 25000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 10            # Definindo o tamanho do buffer

# Criando o socket UDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket a porta
tcp_socket.connect((HOST, PORT)) 

while True:
    # Solicitando uma mensagem ao usuário
    mensagem_ida = input('Digite a mensagem: ')
    # Convertendo a mensagem digitada de string para bytes
    mensagem_ida = mensagem_ida.encode('utf-8')
    # Enviando a mensagem ao servidor      
    tcp_socket.send(mensagem_ida)
    
    if mensagem_ida.decode(CODE_PAGE).upper() == 'EXIT': break

# Fechando o socket
tcp_socket.close()
