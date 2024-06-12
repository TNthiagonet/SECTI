package aula5;


public class Alunos {

	public String nome;
	private int idade;

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		
		if (idade > 0 && idade < 120){
			this.idade = idade;
		}
		else{
			System.out.println("Insira uma idade válida");
		}
	}
	public void aprenderConteudo(){
        System.out.println(" e está aprendendo JAVA!");
	}
	public void fazerAniversario(){
		idade++;
	}

}
