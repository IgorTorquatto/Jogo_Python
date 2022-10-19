#Jogo sendo desenvolvido por Cícero Igor Alves Torquato dos Santos
import pygame
import random

#Estruturado:
class Player(pygame.sprite.Sprite):
    #1-Preparar um objeto (imagem) inserir numa area retangular e posicionar na tela.
    def __init__(self, imagem): #Método construtor
        self.imagem = imagem #Vamos passar a imagem posteriormente
        self.rect = self.imagem.get_rect()  #Captura a area retangular para ser usada
        self.rect.top, self.rect.left = (100, 200)  #posições do retângulo 100 do topo 200 a esquerda

    def mover(self, vx, vy):  #Objeto principal self + referências
        self.rect.move_ip(vx, vy)
    #3- Atualizar um objeto (superficie)
    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

def main():
    import pygame
    #main usa a classe player por isso não pode estar dentro dessa classe.
    #Declaração das váriaveis (objetos)
    pygame.init()
    tela = pygame.display.set_mode((480, 300))
    sair = False
    relogio = pygame.time.Clock() #Velocidade da tela , em quantos quadros ela é renderizada.

    img_nave = pygame.image.load("imagens/nave.png").convert_alpha() #Imagem deve ser png, sem fundo branco, para não bugar colisão. Converte para ter uma certa transparência suave de fundo.
    jogador = Player(img_nave) #Classe Player criada , dar referência que a imagem da nave será o jogador em si . Quando criar a area retangular vai colocar nela a imagem e essa imagem é o player.

    
    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Se o usuário clicar no X ele quita do game.
                sair = True
        

        relogio.tick(20)  #Atualização 20 frames por segundo.
        #tela.blit(imagem_fundo,(0,0))
        
        #ret.mover()
        ret.cor(tela)
        ret.recriar()
        jogador.update(tela)
        #jogador.mover(vx, vy)
        
        
        

        pygame.display.update() #Atualizando enquanto a tela está aberta

    pygame.quit() #sair ==  True

main()