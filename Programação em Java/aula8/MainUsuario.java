package aula8;
import java.util.Scanner;


public class MainUsuario {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    Usuario[] usuarios = new Usuario[5];

    for (int i = 0; i < usuarios.length; i++) {
      Usuario temp = new Usuario();
      System.out.println(i + ".Digite seu Nome: ");
      temp.setNome(scan.nextLine());
      System.out.println(i + ".Digite sua Senha: ");
      temp.setSenha(scan.nextLine());
      usuarios[i] = temp;
      System.out.println("Usuario "+ i + ": "+ temp.getNome());
      System.out.println("Senha "+ i + ": "+ temp.getSenha());

    }
  }
}
