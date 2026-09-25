import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("media/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
perdiste = False
ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60
puntuaje = 0
COLOR_FONDO = (36, 148, 240)
COLOR_JUGADOR = (20, 200, 40)
COLOR_METEORITO = (255, 100, 60)
color_texto = (20,20,250)
fuente = pygame.font.SysFont(None, 74)
fuente_small = pygame.font.SysFont(None, 34)

meteoritos = []
nivel = 1
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 60
INTERVALO_APARICION = 500
ultimo_spawn = pygame.time.get_ticks()
aumento = 70
ganaste = False
JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

# --- Meteoritos ---
# Cada meteorito lo representaremos como un pygame.Rect dentro de esta lista.
meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4

sprite_grigio = pygame.image.load("media/grigio.jpeg").convert_alpha()
sprite_bruno = pygame.image.load("media/bruno.jpeg").convert_alpha()

sprite_grigio = pygame.transform.scale(sprite_bruno, (50,50))
sprite_bruno = pygame.transform.scale(sprite_grigio, (50,50))
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
        puntuaje += 1
        for i in range(10):
            if puntuaje // 10 == i*aumento:
                VELOCIDAD_METEORITO += 0.1
                INTERVALO_APARICION -= 0.1
                nivel = i
            if nivel == 7:
                  ganaste = True
        
           
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
        for meteorito in meteoritos:
            meteorito.y += VELOCIDAD_METEORITO
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_spawn >= INTERVALO_APARICION:
            x = random.randint(0, ANCHO - METEORITO_TAM)
            meteoritos.append(pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM))
            ultimo_spawn = tiempo_actual
            
        for meteorito in meteoritos:
            pantalla.blit(sprite_grigio, (jugador_x, jugador_y))
            meteoritos = [m for m in meteoritos if m.y < ALTO]
        

    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    for meteorito in meteoritos:
           if jugador_rect.colliderect(meteorito):
                  perdiste = True
                  
    
    
    
    pantalla.fill(COLOR_FONDO)
    
    pantalla.blit(sprite_bruno, (jugador_x, jugador_y))

    for meteorito in meteoritos:
           pantalla.blit(sprite_grigio, (jugador_x, jugador_y))
    texto_puntuaje = fuente_small.render(f"Puntuaje: {puntuaje // 10}", True, "white")
    texto_nivel = fuente_small.render(f"nivel: {nivel}", True, "white")
    pantalla.blit(texto_nivel, (10,40))
    pantalla.blit(texto_puntuaje, (10,10))
    if perdiste:
           texto = fuente.render("perdiste", True, color_texto)
           textop = fuente_small.render(f"llegaste al nivel:  {nivel}", True, color_texto)
           rect_texto = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
           pantalla.blit(texto, rect_texto)
           rect_textop = textop.get_rect(center=(ANCHO // 2, ALTO // 2 + 40))
           pantalla.blit(textop, rect_textop)
           juego_terminado = True
    if ganaste:
        texto_w = fuente.render("ganaste!!", True, "white")
        rect_texto = texto_w.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto_w, rect_texto)
        juego_terminado = True
    
    
    
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
