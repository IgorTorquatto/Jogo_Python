import pygame,sys
import random
import time

#Menu:
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
    HEIGHT = 630
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Escape from Earth")


    BG = pygame.image.load("imagens/fundo - Copia.png")


    img_photo = pygame.image.load("imagens/nave.png").convert_alpha()

    pygame.mixer.music.load("audios/Star Wars The Force Awakens _Force Theme_ [8 Bit Version North Pole Twin].ogg")
    pygame.mixer.music.play(50)

    def get_font(size):
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

            OPTIONS_MANUAL3 = get_font(10).render("Para mudar a dificuldade do jogo use a tecla \"a\".", True, "Black")
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


        nave = Player(img_photo)
        nave2 = Player(img_photo)
        nave3 = Player(img_photo)
        nave4 = Player(img_photo)
        nave5 = Player(img_photo)
        nave6 = Player(img_photo)


        while True:

            SCREEN.blit(BG, (0, 0))
            XVEL+=1
            YVEL+=1


            if YVEL == 20 and XVEL == 20:
                XVEL = -XVEL +1
                YVEL = -YVEL +1


            #Naves Animadas:
            nave.mover(XVEL,YVEL)
            nave2.mover(0, YVEL)
            nave3.mover(-XVEL,YVEL)
            nave4.mover(-XVEL,-YVEL)
            nave5.mover(0,-YVEL)
            nave6.mover(XVEL,-YVEL)

            time.sleep(0.25)

            #Mostrar as naves:
            nave.update(SCREEN)
            nave2.update(SCREEN)
            nave3.update(SCREEN)
            nave4.update(SCREEN)
            nave5.update(SCREEN)
            nave6.update(SCREEN)


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


#Jogo:
class Recs(object):
    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2, 1100)
            toprandom = random.randrange(-1124, -10)
            width = random.randrange(10, 30)
            height = random.randrange(15, 30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height))


    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0, 2)
                            

    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165,214,254),retangulo)

    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481:

                leftrandom = random.randrange(2, 1100)
                toprandom = random.randrange(-1124, -10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))
        
#Estruturado:
class Player(pygame.sprite.Sprite):

    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (315, 500)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)


def colisao(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False


def main():
    import pygame

    tempo_menu = pygame.time.get_ticks()

    pygame.init()
    tela = pygame.display.set_mode((1024, 500))
    pygame.display.set_caption(("Escape from Earth"))
    sair = False
    relogio = pygame.time.Clock()
    dificuldade = 50

    img_nave = pygame.image.load("imagens/nave.png").convert_alpha()
    jogador = Player(img_nave)

    imagem_fundo = pygame.image.load("imagens/fundo - Copia.png").convert_alpha()
    imagem_explosao = pygame.image.load("imagens/explosao.png").convert_alpha()

    pygame.mixer.music.load("audios/musica.ogg")
    pygame.mixer.music.play(10)

    som_explosao = pygame.mixer.Sound("audios/explosao2.ogg")
    som_mov = pygame.mixer.Sound("audios/som2.ogg")

    vx, vy = 0,0
    velocidade = 2
    leftpress, rightpress, uppress, downpress = False, False, False, False

    texto = pygame.font.SysFont("Arial", 15, True, False)

    ret = Recs(30)
    colidiu = False

    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if colidiu == False:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        dificuldade+=10

                    if event.key == pygame.K_LEFT:
                        leftpress = True
                        vx = - velocidade

                    if event.key == pygame.K_RIGHT:
                        rightpress = True
                        vx = velocidade

                    if event.key == pygame.K_UP:
                        uppress = True
                        vy = - velocidade
                        som_mov.play()

                    if event.key == pygame.K_DOWN:
                        downpress = True
                        vy = velocidade

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftpress = False
                        if rightpress:vx = velocidade
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

            tela.blit(imagem_fundo,(0,0))
            segundos = (pygame.time.get_ticks()/1000 ) - tempo_menu/1000
            segundos = round(segundos,3)
            segundos = str(segundos)
            contador = texto.render("Pontuação:{}".format(segundos), 0, (255,140,0)) #Cor laranja em RGB
            tela.blit(contador, (800, 10)) 

        relogio.tick(dificuldade)

        ret.cor(tela)
        ret.recriar()
        jogador.update(tela)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    menu()
