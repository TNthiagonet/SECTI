package aula3;

public class Aula3 {

    public static void main(String args[])  {
        String aluno1 = "João";
        String aluno2 = "Pedro";
        String aluno3 = "Francisco";

        Float nota1aluno1 = 9.3f;
        Float nota2aluno1 = 8.4f;
        Float nota3aluno1 = 7.2f;
        Float nota4aluno1 = 8.0f;

        Float nota1aluno2 = 7.5f;
        Float nota2aluno2 = 7.6f;
        Float nota3aluno2 = 7.0f;
        Float nota4aluno2 = 7.2f;

        Float nota1aluno3 = 7.0f;
        Float nota2aluno3 = 6.0f;
        Float nota3aluno3 = 5.0f;
        Float nota4aluno3 = 4.0f;

        Float media = 7.0f;

        Float mediaAluno1 = (nota1aluno1 + nota2aluno1 + nota3aluno1 + nota4aluno1) / 4;
        Float mediaAluno2 = (nota1aluno2 + nota2aluno2 + nota3aluno2 + nota4aluno2) / 4;
        Float mediaAluno3 = (nota1aluno3 + nota2aluno3 + nota3aluno3 + nota4aluno3) / 4;

        if (mediaAluno1 >= media){
            System.out.println("O aluno " + aluno1 + " obteve as notas " + nota1aluno1 + " - " + nota2aluno1 + " - " + nota3aluno1 + " - " + nota4aluno1 + " e está aprovado com a média " + mediaAluno1);
        } else {
            System.out.println("O aluno " + aluno1 + " obteve as notas " + nota1aluno1 + " - " + nota2aluno1 + " - " + nota3aluno1 + " - " + nota4aluno1 + " e está reprovado com a média " + mediaAluno1);
        }
        if (mediaAluno2 >= media){
            System.out.println("O aluno " + aluno2 + " obteve as notas "  + nota1aluno2 + " - " + nota2aluno2 + " - " + nota3aluno2 + " - " + nota4aluno2 + " e está aprovado com a média " + mediaAluno2);
        } else {
            System.out.println("O aluno " + aluno2 + " obteve as notas "  + nota1aluno2 + " - " + nota2aluno2 + " - " + nota3aluno2 + " - " + nota4aluno2 + " e está reprovado com a média " + mediaAluno2);
        }
        if (mediaAluno3 >= media){
            System.out.println("O aluno " + aluno3 + " obteve as notas "  + nota1aluno3 + " - " + nota2aluno3 + " - " + nota3aluno3 + " - " + nota4aluno3 + " e está aprovado com a média " + mediaAluno3);
        } else {
            System.out.println("O aluno " + aluno3 + " obteve as notas "  + nota1aluno3 + " - " + nota2aluno3 + " - " + nota3aluno3 + " - " + nota4aluno3 + " e está reprovado com a média " + mediaAluno3);
        }
    }   
}
