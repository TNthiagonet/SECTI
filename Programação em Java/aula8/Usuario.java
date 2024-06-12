package aula8;

public class Usuario {
  private String nome;
  private String senha;

  public Usuario (String nome, String senha){
    setNome(nome);
    setSenha(senha);
  }

  public Usuario() {
    //TODO Auto-generated constructor stub
  }

  public String getNome() {
    return nome;

  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getSenha() {
    return senha;
  }

  public void setSenha(String senha) {
    this.senha = senha;
  }
}
