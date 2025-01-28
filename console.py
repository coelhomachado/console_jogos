def adivinhacao():
  print("oi")
  import random
  alvo = random.randint(0,100)
  try:
    chute = int(input("Digite um numero inteiro entre 0 e 100:"))
    if chute == alvo:
      print("Você acertou o alvo!")
    else:
      #print("Você errou, o número era", str(alvo))
      print("Você errou, o número era", alvo)
  except:
    print("Número não é inteiro, tente novamente!")

def jokenpo():
  print("Hello")
  print("Este é um protótipo de um jogo Jokenpo")
  print("Insira sua jogada, lembrando que deve ser uma das seguintes opções:")
  print("Pedra, Papel ou Tesoura")
  print("Boa sorte!")
  import random
  opcoes = ["Pedra", "Papel", "Tesoura"]
  cpu = random.choice(opcoes)
  print(cpu)
  jogador = input("Digite sua jogada:")
  if cpu == jogador:
    print("Empate!")
  elif cpu == 'Pedra'and jogador == 'Papel':
    print("Você ganhou!")
  elif cpu == 'Pedra'and jogador == 'Tesoura':
    print("Você perdeu!")
  elif cpu == 'Papel'and jogador == 'Tesoura':
    print("Você ganhou!")
  elif cpu == 'Papel'and jogador == 'Pedra':
    print("Você perdeu!")
  elif cpu == 'Tesoura'and jogador == 'Pedra':
    print("Você ganhou!")
  elif cpu == 'Tesoura'and jogador == 'Papel':
    print("Você perdeu!")
  else:
    print("Opção inválida tente novamente!")

#def quiz():

opcao = input('''### CONSOLE DE JOGOS ###
# MENU PRINCIPAL #
Selecione uma opção:
1 - Adivinhação
2 - Jokenpo
3 - Quiz
''')
if opcao == '1':
  adivinhacao()
elif opcao == '2':
  jokenpo()
elif opcao == '3':
  quiz()
else:
  print("Opção inválida, tente novamente!")