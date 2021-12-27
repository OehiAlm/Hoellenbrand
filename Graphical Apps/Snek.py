import pygame
import random
import os
import time

def main():

    # Hier wird die Clock Variable definiert und damit der Tick verfügbar gemacht
    clock = pygame.time.Clock()
    game_is_running = True

    # Position des Fensters auf dem aktuellen Bildschirm
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (64, 64)

    # wichtig für die DeltaTime
    prev_time = time.time()
    dt = 0

    desired_fps = 60

    class ScreenSize:
        screensizeX = 1024
        screensizeY = 800


    pygame.display.set_caption("This is Snek")
    background_color = (0, 0, 0)
    snek_color = (255, 255, 255)

    # Hier wird die Fenster-Auflösung gesetzt
    screen = pygame.display.set_mode((ScreenSize.screensizeX, ScreenSize.screensizeY))

    # das ist, wie häufig die key-presses pro Sekunde abgefragt werden
    pygame.key.set_repeat((int)(1000 / (desired_fps * 4)))

    while game_is_running:
        # hier wird die framerate eingestellt. Muss tatsächlich jeden Tick aufgerufen werden
        clock.tick(desired_fps)
        now = time.time()
        #print("current time = {}".format(now))
        dt = now - prev_time
        #print("deltaTime = {}".format(dt))
        prev_time = now
        #print("\nprevious time was = {}".format(prev_time))
        current_time = pygame.time.get_ticks()
        #print(current_time)

        # hier wird geguckt, ob das Quit-Event aufgerufen wurde (oder so)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            # hier wird geguckt, ob Tasten gedrückt werden (z.B. die Escape Taste), indem er sich die Tastendruck-Zustände aller!! Tasten in einer Liste holt
            # und wir dann an den entsprechenden Stellen die relevanten Tasten abfragen
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_ESCAPE]:
                game_is_running = False
            # if keys_pressed[pygame.K_UP]:
            #     if p1_y >= 5:
            #         p1_y = p1_y - 1 * dt * desired_fps
            # if keys_pressed[pygame.K_DOWN]:
            #     if p1_y <= screensizeY - p1_pedal_height - 5:
            #         p1_y = p1_y + 1 * dt * desired_fps
            # if keys_pressed[pygame.K_w]:
            #     if p2_y >= 5:
            #         p2_y = p2_y - 1 * dt * desired_fps
            # if keys_pressed[pygame.K_s]:
            #     if p2_y <= screensizeY - p2_pedal_height - 5:
            #         p2_y = p2_y + 1 * dt * desired_fps


        # hier wird die Hintergrundfarbe reingeladen
        screen.fill(background_color)

        def draw_snek(screen, snek_color, ScreenSize):
            pygame.draw.rect(screen, snek_color, (ScreenSize.screensizeX / 2, ScreenSize.screensizeY / 2, 10, 10))

        draw_snek(screen, snek_color, ScreenSize)

        # hier wird das Display refreshed
        pygame.display.flip()




main()
