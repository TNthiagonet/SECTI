package aula4;
import java.util.Scanner;

public class Aula4exercicio1 {
    public static void main(String args[])  {

        Scanner leitorTexto = new Scanner(System.in);
        Scanner leitorNumero = new Scanner(System.in);

        System.out.println("Escreva um texto");

        String texto = leitorTexto.nextLine();

        System.out.println("O seu texto foi: " + texto);

        System.out.println("Escreva um número ");

        float numero = leitorNumero.nextFloat();

        System.out.println("O seu numero foi: " + numero);

    }
}
