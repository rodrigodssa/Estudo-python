
for i in range(20):
    print("Se inscreva na pagina oficial")
    print("Já se inscreveu na pagina? ")

lista_preco = [1500, 1000, 800, 2000]
imposto = 0.1

for preco in lista_preco:
    imposto = preco * 0.1
    print(f"preco {preco}, imposto: {imposto}")

# regra do imposto
# preco até 1000 -> imposto é de 10%
# preco maior do que 1000 -> imposto é de 15%

total_imposto = 0 # acumulado

for preco in lista_preco: 
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1 
    print(f"preco {preco}, imposto: {imposto}")


total_imposto = 0 # acumulado
    

for preco in  lista_preco: # 1000
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1 # 80
    print(f"Preço {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto 

print(total_imposto)

# exercicios





