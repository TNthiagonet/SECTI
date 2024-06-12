package aula9;

import java.util.HashMap;
import java.util.Map;

public class DicionarioUsuario {
    public static void main(String[] args) {
        Map<String,String>usuarios=new HashMap<>();

        usuarios.put("user00","senha00");
        usuarios.put("user01","senha01");
        usuarios.put("user02","senha02");
        usuarios.put("user03","senha03");
        usuarios.put("user04","senha04");

        System.out.println("Nomes: "+ usuarios.keySet());
        System.out.println("Senhas: "+ usuarios.values());

    }
}
