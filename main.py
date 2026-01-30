'''
Main for Maz-Rogue game.
'''
import pygame
import sys

pygame.init()


def main():
    '''
    Funcion que crea el componente inicial para empezar el juego.
    '''
    display = (800, 600)
    caption = "Maz-Rogue Game!"

    window = pygame.display.set_mode(display)
    pygame.display.set_caption(caption)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == '__main__':
    main()
