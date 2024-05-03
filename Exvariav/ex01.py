nome = "Rodrigo"   # obs srting
idade = 41         #  obs "41" dentro de aspas ele é uma string  # idade = 41 fora de aspas numero Int= inteiro
altura = 1.81      # Float numero com casas decimais
# is_male = True / False O Obs true para verdadeiro ou False para falso 
gosto_de = "Programacao"

print(f"Meu nome é {nome}.") # obs colocar o valor de uma variavel dentro de um texto (f)+ {}
print(f"Eu gosto de {gosto_de}.")
print(f"Eu tenho {idade} anos.")

idade = 34   # obs adicionando uma nova variavel ele imprimia idade = 41 e passou para idade = 34

print(f"{nome} gosta de {gosto_de} e tem {idade} anos e tem {altura} de altura.")