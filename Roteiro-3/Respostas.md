Reflexão:
1- No multicast, o endereço não está escrito diretamente, enquanto no tcp e udp ele está. Quando ele não está escrito diretamente, isso favorece a transparência de localização reduzindo o acoplamento
2- O cliente deve montar as strings manualmente. Isso significa que não há nenhuma(ausencia) transparência de acesso, já que o cliente não sabe o que deve digitar
3-Para o TCP seria falha total, para o UDP seria uma falha silenciosa, demonstrada por timeouts infinitos. Já para o multicast, não importa desde que o servidor aponte para o cliente corretamente