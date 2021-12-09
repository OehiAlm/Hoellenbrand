import pygame
import random
import os
import time

def run_game():

    #TODO for next time: Winkel für ankommende / abprallende Bälle

    # Hier wird die Clock Variable definiert und damit der Tick verfügbar gemacht
    clock = pygame.time.Clock()
    game_is_running = True

    # Position des Fensters auf dem aktuellen Bildschirm
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (2560-1050, 1440-1400)

    # wichtig für die DeltaTime
    prev_time = time.time()
    dt = 0

    desired_fps = 120

    screensizeX = 512
    screensizeY = 1024
    p1_score = 0
    p2_score = 0
    p1_pedal_height = 200
    p2_pedal_height = 200
    p_pedal_thiccness = 15
    BallDirectionX = random.choice([-1,1])
    BallDirectionY = random.choice([-3,-2,-1,1,2,3])
    GameCounter = 0

    pygame.font.init()
    pygame.display.set_caption("This is Peng")
    background_color = (0,0,0)
    ball_color = (255,255,255)

    # Hier wird die Fenster-Auflösung gesetzt
    screen = pygame.display.set_mode((screensizeX, screensizeY))

    # das ist, wie häufig die key-presses pro Sekunde abgefragt werden
    pygame.key.set_repeat((int)(1000 / (desired_fps * 4)))

    # Startpositionen der beiden Player Rectangles
    p1_x = screensizeX / 20
    p1_y = (screensizeY / 2) - (p1_pedal_height / 2)
    p2_x = screensizeX - screensizeX / 20 - p_pedal_thiccness
    p2_y = (screensizeY / 2) - (p2_pedal_height / 2)

    # Divider values
    divider_length = 25
    divider_gap = 25
    divider_thicc = 6
    divider_Xpos = screensizeX / 2 - divider_thicc / 2
    divider_Ypos = 0

    # Alles über den Ball
    ball_cooldown = 0
    temp_ballDirectionX = 0
    MaxBallSpeed = 5.5
    OGBallSpeed = 2
    BallSpeed = OGBallSpeed
    ballX = screensizeX / 2
    ballY = screensizeY / 2
    ballRadius = 10
    pygame.draw.circle(screen, ball_color, (ballX, ballY), 10)

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
            if keys_pressed[pygame.K_UP]:
                if p1_y >= 5:
                    p1_y = p1_y - 1 * dt * desired_fps
            if keys_pressed[pygame.K_DOWN]:
                if p1_y <= screensizeY - p1_pedal_height - 5:
                    p1_y = p1_y + 1 * dt * desired_fps
            if keys_pressed[pygame.K_w]:
                if p2_y >= 5:
                    p2_y = p2_y - 1 * dt * desired_fps
            if keys_pressed[pygame.K_s]:
                if p2_y <= screensizeY - p2_pedal_height - 5:
                    p2_y = p2_y + 1 * dt * desired_fps

        Oberkante_p1 = p1_y
        Oberkante_p2 = p2_y
        Unterkante_p1 = p1_y + p1_pedal_height
        Unterkante_p2 = p2_y + p2_pedal_height

        #Ball movement
        if (ballX >= p2_x - (ballRadius/2)) or (ballX <= p1_x + p_pedal_thiccness + (ballRadius/2)):
            if (ballY > Oberkante_p1 and ballY < Unterkante_p1 and BallDirectionX < 0)\
            or (ballY > Oberkante_p2 and ballY < Unterkante_p2 and BallDirectionX > 0):
                BallDirectionX = BallDirectionX * -1
                if BallSpeed < MaxBallSpeed: #mehr als 5.5 zerfickt die "Physik", weil der Ball dann zu schnell hinter die (dünnen) Balken kommt
                    BallSpeed = BallSpeed + 0.25

        if (ballY >= screensizeY - ballRadius/2) or (ballY <= ballRadius/2):
            BallDirectionY = BallDirectionY * -1

        ballX = ballX + BallDirectionX * BallSpeed * dt * desired_fps
        ballY = ballY + BallDirectionY * dt * desired_fps

        #Trigger Game over
        if ballX <= p1_x + p_pedal_thiccness or ballX >= p2_x:
            ball_cooldown = pygame.time.get_ticks() + 1000
            GameCounter = GameCounter + 1
            BallSpeed = OGBallSpeed
            pygame.display.set_caption("YOU SUCK: Game Counter = {}".format(GameCounter))
            ballX = screensizeX / 2
            ballY = screensizeY / 2

            # Checken, wer den Score kriegt und dementsprechend, was die neue Startrichtung ist
            if BallDirectionX > 0:
                p1_score = p1_score + 1
                temp_ballDirectionX = -1
            else:
                p2_score = p2_score + 1
                temp_ballDirectionX = 1

        if current_time < ball_cooldown:
            BallDirectionX = 0
            BallDirectionY = 0
        elif BallDirectionX == 0 or BallDirectionY == 0:
            BallDirectionX = temp_ballDirectionX
            BallDirectionY = random.choice([-3, -2, -1, 1, 2, 3])

        # hier wird die Hintergrundfarbe reingeladen
        screen.fill(background_color)
        # hier wird der divider gerendert
        divider_Ypos = 0
        while divider_Ypos <= screensizeY:
            pygame.draw.rect(screen, ball_color, (divider_Xpos, divider_Ypos, divider_thicc, divider_length))
            divider_Ypos = divider_Ypos + divider_length + divider_gap
        # hier wird der Score gezeichnet
        font = pygame.font.SysFont('consolas',100)
        Score_p1 = font.render("{}".format(p1_score), True, ball_color)
        Score_p2 = font.render("{}".format(p2_score), True, ball_color)
        screen.blit(Score_p1, (screensizeX / 3 - 50, 50))
        screen.blit(Score_p2, (screensizeX * 2 / 3, 50))
        # hier wird Debug Gedöns gezeichnet
        Debug_font = pygame.font.SysFont('consolas', 10)
        Debug_Screen = Debug_font.render("current Ball Speed: {}".format(BallSpeed), True, ball_color)
        screen.blit(Debug_Screen, (screensizeX - 150, screensizeY - 40))
        # hier wird der Ball gezeichnet
        pygame.draw.circle(screen, ball_color, (ballX, ballY), ballRadius)
        # hier werden die Player-Rectangle gezeichnet
        pygame.draw.rect(screen, ball_color, (p1_x, p1_y, p_pedal_thiccness, p1_pedal_height))
        pygame.draw.rect(screen, ball_color, (p2_x, p2_y, p_pedal_thiccness, p2_pedal_height))
        # hier wird das Display refreshed
        pygame.display.flip()

run_game()