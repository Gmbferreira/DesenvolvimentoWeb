Parte A - Respostas
1- Se o cliente for executado antes do servidor, ele falha em se conectar pois não há servidor existente
2- O mecanismo responsável são os numeros de sequencia atribuidos aos segmentos
3- O código não suporta isso. Enquanto o cliente 1 estiver sendo atendido, o cliente 2 ficara em uma fila

Parte B - Respostas
1- Nada aconteceu, a mensagem não chegou e o cliente travou até sofrer timeout. no tcp, a conexão falharia e o cliente receberia um erro
2- Chamads de voz em tempo real e livestreams, tcp atrasaria pois devem minimiar latência mesmo arriscando perdas parciais de pacotes.
3- É possivel implementar. A arquitetura precisa de um relógio (Timer) que remove da lista qualquer cliente que não envie pacotes por mais de alguns segundos (inatividade) e mensagens periódicas (Heartbeat).