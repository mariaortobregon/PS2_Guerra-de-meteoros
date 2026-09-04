"""
PARTE 0: Setup básico
Repasamos: inicializar pygame, crear una ventana y armar el loop principal.
"""
import pygame
import sys

pygame.init()

# TODO 1: Define el ancho y alto de la ventana (sugerencia: 800 x 400)
ANCHO = 250  # <-- reemplaza None por un número
ALTO = 250   # <-- reemplaza None por un número

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")

reloj = pygame.time.Clock()

# TODO 2: Define los cuadros por segundo (FPS) a los que correrá el juego.
# Sugerencia: 60
FPS = 50

# TODO 3: Define un color de fondo en formato RGB: una tupla de 3 números (0-255)
# Ejemplo de morado oscuro: (30, 20, 50)
COLOR_FONDO = (60, 30, 90)

corriendo = True
while corriendo:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujado
    pantalla.fill(COLOR_FONDO)

    # Actualizar pantalla y controlar velocidad
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
