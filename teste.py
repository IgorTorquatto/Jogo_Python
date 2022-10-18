import pygame

def main():
    pygame.init()
    pygame.display.set_mode([300,300])
    pygame.display.set_caption(("Iniciando Pygame"))
    sair = False

    while sair != True:
        #Receber com o get o evento para sair e trocar a variável sair para True.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

    #Com a variável sair == True vai fechar o programa:
    pygame.quit()





main()