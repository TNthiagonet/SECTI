// com While, que é sempre verdadeiro, utilizamos o break para
// digigitamos o numero de 0 a 10 
// a maquina escolhe um número randomicamente 
// quando este número for acertado ele para de perguntar
package aula7;
import java.util.Random;
import java.util.Scanner;

public class Aula7exercicio1 {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    Random random = new Random();

    int numero = random.nextInt(11);
    int tentativaTotal = 0;
    int tentativa;

    System.out.println("Digite um número de 0 a 10: ");
    while (true) {
      tentativa = scan.nextInt();
      tentativaTotal++;
      if (numero == tentativa){
        System.out.println("Você acertou! O número era " + numero );
        break;
      }else{
        System.out.println("Você errou! Tente novamente.");
      }
    }
  }
}
