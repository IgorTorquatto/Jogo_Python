import pygame,sys
import random
import time


class Recs(object):
    def __init__(self, numeroinicial):
        self.lista = []  #Guarda os retângulos criados.
        for x in range(numeroinicial):  #Percorre até o numeroincial que é a quantidade de retângulos que queremos criar.
            leftrandom = random.randrange(2, 1100) # Passa um pouco da tela para testes. #(2,560)
            toprandom = random.randrange(-1124, -10) #(-580,-10)
            width = random.randrange(10, 30) #Largura #(10,30)
            height = random.randrange(15, 30) #(15,30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height)) #Colocando rects na lista com as variáveis definidas.


    def mover(self):
        for retangulo in self.lista: #Lista pertence a classe então devemos acessá-lo por self.lista
            retangulo.move_ip(0, 2)
                            

    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165,214,254),retangulo) #Desenhando retãngulo na cor azul.

    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481: #Se a lista na posição do retângulo ( Parte superior) passar da tela recria.

                leftrandom = random.randrange(2, 1100) #(2,560)
                toprandom = random.randrange(-1124, -10) #(-580,-10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))  #Recria assim que um retângulo passa da tela, se fosse o append ia ficar criando retângulos sempre.
        
#Estruturado:
class Player(pygame.sprite.Sprite):
    #1-Preparar um objeto (imagem) inserir numa area retangular e posicionar na tela.
    def __init__(self, imagem): #Método construtor
        self.imagem = imagem #Vamos passar a imagem posteriormente
        self.rect = self.imagem.get_rect()  #Captura a area retangular para ser usada
        self.rect.top, self.rect.left = (315, 500)  #Antigo:400X480

    def mover(self, vx, vy):  #Objeto principal self + referências
        self.rect.move_ip(vx, vy) #Como a imagem está dentro do retângulo podemos mover apenas o retângulo com velocidades x e y.
    #3- Atualizar um objeto (superficie)
    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)


def colisao(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec): #Testa colisão.
            return True
    return False


def main():
    import pygame
    #main usa a classe player por isso não pode estar dentro dessa classe.
    #Declaração das váriaveis (objetos)
    pygame.init()
    tela = pygame.display.set_mode((1024, 500))  #480,300
    pygame.display.set_caption(("Escape from Earth"))
    sair = False
    relogio = pygame.time.Clock() #Velocidade da tela , em quantos quadros ela é renderizada.
    dificuldade = 50

    img_nave = pygame.image.load("imagens/nave.png").convert_alpha() #Imagem deve ser png, sem fundo branco, para não bugar colisão. Converte para ter uma certa transparência suave de fundo.
    jogador = Player(img_nave) #Classe Player criada , dar referência que a imagem da nave será o jogador em si . Quando criar a area retangular vai colocar nela a imagem e essa imagem é o player.

    imagem_fundo = pygame.image.load("imagens/fundo - Copia.png").convert_alpha()
    imagem_explosao = pygame.image.load("imagens/explosao.png").convert_alpha()

    pygame.mixer.music.load("audios/musica.mp3")
    pygame.mixer.music.play(3)

    som_explosao = pygame.mixer.Sound("audios/explosao2.wav")
    som_mov = pygame.mixer.Sound("audios/som2.wav")

    vx, vy = 0,0 #velocidade inicial
    velocidade = 2 # o quanto que ele vai se deslocar quando pressionarmos o botão em pixel.
    leftpress, rightpress, uppress, downpress = False, False, False, False

    texto = pygame.font.SysFont("Arial", 15, True, False)

    ret = Recs(30) #passando o numeroincial de 30 para criar os retângulos
    colidiu = False

    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Evento de tela : Se o usuário clicar no X ele quita do game.
                sair = True

            if colidiu == False:

                if event.type == pygame.KEYDOWN:  #Evento de teclado: Se a tecla for pressionada.

                    if event.key == pygame.K_LSHIFT:
                        #if velocidade > 1:
                          #  velocidade -= 0.5
                        #print(velocidade)
                        dificuldade+=10

                    if event.key == pygame.K_LEFT:
                        leftpress = True
                        vx = - velocidade  #-10 eixo x

                    if event.key == pygame.K_RIGHT:
                        rightpress = True
                        vx = velocidade  #10 eixo x

                    if event.key == pygame.K_UP:
                        uppress = True
                        vy = - velocidade  # -10 no eixo y (sendo que para subir é negativo mesmo).
                        som_mov.play()   #A função play roda o som.

                    if event.key == pygame.K_DOWN:
                        downpress = True
                        vy = velocidade  # 10 eixo y

                if event.type == pygame.KEYUP: #Evento de Teclado: Verifica se você soltou a tecla.
                    if event.key == pygame.K_LEFT:
                        leftpress = False
                        if rightpress:vx = velocidade #para corrigir troca de sentidos, melhora movimentação e velocidade da movimentação.
                        else:vx = 0

                    if event.key == pygame.K_RIGHT:
                        rightpress = False
                        if leftpress:vx = -velocidade
                        else:vx = 0

                    if event.key == pygame.K_UP:
                        uppress = False
                        if downpress:vx = velocidade
                        vy = 0

                    if event.key == pygame.K_DOWN:
                        downpress = False
                        if uppress:vx = -velocidade
                        vy = 0


        if colisao(jogador, ret):
            
            colidiu = True
            jogador.imagem = imagem_explosao
            pygame.mixer.music.stop()
            som_explosao.play()
            
         

        if colidiu == False:
            ret.mover()
            jogador.mover(vx, vy)

            tela.blit(imagem_fundo,(0,0)) #O blit coloca na tela, passamos o objeto e a posição. (0,0) zero em x e em y centralizado.
            #segundos = pygame.time.get_ticks()/1000
            #segundos = str(segundos)
           # contador = texto.render("Pontuação:{}".format(segundos), 0, (255,140,0)) #Cor laranja em RGB
            #tela.blit(contador, (800, 10)) #320,10
                    

        relogio.tick(dificuldade)  #Atualização 20 frames por segundo. Velocidade do Game.
        #tela.blit(imagem_fundo,(0,0))
        
        #ret.mover()
        ret.cor(tela) #Desenha o retângulo
        ret.recriar()
        jogador.update(tela)
        #jogador.mover(vx, vy)
        
        
        

        pygame.display.update() #Atualizando enquanto a tela está aberta

    pygame.quit() #sair ==  True

def menu():

    class Button():
        def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                return True
            return False

        def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)

    pygame.init()

    WIDTH = 1000
    HEIGHT = 630  #650
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #1000,650
    pygame.display.set_caption("Escape from Earth")


    BG = pygame.image.load("imagens/fundo - Copia.png")

    #Imagem da nave para animação no menu:
    img_photo = pygame.image.load("imagens/nave.png").convert_alpha()


    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def play():
        main()

    def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = get_font(30).render("Manual:", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 15))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_MANUAL = get_font(10).render("Use as setas do teclado para locomover a nave espacial e desviar dos objetos.",True,"Black")
            OPTIONS_RECT2 = OPTIONS_MANUAL.get_rect(center=(500, 60))
            SCREEN.blit(OPTIONS_MANUAL, OPTIONS_RECT2)

            OPTIONS_MANUAL2 = get_font(10).render("O objetivo do jogo é desviar o máximo de tempo possível dos obstáculos.", True, "Black")
            OPTIONS_RECT3 = OPTIONS_MANUAL2.get_rect(center=(500, 80))
            SCREEN.blit(OPTIONS_MANUAL2, OPTIONS_RECT3)

            OPTIONS_MANUAL3 = get_font(10).render("Para mudar a dificuldade do jogo use a tecla Shift da esquerda.", True, "Black")
            OPTIONS_RECT3 = OPTIONS_MANUAL3.get_rect(center=(500, 100))
            SCREEN.blit(OPTIONS_MANUAL3, OPTIONS_RECT3)

            OPTIONS_BACK = Button(image=None, pos=(500, 600),
                                  text_input="VOLTAR", font=get_font(50), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def main_menu():

        XVEL=0
        YVEL=0

        # Naves para animação do menu:

        nave = Player(img_photo)
        nave2 = Player(img_photo)
        nave3 = Player(img_photo)
        nave4 = Player(img_photo)
        nave5 = Player(img_photo)
        nave6 = Player(img_photo)

        #coordenadas = [500,315]
        while True:

            SCREEN.blit(BG, (0, 0))
            XVEL+=1
            YVEL+=1

            # 29, 30 tamanho nave na hor e vert



            #Lembrando : SCREEN: 1000 X 650 ; BACKGROUND: 1024 X 640 ; NAVE( Inicia em): 500 X 315
            #Corrigindo bugs -> Temos que lembrar que o XVEL até 20 toca no canto da tela, porém temos que colocar 21 por conta da correção de índice
            #na subida, ou seja , quando a variável recebe o negativo dela temos que somar 1 para que ele sempre volte de onde ele partiu e não fique voltando antes.
            if YVEL == 23 and XVEL == 23:
                XVEL = -XVEL +1
                YVEL = -YVEL +1



            #Naves Animadas:
            nave.mover(XVEL,YVEL)
            nave2.mover(0, YVEL)
            nave3.mover(-XVEL,YVEL)
            nave4.mover(-XVEL,-YVEL)
            nave5.mover(0,-YVEL)
            nave6.mover(XVEL,-YVEL)

            time.sleep(0.2)
            print(XVEL,YVEL)

            #Mostrar as naves:
            nave.update(SCREEN)
            nave2.update(SCREEN)
            nave3.update(SCREEN)
            nave4.update(SCREEN)
            nave5.update(SCREEN)
            nave6.update(SCREEN)


            #

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(540, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(540, 250),
                                 text_input="JOGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(540, 400),
                                    text_input="MANUAL", font=get_font(75), base_color="#d7fcd4",
                                    hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(540, 550),
                                 text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    main_menu()

if __name__ == "__main__":
   menu()

