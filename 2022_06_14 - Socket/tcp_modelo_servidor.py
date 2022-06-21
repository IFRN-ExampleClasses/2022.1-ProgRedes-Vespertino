# Importando a biblioteca socket
import socket, sys

# Definindo as constantes do programa
HOST        = 'localhost'   # Definindo o IP do servidor
PORT        = 60000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 512           # Definindo o tamanho do buffer
MAX_LISTEN  = 1             # Definidndo o máximo de conexões enfileiradas

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # Vinculando o socket a porta
tcp_socket.bind((HOST, PORT))

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN) 

print('\nRecebendo Mensagens...\n\n')

try:
   while True:
      # Aceita a conexão com o cliente
      conexao, ip_cliente = tcp_socket.accept() 
      print(f'Conectado por: {ip_cliente}')
      while True:
         # Recebendo a mensagem do cliente
         mensagem = conexao.recv(BUFFER_SIZE)
         # Convertendo a mensagem recebida de bytes para string
         mensagem = mensagem.decode(CODE_PAGE)

         # Imprimindo a mensagem recebida convertendo de bytes para string
         if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
            conexao.close()    
            break
         else:
            print(f'{ip_cliente}->  {mensagem}')
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
#finally:    
   #print('Derrubando o servidor...', ip_cliente)
   #conexao.close()
