n="admin"
s=123456
nd=0
sd=0
print("bem vindo ao cofre, se voce não tiver login, responda 'não' a pergunta abaixo")
p1=str(input("Voce tem login? "))
if p1=="não":
    n=str(input("digite o seu nome para o novo login: "))
    s=int(input("agora digite sua senha: "))
    s1=int(input("repita a senha: "))
    while s1!=s:
        s1=int(input("as senhas não coincidem, digite novamente a senha s1: "))
    print("login criado com sucesso")
    nd=str(input("para entrar no sistema digite seu nome: "))
    sd=int(input("agora, digite sua senha: "))
    while nd!=n or sd!=s:
        print ("dados invalidos, digite novamente")
        nd=str(input("para entrar no sistema digite seu nome: "))
        sd=int(input("agora, digite sua senha: "))
    print ("acesso permitido")
elif p1=="sim":
    print("digite seu nome e senha: ")
    nz=str(input())
    sz=int(input())
    while nz!=n and sz!=s:
        print("dados invalidos, digite novamente")
        nz=str(input("para entrar no sistema digite seu nome: "))
        sz=int(input("agora, digite sua senha: "))
    print("acesso permitido")
