package aula6;

public class GatoTeste {
    
    public static void main(String[] args) {
        Gato gato1 = new Gato();
        gato1.nome = "Barney ";
        gato1.setIdade(3);
        System.out.println(gato1.nome + " tem " + gato1.getIdade() + " anos" );
        gato1.comer("ração de Frango");
        gato1.dormir();
        
    }

}
