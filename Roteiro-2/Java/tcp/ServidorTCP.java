import java.io.*;
import java.net.*;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class ServidorTCP {
    public static void main(String[] args) throws IOException {
        int porta = 5021;
        DateTimeFormatter formatadorHora = DateTimeFormatter.ofPattern("HH:mm:ss");

        try (ServerSocket servidor = new ServerSocket(porta)) {
            System.out.println("[TCP] Servidor aguardando conexões na porta " + porta + "...");
            
            try (Socket cliente = servidor.accept();
                 BufferedReader entrada = new BufferedReader(
                         new InputStreamReader(cliente.getInputStream(), "UTF-8"));
                 PrintWriter saida = new PrintWriter(new OutputStreamWriter(cliente.getOutputStream(), "UTF-8"), true)) {

                System.out.println("[TCP] Cliente conectado: " + cliente.getRemoteSocketAddress());
                String mensagem;
                
                while ((mensagem = entrada.readLine()) != null) {
                    // Remove espaços em branco e caracteres invisíveis de controle
                    String comando = mensagem.trim().replaceAll("\\p{C}", "").toLowerCase();
                    System.out.println("[TCP] Recebido: [" + mensagem + "]");
                    
                    if (comando.equals("sair")) {
                        saida.println("Encerrando conexão. Até mais!");
                        saida.flush();
                        break;
                    } else if (comando.equals("hora") || comando.contains("hora")) {
                        String horaAtual = LocalTime.now().format(formatadorHora);
                        saida.println("Hora atual do servidor: " + horaAtual);
                        saida.flush();
                    } else {
                        saida.println("Monitor responde: recebi sua mensagem -> \"" + mensagem + "\"");
                        saida.flush();
                    }
                }
            }
        }
        System.out.println("[TCP] Servidor encerrado.");
    }
}