import asyncio

HOST = '127.0.0.1'
PORT = 65432

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """
    Corrotina chamada pelo Event Loop para cada nova conexão.
    """
    addr = writer.get_extra_info('peername')
    print(f"[NOVA CONEXÃO] {addr}")

    try:
        # 1. Leia os dados enviados pelo cliente
        data = await reader.read(1024)
        mensagem = data.decode('utf-8')
        print(f"[{addr}] Recebido: {mensagem}")

        # 2. Simule um processamento pesado SEM bloquear a thread principal.
        # asyncio.sleep(5) suspende esta corrotina, permitindo que o 
        # Event Loop atenda outros clientes enquanto isso.
        await asyncio.sleep(5)

        # 3. Envie a resposta ao cliente
        resposta = f"Sucesso: {mensagem} processada.".encode('utf-8')
        writer.write(resposta)
        await writer.drain() # Garante que os dados saiam do buffer para a rede

    except Exception as e:
        print(f"Erro ao lidar com {addr}: {e}")
    finally:
        # 4. Feche a conexão de forma segura
        writer.close()
        await writer.wait_closed()
        print(f"[DESCONECTADO] {addr}")


async def main():
    """
    Ponto de entrada assíncrono: cria e inicia o servidor.
    """
    
    server = await asyncio.start_server(
        handle_client, HOST, PORT, backlog=250
    )

    addr = server.sockets[0].getsockname()
    print(f"[ASSÍNCRONO] Servidor rodando em {addr} — Event Loop ativo.")

    # Mantenha o servidor rodando indefinidamente
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[DESLIGANDO] Servidor encerrado pelo usuário.")