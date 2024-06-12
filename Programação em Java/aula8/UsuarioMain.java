package aula8;

public class UsuarioMain {
    /**
     * @param args
     */
    public static void main(String[] args) {
        Usuario[] user = new Usuario[5];

        Usuario user1 =new Usuario("Chiquinha", "1234");
        user[0]= user1;
        Usuario user2 =new Usuario("Chaves", "1234");
        user[1]= user2;
        Usuario user3 =new Usuario("Kiko", "1234");
        user[2]= user3;
        Usuario user4 =new Usuario("Madruga", "1234");
        user[3]= user4;
        Usuario user5 =new Usuario("Florinda", "1234");
        user[4]= user5;

        for(int i=0; i<user.length;i++){
          System.out.println();
        }

    }
}
