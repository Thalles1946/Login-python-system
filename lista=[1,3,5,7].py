nd=0
sd=0
print("bem vindo ao cofre, se voce não tiver login, responda 'não' a pergunta abaixo")
p1=str(input("Voce tem login? "))
if p1=="não":
    n=str(input("digite o seu nome para o novo login: "))
    s=int(input("agora digite sua senha: "))
    s1=int(input("repita a senha: "))
    print("login criado com sucesso")
    while s1!=s:
        s1=int(input("as senhas não coincidem, digite novamente a senha s1: "))
elif p1=="sim":
    print("digite seu nome e senha: ")
    n=str(input())
    s=int(input())
#ainda falta criar um metodo onde o sistema solicite os dados de novo
if n!=n or s!=s:
    print("dados invalidos, digite novamente")
elif n==n and s==s:
    print ("acesso permitido")
