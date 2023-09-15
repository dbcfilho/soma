#Nesta linha estou apenas imprimindo uma informação ao usuário.
print("Digite uma sequência de valores terminada por zero.")

#aqui inseri duas variaveis, soma pois é aonde o valor será "repetido" e valor aonde o while vai atuar, foi definido 1 por ser diferente de 0, apenas para funcionar a lógica
soma = 0
valor = 1

#enquanto o valor for diferente de 0, a partir dai ele executa a captação "Digite um valor a ser somado" e faz a sequencia de ações até receber o valor de zero e finalizar o programa
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)