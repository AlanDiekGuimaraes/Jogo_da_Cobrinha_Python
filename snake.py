# Instalar a biblioteca pygame
import random
import pygame

pygame.init()
resolucao = (500, 500)                                      # Criando a tela do Jogo em pixels
screen = pygame.display.set_mode(resolucao)

preto = (0, 0, 0)                                        # Cores em RGB para o fundo da tela.
screen.fill(preto)                                       # Definindo a cor da tela como preta
pygame.display.update()                                  # Atualizando a tela para aplicar a cor definida.

class Frutinha:                                      # Definindo a frutinha no jogo.
    cor = (255, 0, 0)                                # Atribuindo a cor vermelha (em RGB) a a variavel cor.
    tamanho = (10, 10)                               # Definindo o tamanho para a frutinha.


    def __init__(self):
        self.textura = pygame.Surface(self.tamanho) # Criando um quandrado para a frutinha e atibuindo o tamanho da mesma.
        self.textura.fill(self.cor)                 # Atribuindo a cor da variavel ao elemento.

        x = random.randint(0, 49) * 10         # Deixando a frutinha em uma posição randomica nos eixos x e y.
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)                        # Definindo a posição da frutinha.

frutinha = Frutinha()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                   # Evento para sair do jogo ao clicar no X de fechar o programa.
            exit()

    screen.blit(frutinha.textura, frutinha.posicao)     # Desenhando a frutinha na tela na posição especificada.
    pygame.display.update()                             # Atualizando a tela para exibir a frutinha.