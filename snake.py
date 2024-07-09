# Instalar a biblioteca pygame
import random
import pygame

pygame.init()
resolucao = (500, 500)                                              # Criando a tela do Jogo em pixels
screen = pygame.display.set_mode(resolucao)
pygame.display.set_caption('Jogo da Cobrinha')
preto = (0, 0, 0)                                                   # Cores em RGB para o fundo da tela.
clock = pygame.time.Clock()                                         # Adicionando limitador de fps

class Snake:                                                        # Classe que define a cobra no jogo.
    cor = (255, 255, 255)                                           # Cor branca (em RGB) para a cobra.
    tamanho = (10, 10)                                              # Tamanho de cada segmento da cobra.
    velocidade = 10                                                 # Defiindo a velocidade da cobrinha.
    tamanho_maximo = 49 * 49

    def __init__(self):                                             # Método inicializador da classe.
        self.textura = pygame.Surface(self.tamanho)                 # Criando uma superfície para cada pixel da cobra.
        self.textura.fill(self.cor)                                 # Preenchendo a superfície com a cor branca.

        self.corpo = [ (100, 100),(90, 100), (80, 100)]             # Lista que define a posição inicial da cobra.

        self.direcao ='direita'

        self.pontos = 0

    def blit(self, screen):                                         # Método para desenhar a cobra na tela.
        for posicao in self.corpo:                                  # Percorre cada posição do corpo da cobra.
            screen.blit(self.textura, posicao)                      # Desenha o segmento da cobra na tela na posição especificada.

    def andar(self):                                                # Método para mover a cobra na direção atual.
        cabeca = self.corpo[0]                                      # A cabeça da cobra é o primeiro segmento na lista do corpo.
        x = cabeca[0]                                               # Cordenadas da cabeca
        y = cabeca[1]

        if self.direcao == 'direita':                               # Lógica para mover na direção indicada.
            self.corpo.insert(0, (x + self.velocidade, y))
        elif self.direcao == 'esquerda':
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direcao == 'cima':
            self.corpo.insert(0,(x, y - self.velocidade))
        elif self.direcao == 'baixo':
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):                                                 # Métodos para mudar a direção da cobra.
        if self.direcao != 'baixo':                                 # Verifica se a direção atual não é para baixo para evitar o movimento contrário.
            self.direcao = 'cima'                                   # Definição da direção da cobra.

    def baixo(self):
        if self.direcao != 'cima':
            self.direcao = 'baixo'

    def esquerda(self):
        if self.direcao != 'direita':
            self.direcao = 'esquerda'

    def direita(self):
        if self.direcao != 'esquerda':
            self.direcao = 'direita'

    def colisao_frutinha(self, frutinha):                            # Método para verificar colisão com a frutinha.
        return self.corpo[0] == frutinha.posicao                     # Retorna VERDADEIRO se a cabeça da cobra estiver na mesma posição da frutinha.

    def comer(self):                                                  # Método para aumentar o tamanho da cobra ao comer uma frutinha.
        self.corpo.append((0, 0))                                     # Adiciona mais um elemento à cobra.
        self.pontos += 1                                              # Aumenta a pontuação.
        pygame.display.set_caption(f'Jogo da Cobrinha || Pontos: {self.pontos} ' )  # Atualiza o título da janela com a nova pontuação.


    def colisao(self):                                                  # Método para verificar colisões.
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        calda = self.corpo[1:]                                       # O restante do corpo da cobra, excluindo a cabeça.

        return x < 0 or y < 0 or x > 490 or y > 490 or cabeca in calda or len(self.corpo) > self.tamanho_maximo  # Identificando se a cobrinha está batendo com alguma parte das paredes em seu corpo ou se atingiu o tamanho maximo permitido.

    def auto_colisao(self):                                             # Método para verificar colisão com a propria cobra
        return self.corpo[0] in self.corpo[1:]

class Frutinha:                                                     # Definindo a frutinha no jogo.
    cor = (255, 0, 0)                                               # Atribuindo a cor vermelha (em RGB) a a variavel cor.
    tamanho = (10, 10)                                              # Definindo o tamanho para a frutinha.
    def __init__(self, cobrinha):                                   # Método inicializador da classe.
        self.textura = pygame.Surface(self.tamanho)                 # Criando um quandrado para a frutinha e atibuindo o tamanho da mesma.
        self.textura.fill(self.cor)                                 # Atribuindo a cor da variavel ao elemento.

        self.posicao = Frutinha.criar_posicao(cobrinha)             # Definindo a posição da frutinha.

    @staticmethod
    def criar_posicao(cobrinha):
        x = random.randint(0, 49) * 10                         # Deixando a frutinha em uma posição randomica nos eixos x e y.
        y = random.randint(0, 49) * 10

        if (x, y) in cobrinha.corpo:                                # Verifica se a nova posição da frutinha está no corpo da cobra.
            frutinha.criar_posicao(cobrinha)                        # Se estiver, chama o método para criar uma nova posição.
        else:
            return (x, y)                                           # Se não estiver, retorna a posição válida da frutinha.
    def blit(self, screen):
        screen.blit(self.textura, self.posicao)                     # Desenhando a frutinha na tela na posição especificada.

cobrinha = Snake()                                                  # Criando a cobrinha.
frutinha = Frutinha(cobrinha)                                       # Criando a frutinha, passando a cobra como parâmetro para evitar a frutinha nascer em cima da cobra.

frutinha.blit(screen)                                               # Desenha a frutinha na tela.


while True:
    clock.tick(10)                                                  # Limitando a velocidade da cobrinha a 20 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                               # Evento para sair do jogo ao clicar no X de fechar o programa.
            exit()

        if event.type == pygame.KEYDOWN:                            # Verificando qual tecla foi precionada
            if event.key == pygame.K_UP:                            # e mundado a direção de acordo com a tecla precionada.
                cobrinha.cima()
                break
            elif event.key == pygame.K_DOWN:
                cobrinha.baixo()
                break
            elif event.key == pygame.K_LEFT:
                cobrinha.esquerda()
                break
            elif event.key == pygame.K_RIGHT:
                cobrinha.direita()
                break




    if cobrinha.colisao_frutinha(frutinha):                         # Verifica se a cobra colidiu com a frutinha.
        cobrinha.comer()                                            # Aumenta o tamanho da cobra e atualiza a pontuação.
        frutinha = Frutinha(cobrinha)                                # Gera uma nova frutinha em uma posição aleatória.

    if cobrinha.colisao():                                          # Verifica se a cobra colidiu com a parede ou consigo mesma.
        cobrinha = Snake()                                          # Reinicia o jogo criando uma nova cobra.

    cobrinha.andar()                                                # Move a cobra na direção atual.

    screen.fill(preto)                                              # Definindo a cor da tela como preta
    frutinha.blit(screen)                                           # Desenha a frutinha na tela.
    cobrinha.blit(screen)                                           # Desenha a cobrinha na tela.

    pygame.display.update()                                         # Atualizando a tela para exibir a frutinha e a cobra.


