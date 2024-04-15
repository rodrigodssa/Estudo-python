nome = input("Digite aqui seu nome: ")
email = input("Digite aqui seu email: ")

# descubra o servidor do eamil
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o 1 nome do usuario
posicao = nome.find (" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com email tal
mensagem = f"usuario {primeiro_nome} cadastrado com sucesso  email: {email}"
print(mensagem)

# construa uma mensagem: Enviamos um link de confirmacao para o email R***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmacao para o email {primeira_letra} ***{servidor}"
print(mensagem2)




