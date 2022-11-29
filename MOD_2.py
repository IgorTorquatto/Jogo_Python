#Retângulos
import random
import pygame

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
            pygame.draw.rect(superficie, (165, 214, 254), retangulo)

    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481:
                leftrandom = random.randrange(2, 1100)
                toprandom = random.randrange(-1124, -10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))
