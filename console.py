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
  #print(cpu)
  jogador = input("Digite sua jogada:")
  if cpu == jogador:
    print("Empate!")
  elif cpu == 'Pedra'and jogador == 'Papel':
    print("Você ganhou!")
  elif cpu == 'Pedra'and jogador == 'Tesoura':
    print("Você perdeu,", cpu, "venceu!")
  elif cpu == 'Papel'and jogador == 'Tesoura':
    print("Você ganhou!")
  elif cpu == 'Papel'and jogador == 'Pedra':
    print("Você perdeu,", cpu, "venceu!")
  elif cpu == 'Tesoura'and jogador == 'Pedra':
    print("Você ganhou!")
  elif cpu == 'Tesoura'and jogador == 'Papel':
    print("Você perdeu,", cpu, "venceu!")
  else:
    print("Opção inválida tente novamente!")

def quiz():
  resposta = input("Qual é o principal vilão dos filmes Star Wars?")
  if resposta == 'Dart Vader':
    print("Parabéns, você acertou!")
  else:
    print("Que pena, você errou!")

executar = True
while executar == True:
  opcao = input('''### CONSOLE DE JOGOS ###
  # MENU PRINCIPAL #
  Selecione uma opção:
  1 - Adivinhação
  2 - Jokenpo
  3 - Quiz
  0 - SAIR
  ''')
  if opcao == '1':
    adivinhacao()
  elif opcao == '2':
    jokenpo()
  elif opcao == '3':
    quiz()
  elif opcao == '0':
    executar = False
    print("Obrigado, volte sempre!")
  else:
    print("Opção inválida, tente novamente!")