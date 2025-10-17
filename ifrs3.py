"""3) Média final do aluno
Um professor resolveu utilizar quatro provas para testar o conhecimento dos alunos. Desenvolva um programa
que solicite ao usuário que informe as quatro notas de um aluno - valores positivos que podem conter até duas
casas decimais - e calcule a média final, apresentando esse resultado na tela. O cálculo utiliza a média aritmética,
conforme determinado nos exemplos abaixo.
Entrada: quatro valores positivo com até duas casas decimais, representando as quatro notas do aluno.
Saída: um valor positivo, com duas casas decimais, que representa a média aritmética entre as notas informadas
na entrada.
Exemplos de entrada e saída:"""

nota1 = float(input("Digite a primeira nota: ")) #pede que o usuario digite, converte no tipo de dado ponto flutuante e armazena o valor na variável nota1
nota2 = float(input("Digite a segunda nota: ")) #pede que o usuario digite, converte no tipo de dado ponto flutuante e armazena o valor na variável nota2
nota3 = float(input("Digite a terceira nota: ")) #pede que o usuario digite, converte no tipo de dado ponto flutuante e armazena o valor na variável nota3
nota4 = float(input("Digite a quarta nota: ")) #pede que o usuario digite, converte no tipo de dado ponto flutuante e armazena o valor na variável nota4
print(nota1,nota2,nota3,nota4) #exibe as notas informadas pelo usuario que estão armazenadas como nota1,nota2,nota3 e nota4.

somar_media = (nota1 + nota2 + nota3 + nota4) / 4 # soma todas as notas, divide pelo número de notas e armazena na variável somar_media

print("A média das 4 notas informadas é: ", somar_media) #Exibe a string e concatena com a variavel somar_media