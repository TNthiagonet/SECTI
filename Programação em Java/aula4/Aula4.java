package aula4;
import java.util.Scanner;

public class Aula4 {
    public static void main(String args[])  {

        Scanner leitor = new Scanner(System.in);

        int valor1 = leitor.nextInt();
        int valor2 = leitor.nextInt();
        int valor3 = leitor.nextInt();
        //  Se valor1 for maior que valor2 e valor1 for maior que o valor 3
        if (valor1 > valor2 && valor1 > valor3){
            // Imprima 
            System.out.println("O valor um: " + valor1 + " é o mais alto");

        //  Se valor2 for maior que valor1 e valor2 for maior que o valor 3
        } else if (valor2 > valor1 && valor2 > valor3) {
            // Imprima
            System.out.printf("O valor dois: %d é o mais alto", valor2); 
        
        //  Se valor3 for maior que valor1 e valor3 for maior que o valor 2
        } else if (valor3 > valor1 && valor3 > valor2) {
            // Imprima
            System.out.printf("O valor tres: %d é o mais alto", valor3);
        } 
    }
}

