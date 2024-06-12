package aula8;
import java.util.ArrayList;
import java.util.List;

public class MainList {
  public static void main(String[] args) {
    Usuario[] user = new Usuario[5];
    
    List<Usuario> users = new ArrayList<>(); 

    Usuario user1 = new Usuario("Chiquinha", "1234");
    users.add(user1);
    Usuario user2 = new Usuario("Chaves", "1234");
    users.add(user2);
    Usuario user3 = new Usuario("Kiko", "1234");
    users.add(user3);
    Usuario user4 = new Usuario("Madruga", "1234");
    users.add(user4);
    Usuario user5 = new Usuario("Florinda", "1234");
    users.add(user5);
  }
}

