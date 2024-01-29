def login (user, senha):
    if user == "mateus" and senha == "123":
        return "Logado com sucesso"
    else:
        return "Login ou senha errados"
    
user = "mateus"
senha = '123'

a = login(user, senha)
print(a)