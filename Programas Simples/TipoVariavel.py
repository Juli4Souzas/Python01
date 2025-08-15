codigo = 10
salario = 1500.00
nome = 'José'
situação = True

tipo = type(salario)

print(salario)
print(tipo)

print("----- concatenando -----")
print("codigo:",codigo, "Nome:", nome, "O salário atual é de:", salario)

print("----- concatenando com '+' -----")
#    Também podemos concatenar as informações na linguagem Python utilizando o sinal de soma (+).
#    Neste caso, temos de converter os valores que não são string para o tipo string.
print("codigo: "+ str (codigo)+ " Nome: " +nome+ " O salário atual é de: " + str(salario))

# Máscaras
print("----- Mácaras -----")
print("Código: %d "%codigo)
print("Nome: %s "%nome)
print("Salário: %.2f "%salario)
print("Ativo: %r "%situação)