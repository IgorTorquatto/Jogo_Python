#Módulos Python:
import pygame,sys
import time

#Módulos Pessoal:
import MOD_1
import MOD_2
import MOD_3

#Constantes Numéricas:
TELA_MENU_LARGURA = 1000
TELA_MENU_ALTURA = 630
TELA_JOGO_LARGURA = 1024
TELA_JOGO_ALTURA = 500
FONTE_TITULO = 30
FONTE_TEXTO = 10
FONTE_MAIN_MENU = 100
FONTE_BOTOES = 75
FONTE_BACK = 50
FONTE_SCORE = 15
VELOCIDADE_INICIAL = 0
VELOCIDADE_FINAL_MENU = 20
VELOCIDADE_JOGADOR = 2
CENTRALIZACAO_X = 0
CENTRALIZACAO_Y = 0
INCREMENTO_VELCOCIDADE_MENU = 1
INCREMENTO_DIFICULDADE = 10
OPTIONS_X = 540
OPTION_Y_1 = 100
OPTION_Y_2 = 250
OPTION_Y_3 = 400
OPTION_Y_4 = 550
RETANGULO_X = 500
RETANGULO_Y_1 = 15
RETANGULO_Y_2 = 60
RETANGULO_Y_3 = 80
RETANGULO_Y_4 = 100
RETANGULO_Y_5 = 600
SCORE_X = 800
SCORE_Y = 10
LOOP_MUSICA = 50
TEMPO_ANIMACAO = 0.25
CORRECAO_SEGUNDOS = 1000
ARREDONDAMENTO = 3
DIFICULDADE_INICIAL = 50
NUMERO_RETANGULOS = 30

#Constantes Load:
BACKGROUND = pygame.image.load("imagens/fundo - Copia.png")
IMAGEM_NAVE = pygame.image.load("imagens/nave.png")
EXPLOSAO = pygame.image.load("imagens/explosao.png")
MUSICA_MENU = "audios/Star Wars The Force Awakens _Force Theme_ [8 Bit Version North Pole Twin].ogg"
MUSICA_JOGO = "audios/musica.ogg"
SOM_EXPLOSAO = "audios/explosao2.ogg"
SOM_MOVIMENTACAO = "audios/som2.ogg"
FONTE_PADRAO = "assets/font.ttf"
FONTE_ARIAL = "Arial"
RETANGULO_PLAY = "assets/Play Rect.png"
RETANGULO_OPTIONS = "assets/Options Rect.png"
RETANGULO_QUIT = "assets/Quit Rect.png"


#Constantes Textos:
NOME_JOGO = "Escape From Earth"
TITULO = "Manual:"
VOLTAR = "VOLTAR"
PARAGRAFO_1 = "Use as setas do teclado para locomover a nave espacial e desviar dos objetos."
PARAGRAFO_2 = "O objetivo do jogo é desviar o máximo de tempo possível dos obstáculos."
PARAGRAFO_3 = "Para mudar a dificuldade do jogo use a tecla \"a\"."
MENU = "MENU"
JOGAR = "JOGAR"
MANUAL = "MANUAL"
SAIR = "SAIR"

#Cores:
BRANCO = "White"
PRETO = "Black"
VERDE = "Green"
AMARELO = "#b68f40"
VERDE_CLARO = "#d7fcd4"
LARANJA_RGB = (255,140,0)

#Menu:
def menu():

    pygame.init()

    SCREEN = pygame.display.set_mode((TELA_MENU_LARGURA, TELA_MENU_ALTURA))
    pygame.display.set_caption(NOME_JOGO)

    pygame.mixer.music.load(MUSICA_MENU)
    pygame.mixer.music.play(LOOP_MUSICA)

    def get_font(size):
        return pygame.font.Font(FONTE_PADRAO, size)

    def play():
        main()

    def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill(BRANCO)

            OPTIONS_TEXT = get_font(FONTE_TITULO).render(TITULO, True, PRETO)
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(RETANGULO_X, RETANGULO_Y_1))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_MANUAL = get_font(FONTE_TEXTO).render(PARAGRAFO_1,True,PRETO)
            OPTIONS_RECT2 = OPTIONS_MANUAL.get_rect(center=(RETANGULO_X, RETANGULO_Y_2))
            SCREEN.blit(OPTIONS_MANUAL, OPTIONS_RECT2)

            OPTIONS_MANUAL2 = get_font(FONTE_TEXTO).render(PARAGRAFO_2, True,PRETO)
            OPTIONS_RECT3 = OPTIONS_MANUAL2.get_rect(center=(RETANGULO_X, RETANGULO_Y_3))
            SCREEN.blit(OPTIONS_MANUAL2, OPTIONS_RECT3)

            OPTIONS_MANUAL3 = get_font(FONTE_TEXTO).render(PARAGRAFO_3, True,PRETO)
            OPTIONS_RECT3 = OPTIONS_MANUAL3.get_rect(center=(RETANGULO_X, RETANGULO_Y_4))
            SCREEN.blit(OPTIONS_MANUAL3, OPTIONS_RECT3)

            OPTIONS_BACK = MOD_1.Button(image=None, pos=(RETANGULO_X, RETANGULO_Y_5),
                                  text_input=VOLTAR, font=get_font(FONTE_BACK), base_color=PRETO, hovering_color=VERDE)

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
        
        XVEL=VELOCIDADE_INICIAL
        YVEL=VELOCIDADE_INICIAL

        nave = MOD_3.Player(IMAGEM_NAVE)
        nave2 = MOD_3.Player(IMAGEM_NAVE)
        nave3 = MOD_3.Player(IMAGEM_NAVE)
        nave4 = MOD_3.Player(IMAGEM_NAVE)
        nave5 = MOD_3.Player(IMAGEM_NAVE)
        nave6 = MOD_3.Player(IMAGEM_NAVE)

        while True:

            SCREEN.blit(BACKGROUND, (CENTRALIZACAO_X, CENTRALIZACAO_Y))
            XVEL+=INCREMENTO_VELCOCIDADE_MENU
            YVEL+=INCREMENTO_VELCOCIDADE_MENU


            if YVEL == VELOCIDADE_FINAL_MENU and XVEL == VELOCIDADE_FINAL_MENU:
                XVEL = -XVEL + INCREMENTO_VELCOCIDADE_MENU
                YVEL = -YVEL + INCREMENTO_VELCOCIDADE_MENU


            #Naves Animadas:

            nave.mover(XVEL,YVEL)
            nave2.mover(CENTRALIZACAO_X, YVEL)
            nave3.mover(-XVEL,YVEL)
            nave4.mover(-XVEL,-YVEL)
            nave5.mover(CENTRALIZACAO_X,-YVEL)
            nave6.mover(XVEL,-YVEL)

            time.sleep(TEMPO_ANIMACAO)

            #Mostrar as naves:
            nave.update(SCREEN)
            nave2.update(SCREEN)
            nave3.update(SCREEN)
            nave4.update(SCREEN)
            nave5.update(SCREEN)
            nave6.update(SCREEN)


            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(FONTE_MAIN_MENU).render(MENU, True, AMARELO)
            MENU_RECT = MENU_TEXT.get_rect(center=(OPTIONS_X, OPTION_Y_1))

            PLAY_BUTTON = MOD_1.Button( image= pygame.image.load(RETANGULO_PLAY), pos=(OPTIONS_X, OPTION_Y_2),
                                 text_input=JOGAR, font=get_font(FONTE_BOTOES), base_color=VERDE_CLARO, hovering_color=BRANCO)
            OPTIONS_BUTTON = MOD_1.Button(image=pygame.image.load(RETANGULO_OPTIONS), pos=(OPTIONS_X, OPTION_Y_3),
                                    text_input=MANUAL, font=get_font(FONTE_BOTOES), base_color=VERDE_CLARO,
                                    hovering_color=BRANCO)
            QUIT_BUTTON = MOD_1.Button(image=pygame.image.load(RETANGULO_QUIT), pos=(OPTIONS_X, OPTION_Y_4),
                                 text_input=SAIR, font=get_font(FONTE_BOTOES), base_color=VERDE_CLARO, hovering_color=BRANCO)

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

def colisao(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False


def main():
    import pygame

    tempo_menu = pygame.time.get_ticks()

    pygame.init()
    tela = pygame.display.set_mode((TELA_JOGO_LARGURA, TELA_JOGO_ALTURA))
    pygame.display.set_caption((NOME_JOGO))
    sair = False
    relogio = pygame.time.Clock()
    dificuldade = DIFICULDADE_INICIAL

    img_nave = IMAGEM_NAVE
    jogador = MOD_3.Player(img_nave)

    imagem_fundo = BACKGROUND
    imagem_explosao = EXPLOSAO

    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(LOOP_MUSICA)


    som_explosao = pygame.mixer.Sound(SOM_EXPLOSAO)
    som_mov = pygame.mixer.Sound(SOM_MOVIMENTACAO)

    vx, vy = VELOCIDADE_INICIAL, VELOCIDADE_INICIAL
    velocidade = VELOCIDADE_JOGADOR
    leftpress, rightpress, uppress, downpress = False, False, False, False

    texto = pygame.font.SysFont(FONTE_ARIAL,FONTE_SCORE, True, False)

    ret = MOD_2.Recs(NUMERO_RETANGULOS)
    colidiu = False

    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if colidiu == False:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        dificuldade+=INCREMENTO_DIFICULDADE

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
                        else:vx = VELOCIDADE_INICIAL

                    if event.key == pygame.K_RIGHT:
                        rightpress = False
                        if leftpress:vx = -velocidade
                        else:vx = VELOCIDADE_INICIAL

                    if event.key == pygame.K_UP:
                        uppress = False
                        if downpress:vx = velocidade
                        vy = VELOCIDADE_INICIAL

                    if event.key == pygame.K_DOWN:
                        downpress = False
                        if uppress:vx = -velocidade
                        vy = VELOCIDADE_INICIAL


        if colisao(jogador, ret):
            
            colidiu = True
            jogador.imagem = imagem_explosao
            pygame.mixer.music.stop()
            som_explosao.play()
            
         

        if colidiu == False:
            ret.mover()
            jogador.mover(vx, vy)

            tela.blit(imagem_fundo,(CENTRALIZACAO_X,CENTRALIZACAO_Y))
            segundos = (pygame.time.get_ticks()/CORRECAO_SEGUNDOS ) - tempo_menu/CORRECAO_SEGUNDOS
            segundos = round(segundos,ARREDONDAMENTO)
            segundos = str(segundos)
            contador = texto.render("Pontuação:{}".format(segundos), 0, LARANJA_RGB)
            tela.blit(contador, (SCORE_X, SCORE_Y))

        relogio.tick(dificuldade)

        ret.cor(tela)
        ret.recriar()
        jogador.update(tela)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    menu()
