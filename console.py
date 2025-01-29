import adivinhacao
import jokenpo
import quiz
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
    adivinhacao.adivinhacao()
  elif opcao == '2':
    jokenpo.jokenpo()
  elif opcao == '3':
    quiz.quiz()
  elif opcao == '0':
    executar = False
    print("Obrigado, volte sempre!")
  else:
    print("Opção inválida, tente novamente!")