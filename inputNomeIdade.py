# Solicita ao usuário o nome e a idade
nome  = input("Digite o seu nome: ")
idade = input("Digita a sua idade: ")

# Convertendo a idade para número inteiro
idade = int(idade)

# Criando uma saudação com nome e a idade
saudacao = f"Olá, {nome}! Voc~e possuí {idade} anos."

# Imprimindo a saudação
print(saudacao)
