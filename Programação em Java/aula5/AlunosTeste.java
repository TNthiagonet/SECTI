package aula5;

import java.util.Scanner;

public class AlunosTeste {
    public static void main(String args[])  {
Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome do aluno: ");
        Alunos aluno1= new Alunos();
        aluno1.nome= scanner.nextLine();
        System.out.println("Digite a idade do aluno: ");
        aluno1.setIdade(scanner.nextInt());

        System.out.println("O Aluno " + aluno1.nome + " tem " + aluno1.getIdade() + " anos ");
        aluno1.aprenderConteudo();
        aluno1.fazerAniversario();
        System.out.println("e a proxima idade dele será:  " + aluno1.getIdade());
    }
}
