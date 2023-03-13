 N     c lass Aluno:
  def __init__(self, nome, notas):
    self.nome = nome
    self.notas = notas
  
  def media(self):
    return sum(self.notas) / len(self.notas)

alunos = [
  Aluno("João", [7, 8, 9]),
  Aluno("Maria", [8, 9, 10]),
  Aluno("José", [5, 6, 7])
]

for aluno in alunos:
  print(f"Nome: {aluno.nome}")
  print(f"Média: {aluno.media():.2f}")


