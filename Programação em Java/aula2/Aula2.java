package aula2;

public class Aula2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// Variável para armazenar nomes:
		String nome = "Thiago";
		// Variável para armazenar idade:
		int idade = 42;
		int nascimento = 1981;
		int esteAno = 2024;
		// Variável para armazenar altura:
		float altura = 1.74f;
		// Variável para armazenar estado civil:
		boolean estaCasado = false;
		
		int idadeZ = esteAno - nascimento;
		
		float primeiraNota = 10.0f;
		float segundaNota = 10.0f;
		float mediaDoAluno = (primeiraNota + segundaNota) / 2;
		
		System.out.println("Nome: " + nome);
		System.out.println("Idade: " + idade);
		System.out.println("Altura" + altura);
		System.out.println("Está Casado: " + estaCasado );
		System.out.println("Segunda aula do curso de JAVA com a professora Júlia Pamplona");
		System.out.println("O aluno " + nome + " tem " + idade + " anos, " + "tem altura de " + altura + " e está casado? " + estaCasado);
		System.out.println("Neste ano ele completa a idade de: " + idadeZ + " anos");
		System.out.println("Média do aluno: " + mediaDoAluno);
	}

}
