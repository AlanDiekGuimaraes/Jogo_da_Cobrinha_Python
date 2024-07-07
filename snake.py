# Instalar a biblioteca pygame
import random
import pygame

pygame.init()
resolucao = (500, 500)                                              # Criando a tela do Jogo em pixels
screen = pygame.display.set_mode(resolucao)

preto = (0, 0, 0)                                                   # Cores em RGB para o fundo da tela.
screen.fill(preto)                                                  # Definindo a cor da tela como preta
pygame.display.update()                                             # Atualizando a tela para aplicar a cor definida.


class Snake:                                                        # Classe que define a cobra no jogo.
    cor = (255, 255, 255)                                           # Cor branca (em RGB) para a cobra.
    tamanho = (10, 10)                                              # Tamanho de cada segmento da cobra.

    def __init__(self):                                             # Método inicializador da classe.
        self.textura = pygame.Surface(self.tamanho)                 # Criando uma superfície para cada pixel da cobra.
        self.textura.fill(self.cor)                                 # Preenchendo a superfície com a cor branca.

        self.corpo = [(100, 100),(90, 100), (80, 100) ]             # Lista que define a posição inicial da cobra.


class Frutinha:                                                     # Definindo a frutinha no jogo.
    cor = (255, 0, 0)                                               # Atribuindo a cor vermelha (em RGB) a a variavel cor.
    tamanho = (10, 10)                                              # Definindo o tamanho para a frutinha.
    def __init__(self):                                             # Método inicializador da classe.
        self.textura = pygame.Surface(self.tamanho)                 # Criando um quandrado para a frutinha e atibuindo o tamanho da mesma.
        self.textura.fill(self.cor)                                 # Atribuindo a cor da variavel ao elemento.

        x = random.randint(0, 49) * 10                        # Deixando a frutinha em uma posição randomica nos eixos x e y.
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)                                       # Definindo a posição da frutinha.


frutinha = Frutinha()
cobrinha = Snake()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                               # Evento para sair do jogo ao clicar no X de fechar o programa.
            exit()

    screen.blit(frutinha.textura, frutinha.posicao)                 # Desenhando a frutinha na tela na posição especificada.

    for posicao in cobrinha.corpo:
        screen.blit(cobrinha.textura, posicao)
    pygame.display.update()                                         # Atualizando a tela para exibir a frutinha.