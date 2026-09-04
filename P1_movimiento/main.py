"""
PARTE 1: Movimiento del jugador
Repasamos: manejo de teclado con pygame.key.get_pressed() y límites de pantalla.
"""
import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60

COLOR_FONDO = (70, 40, 90)
COLOR_JUGADOR = (0, 0, 255)

# El jugador es un rectángulo que se mueve horizontalmente cerca del fondo
JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 10  # píxeles que se mueve por cuadro

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # TODO 1: Obtén el estado de todas las teclas presionadas.
    # Pista: pygame.key.get_pressed() devuelve una lista de booleanos.
    teclas = pygame.key.get_pressed()

    # TODO 2: Si se presiona la flecha izquierda o "A", disminuye jugador_x
    # (recuerda que en pygame, x=0 es el borde izquierdo)
    # Pista: teclas[pygame.K_LEFT] o teclas[pygame.K_a]
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_x -= VELOCIDAD_JUGADOR
    # TODO 3: Si se presiona la flecha derecha o "D", aumenta jugador_x
    # Pista: teclas[pygame.K_RIGHT] o teclas[pygame.K_d]
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jugador_x += VELOCIDAD_JUGADOR
    # TODO 4: Evita que el jugador se salga de la pantalla por los lados.
    # Pista: usa dos condicionales que comparen jugador_x con 0
    # y con (ANCHO - JUGADOR_ANCHO)
    if jugador_x < 0:
         jugador_x = 800 - JUGADOR_ANCHO
    if jugador_x > 800 - JUGADOR_ANCHO:
         jugador_x = JUGADOR_ANCHO
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(
        pantalla, COLOR_JUGADOR, (jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)
    )
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
