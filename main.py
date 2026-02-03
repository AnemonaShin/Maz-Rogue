'''
Main for Maz-Rogue game.
'''
import sys
import time
import pygame
import pygame.freetype

pygame.init()


def color(key):
    '''
    Funcion que extrae un color desde la libreria THECOLORS de Pygame.
    En caso de no traer nada devuelve el color blanco.
    :param key: Color a extraer
    '''
    if key in pygame.colordict.THECOLORS:
        return pygame.Color(key)
    else:
        return pygame.Color("white")


def text_generator(text, text_color):
    '''
    Crea un texto segun la fuente oficial del proyecto.

    :param text: Texto a crear
    :param text_color: Color del texto
    '''
    game_font = pygame.freetype.Font("./assets/font/Glass_TTY_VT220.ttf", 60)

    return game_font.render(
        text, color(text_color))


def main():
    '''
    Funcion que crea el componente inicial para empezar el juego.
    '''

    display = (800, 600)
    caption = "Maz-Rogue Game!"
    game_active = True
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption(caption)

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(color("white"))

        r_width, r_height = 750, 550
        r_x, r_y = (display[0] - r_width) // 2, (display[1] - r_height) // 2

        pygame.draw.rect(screen, color("black"), (r_x, r_y, r_width, r_height))
        text_surface, rect = text_generator("@", "red")
        screen.blit(text_surface, (150, 300))

        pygame.display.flip()


if __name__ == '__main__':
    main()
