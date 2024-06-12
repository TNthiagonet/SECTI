package aula4;
import java.util.Scanner;

public class Aula4exercicio2 {
    public static void main(String args[])  {

        Scanner leitor = new Scanner(System.in);

        System.out.println("Qual o seu nome: " );
        String nome = leitor.nextLine();

        System.out.println("Qual sua altura: " );
        Float altura = leitor.nextFloat();
        
        // A linha abaixo corrige o erro de usar varios (leitor.nextLine();) em sequência
        leitor.nextLine();
        System.out.println("Qual o seu curso: " );
        String curso = leitor.nextLine();

        System.out.println("Qual o seu endereço: " );
        String endereco = leitor.nextLine();

        System.out.println("Qual sua idade: " );
        int idade = leitor.nextInt();

        System.out.println("O Aluno " + nome + " tem: " + idade + " anos, " + " e está no curso de: " + curso + ", com altura de: " + altura + " mora em: " + endereco);

    }
}

