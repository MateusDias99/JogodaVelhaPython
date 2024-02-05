import random
import os
LARGURA = 80

lista_palavras = [
    "PITANGA",
    "SALSICHA",
    "COTOVELO",
    "MOTOR",
    "CELULA",
    "TAMARINDO",
    "RODINHA",
    "SIRENE"
]
lista_letras_corretass = []
lista_letras_corretas = set()
lista_tentativas = set()

# Sistema sorteia uma palavra e define as chances
palavra_sorteada = random.choice(lista_palavras)

# Define a quantidade de chances usando a quantidade de letras da palavra
quantidade_chances = 4



# Sistema mostra regras do jogo
print(f"Bem-vindo ao jogo da forca!".center(LARGURA))
print(f"Você tem {quantidade_chances} chances para acertar a palavra.".center(LARGURA))
print(f"Você pode chutar uma letra ou a palavra inteira.".center(LARGURA))
print(f"Caso erre a palavra, você perde o jogo!".center(LARGURA))
print(f"Boa sorte!".center(LARGURA, "*"))

input("Pressione ENTER para começar...")

# Sistema limpa a tela
os.system("cls")

# Jogador pode dar palpites até acabarem as chances
while quantidade_chances > 0:
    os.system("cls")
    # Sistema desenha a forca
    print("Tentativas restantes:", quantidade_chances)
    print("Tentativas Acertivas = ", " - ".join(lista_letras_corretas))
    print("Tentativas = ", " - ".join(lista_tentativas))

    if (quantidade_chances == 4):
      print("o<-<")
      print()
      print ("Socoooro...")
    elif (quantidade_chances == 4-1):
       print("o<-")  
       print()
       print ("Aiii meu pé...")
    elif (quantidade_chances == 4-2):
        print("o<")
        print()
        print ("Uii meu corpinho...")
    elif (quantidade_chances == 4-3):
        print("o_0 Ultima chance...")
        print()
        print ("jesussss maria josé...")

    falta_letras = False

    for letra in palavra_sorteada:

        # Verifica se a letra está na lista de letras corretas
        if letra in lista_letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            falta_letras = True

    # Quebra a linha
    print("\n")

    # Verifica se o jogador acertou todas as letras
    if not falta_letras:
        quantidade_chances = 0
        perdeu = False
        # Sai do loop while
        break

    # Usuário chuta uma palavra ou letra
    palpite = input("Digite uma letra ou a palavra: ").upper()

    if len(palpite) > 1:
        # é uma palavra
        if not palpite == palavra_sorteada:
            quantidade_chances = 0
            perdeu = True
        else:
            quantidade_chances = 0
            perdeu = False
    else:
        # é uma letra
        acertou = False
        for letra in palavra_sorteada:
            if letra == palpite:
                acertou = True
                lista_letras_corretass.append(letra)

        if not acertou:
            quantidade_chances -= 1
            perdeu = True
    
    for corretas in palavra_sorteada:
        if corretas == palpite:
            lista_letras_corretas.add(palpite)
    for incorretas in palavra_sorteada:
        if incorretas != palpite:
            lista_tentativas.add(palpite)

if not perdeu:
    print("Parabéns! Você acertou a palavra!\n") 
else:
    print("MORTO |-o<-<\nQue pena! Você perdeu! A palavra era", palavra_sorteada)