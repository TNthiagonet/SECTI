// Com (for) recebemos 5 numeros e somamos eles
package aula7;
import java.util.Scanner;

public class Aula7 {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int soma = 0;

    System.out.println("Insira os números para a soma: ");
    for (int i=1; i<=5; i++) {
      System.out.println("Número" + i + ": ");
      soma += scan.nextInt();
    }
    System.out.println("A soma é: "+ soma);
  }
}
