## Questão 1.
### 1.1.
A serialização ocorre dentro da biblioteca xmlrpc.client, no ServerProxy
logs:
Servidor XML-RPC em http://localhost:8765 | Ctrl+C para encerrar
127.0.0.1 - - [09/Mar/2026 21:42:58] "POST / HTTP/1.1" 200 -
[Servidor] calcular(soma, 10.0, 3.0) = 13.0
127.0.0.1 - - [09/Mar/2026 21:43:00] "POST / HTTP/1.1" 200 -
[Servidor] calcular(subtracao, 10.0, 3.0) = 7.0
127.0.0.1 - - [09/Mar/2026 21:43:02] "POST / HTTP/1.1" 200 -
[Servidor] calcular(multiplicacao, 4.0, 7.0) = 28.0
127.0.0.1 - - [09/Mar/2026 21:43:04] "POST / HTTP/1.1" 200 -
[Servidor] calcular(divisao, 22.0, 7.0) = 3.142857142857143
127.0.0.1 - - [09/Mar/2026 21:43:06] "POST / HTTP/1.1" 200 -
[Servidor] Evento: [21:43:08] Aluno concluiu Tarefa 1
127.0.0.1 - - [09/Mar/2026 21:43:08] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [09/Mar/2026 21:43:10] "POST / HTTP/1.1" 200 -

### 1.2
xmlrpc.client.Fault é uma classe de exceção específica que encapsula erros ocorridos no lado do servidor durante a execução de uma função. Ela traduz a resposta de erro do XML para um objeto Python que contém um faultCode e uma faultString. (Código numerico e descrição da falha respectivamente)
O Fault é um erro genérico. Ele perde o tipo original do erro e também, ele não possui o stack trace completo do servidor, fornecendo apenas o que foi explicitamente enviado via rede.
O RPC precisa de um mecanismo especial, porque erros são objetos complexos de memória que não podem ser fisicamente enviados pela rede. O RPC precisa de um padrão (o XML) para serializar a falha de forma que qualquer linguagem entenda que algo deu errado, permitindo que o cliente trate o problema em vez de simplesmente travar a conexão.

### 1.3
O system.listMethods() relaciona-se mais diretamente à Transparência de Acesso. Isso acontece porque esta transparência oculta as diferenças na representação de dados e nos mecanismos de invocação. O recurso permite que o cliente descubra os metodos que existem, a interface do serviço de forma padronizada, sem precisar conhecer como as funções foram implementadas ou organizadas internamente no servidor.

## Questão 2.
### 2.1
Marshalling: linhas 71 e 37
Transmissão: linhas 75 e 41
Unmarshalling: linhas 29 e 78
Dispatching: linha 36
### 2.2
O JSON aumenta a latência e o consumo de banda por ser um formato textual redundante, além de que seu processamento consome muito mais cpu, enquanto o Protobuf é binário e extremamente compacto. Em larga escala, isso significa em custos maiores de infraestrutura e uma capacidade reduzida de processar requisições simultâneas.
### 2.3
Isso acontece porque o tcp é orientado a fluxo(byte stream). Sem o framing, o receptor não saberia onde termina uma chamada e começa a próxima, juntando ou desorganizando os dados.

## Questão 3.
### 3.1
O 201 Created comunica a criação de um novo recurso de forma explicita, permitindo que intermediários e proxies invalidem caches de colections desatualizadas. Ele indica uma mudança permanente no estado do servidor que o código 200 OK não descreve com a mesma precisão semântica.

### 3.2
Para ser realmente stateless, o estado dos recursos deve ser movido da memória volátil do servidor para uma camada de persistência externa, como um banco de dados SQL. Isso garante que o servidor não guarde contexto local, permitindo que qualquer instância processe qualquer requisição de forma independente.

### 3.3
A abordagem usada para  requests.post("/calculos", json={...}) deixa mais claro o contato entre cliente e servidor que proxy.calcular("soma", 7, 3). Isso acontece porque no RPC, o contrato é implícito e depende de nomes de funções arbitrários que ocultam a natureza da comunicação. No REST, a semântica é universal, sendo o uso de métodos padrão e códigos de estado, como 201 ou 404, o que torna a interação autodescritiva e independente da implementação interna do servidor.

## Questão 4.
### 4.1
A principal diferença é que o contrato explícito do gRPC garante tipagem forte e validação automática, enquanto o REST depende de convenções e documentação externa que o código pode ignorar. Caso o servidor altero os campos, acontece uma quebra de compatibilidade binária.

### 4.2
São equivalentes. O gRPC é semanticamente mais rico, possuindo 16 status específicos contra o genérico HTTP 400. Enquanto o REST exige o parsing manual do corpo do erro, o gRPC transporta metadados tipados e legíveis por máquina nativamente no cabeçalho da resposta.

### 4.3
O xml.client.Fault limita-se a um par básico de texto (code/string), exigindo análise manual de strings para entender erros complexos. O grpc.RpcError oferece códigos de status específicos e metadados binários tipados que o cliente processa programaticamente. 
Isso faz com que o grpc.Error provenha mais informações.