import pygame

def run_game():
    desired_fps = 120
    pygame.display.set_caption("This is Peng")
    background_color = (0,0,0)
    ball_color = (255,255,255)

    # Hier wird die Fenster-Auflösung gesetzt
    screen = pygame.display.set_mode((1024, 1024))

    # Hier wird die Clock Variable definiert und damit der Tick verfügbar gemacht
    clock = pygame.time.Clock()
    game_is_running = True

    # das ist, wie häufig die key-presses pro Sekunde abgefragt werden
    pygame.key.set_repeat((int)(1000 / (desired_fps * 4)))

    # Startpositionen der beiden Player Rectangles
    player_1_y = 512
    player_2_y = 512

    while game_is_running:

        # hier wird geguckt, ob das Quit-Event aufgerufen wurde (oder so)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            # hier wird geguckt, ob Tasten gedrückt werden (z.B. die Escape Taste), indem er sich die Tastendruck-Zustände aller!! Tasten in einer Liste holt
            # und wir dann an den entsprechenden Stellen die relevanten Tasten abfragen
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_ESCAPE]:
                game_is_running = False
            if keys_pressed[pygame.K_UP]:
                player_1_y = player_1_y - 1
            if keys_pressed[pygame.K_DOWN]:
                player_1_y = player_1_y + 1
            if keys_pressed[pygame.K_w]:
                player_2_y = player_2_y - 1
            if keys_pressed[pygame.K_s]:
                player_2_y = player_2_y + 1

        # hier wird die Hintergrundfarbe reingeladen
        screen.fill(background_color)
        # hier wird der Ball gezeichnet
        pygame.draw.circle(screen, ball_color, (512, 512), 10)
        # hier werden die Player-Rectangle gezeichnet
        pygame.draw.rect(screen, ball_color, (50, player_1_y, 10, 200))
        pygame.draw.rect(screen, ball_color, (1024-60, player_2_y, 10, 200))
        # hier wird das Display refreshed
        pygame.display.flip()
        # hier wird die framerate eingestellt. Frage fürs nächste mal: mUss man das jeden Frame machen?
        clock.tick(desired_fps)



run_game()