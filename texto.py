faturamento = 1000
custo = 700

lucro = faturamento - custo

print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
print("Faturamento:" + str(faturamento) + ", Custo:" + str(custo) + ", Lucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar o elemento: a (posição)

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "Rodrigo Almeida"
print(nome.capitalize()) # capitalize coloca 1 letra em maiusculo ex Rodrigo almeida
print(nome.title()) # title coloca 1 letra de cada palvra em maisculo ex Rodrigo Almeida

# especiais - formatação numerico
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}") # \n = enter dentro de um texto no print 
print(f"Margem: {margem:.1%}")

# exercicios

nome = "Rodrigo ALmeida"
email = "Rodrigofalso@gmail.com"

# descubra o servidor do eamil
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o 1 nome do usuario
posicao = nome.find (" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com email
mensagem = f"usuario {primeiro_nome} cadastrado com sucesso com email: {email}"
print(mensagem)







