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