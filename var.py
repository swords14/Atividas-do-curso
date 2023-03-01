var
nome: caractere
nota1, nota2, nota3, media: real

Escrever("Digite o nome do aluno:" )
Ler(nome)

Escrever("Digite a primeira nota:" )
Ler(nota1)

Escrever("Digite a segunda nota:" )
Ler(nota2)

Escrever("Digite a terceira nota" )
Ler(nota3)

media <-(nota1 + nota2 + nota 3) / 3

Se media >= 7 Então

  Escrever("O aluno", nome, "Esta aprovado.")
Senão Se media >= 5.1 E media <= 6.9 Então
   Escrever ("O aluno", nome, "Esta em recuperação.")
   Senão
   Escrever("O aluno", nome, "Esta reprovado.")
   