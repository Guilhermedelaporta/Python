"""2) Reajuste de salário
Este é o mês de reajuste salarial. Desenvolva um programa para o usuário informar seu salário atual e o
percentual de reajuste prometido. Esses dois valores são positivos, com até duas casas decimais. Depois o
programa calcula e mostra qual será o novo salário, conforme determinado nos exemplos abaixo.
Entrada: dois valores positivos com duas casas decimais, representando, respectivamente, o salário atual e o
percentual de reajuste.
Saída: um valor positivo, com duas casas decimais, que representa o novo salário.
Exemplos de entrada e saída:"""

salario = float(input("Digite o seu salário: ")) # Um campo de entrada que converte o tipo de dado para float para o usuario digitar o seu salário 
percentual_de_reajuste = float(input("Digite o valor do reajuste do salário: ")) #Um campo de entrada que converte tipo de dado para float para o usuário digitar o percentual de reajuste.
print("O seu salário é: ",salario,"E o valor do reajuste é de:", percentual_de_reajuste)
reajuste = (percentual_de_reajuste * salario) / 100 # Uma variável que faz o cálculo da porcentagem 
salario_com_o_reajuste = reajuste + salario # Uma variável que soma o salário com o percentual de reajuste
print("O Seu salário depois do reajuste é de: ",salario_com_o_reajuste) #Exibe na tela o resultado da soma entre o salário e o percentual 

