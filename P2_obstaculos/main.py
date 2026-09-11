"""
PARTE 2: Meteoritos
Repasamos: pygame.time.get_ticks() como temporizador, listas, random.
"""
import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60

COLOR_FONDO = (20, 20, 40)
COLOR_JUGADOR = (20, 200, 40)
COLOR_METEORITO = (255, 100, 60)
color_texto = (20,20,250)
fuente = pygame.font.SysFont(None, 64)

meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 60
INTERVALO_APARICION = 500
ultimo_spawn = pygame.time.get_ticks()


JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

# --- Meteoritos ---
# Cada meteorito lo representaremos como un pygame.Rect dentro de esta lista.
meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4

# TODO 1: Define cada cuántos milisegundos debe aparecer un meteorito nuevo.
# Sugerencia: 800 (0.8 segundos)
INTERVALO_APARICION = 800

# Guardamos el momento (en ms) del último meteorito que apareció.
ultimo_spawn = pygame.time.get_ticks()
juego_terminado = False
corriendo = True
while corriendo:
  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    teclas = pygame.key.get_pressed()
    if not juego_terminado:
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
    if not juego_terminado:
        for meteorito in meteoritos:
            meteorito.y += VELOCIDAD_METEORITO
    # TODO 2: Cada INTERVALO_APARICION milisegundos, crea un meteorito nuevo.
    # Pasos sugeridos:
    #   a) obtén el tiempo actual con pygame.time.get_ticks()
    #   b) si (tiempo_actual - ultimo_spawn) >= INTERVALO_APARICION:
    #        - elige una posición x aleatoria con random.randint(0, ANCHO - METEORITO_TAM)
    #        - crea un pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM)
    #        - agrégalo a la lista `meteoritos`
    #        - actualiza `ultimo_spawn` al tiempo actual
    tiempo_actual = pygame.time.get_ticks()
    if not juego_terminado:
        if tiempo_actual - ultimo_spawn >= INTERVALO_APARICION:
            x = random.randint(0, ANCHO - METEORITO_TAM)
            meteoritos.append(pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM))
            ultimo_spawn = tiempo_actual
    
    for meteorito in meteoritos:
        pygame.draw.rect(pantalla, COLOR_METEORITO, meteorito)
        meteoritos = [m for m in meteoritos if m.y < ALTO]


    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    for meteorito in meteoritos:
           if jugador_rect.colliderect(meteorito):
                  juego_terminado = True
                  print("perdiste..,.")
    # TODO 3: Mueve cada meteorito de la lista hacia abajo
    # (incrementa su coordenada y en VELOCIDAD_METEORITO).
    # Pista: cada elemento de `meteoritos` es un pygame.Rect;
    # los Rect tienen un atributo .y que puedes modificar directamente.

    # TODO 4: Elimina de la lista los meteoritos que ya salieron de la pantalla
    # (es decir, cuando meteorito.y > ALTO).
    # Pista: puedes construir una nueva lista con los que SÍ quieres conservar,
    # por ejemplo usando una list comprehension o un bucle con una lista auxiliar.

    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(
        pantalla, COLOR_JUGADOR, jugador_rect )
    for meteorito in meteoritos:
           pygame.draw.rect(pantalla, COLOR_METEORITO, meteorito)
    if juego_terminado:
           texto = fuente.render("perdiste", True, color_texto)
           rect_texto = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
           pantalla.blit(texto, rect_texto)


    
    
    
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
