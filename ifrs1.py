"""1) Produto entre dois valores
Faça um programa para que o usuário informe dois valore inteiros, calcular o produto entre eles e mostrar o
resultado, conforme os exemplos abaixo.
Entrada: dois valores inteiros.
Saída: um valor inteiro, que representa o produto da multiplicação entre os dois números informados na entrada.
Exemplos de entrada e saída:"""

valor1 = int(input("Digite um valor inteiro:")) #Captura um número inteiro e armazena na variavel valor1
print(valor1) #Exibe o valor da variável valor1 no terminal

valor2 = int(input("Digite outro valor inteiro:")) #Captura outro número inteiro e armazena na variável valor2
print(valor2) #Exibe o valor da variável valor2 no terminal

calcular_Produto = valor1 * valor2 #Calcular o produto entre os dois valores

resultado = print("O Resultado da multiplicação entre", valor1,"e",valor2,"É: ",calcular_Produto)
