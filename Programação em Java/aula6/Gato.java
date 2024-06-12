package aula6;

public class Gato {
    public String nome;
	private int idade;
    protected String cor;
    protected String dono;
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void comer(String racao) {
        System.out.println(nome + "está comendo... " + racao);
    }

    public void dormir() {
        System.out.println(nome + "está dormindo... ");
    }

    public void fazerAniversario(String data) {
        if (data == "15/05"){
            System.out.println(nome + "está fazendo aniversário... ");
        } 
    }

    public void brincar(String brinquedo){
        System.out.println(nome + "está brincando....");
    }
    
    


}



