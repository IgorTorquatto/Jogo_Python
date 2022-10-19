#Jogo sendo desenvolvido por Cícero Igor Alves Torquato dos Santos
import pygame

def main():
    #As definições dos objetos (variáveis):
    pygame.init()
    tela = pygame.display.set_mode([300,300])
    pygame.display.set_caption(("Iniciando Pygame"))
    relogio = pygame.time.Clock()

    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (152,231,114)
    cor_vermelha = (227,57,9)

    sup = pygame.Surface((200,200))
    sup.fill((cor_azul))

    sup2 = pygame.Surface((100, 100))
    sup2.fill((cor_verde))

    ret = pygame.Rect(10,10,45,45)

    sair = False

    while sair != True:
        #Receber com o get o evento para sair e trocar a variável sair para True.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #ret = ret.move(10,10)

            #if event.type == pygame.MOUSEMOTION:
                #ret = ret.move(-10,-10)

            if event.type == pygame.KEYDOWN:  #Se alguma tecla foi pressionada:
                if event.key == pygame.K_LEFT: # Eixo x y
                    ret.move_ip(-10,0)

                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10,0)

                if event.key == pygame.K_UP:
                    ret.move_ip(0,-10)

                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,10)

                if event.key == pygame.K_SPACE:
                    ret.move_ip(10,10)

                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10,-10)

        #Timing para otimizar processamento e colocando cor branca como tela de fundo:
        relogio.tick(27)
        tela.fill(cor_branca)

        #Passar a superficie e as posições no eixo x e y.
        tela.blit(sup,[50,50])
        tela.blit(sup2,[250,50])
        tela.blit(sup2, [250, 150])

        pygame.draw.rect(tela,cor_vermelha,ret)
        pygame.display.update()

    #Com a variável sair == True vai fechar o programa:
    pygame.quit()





main()