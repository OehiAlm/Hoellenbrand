# -------------------------------------------------------------------------------------------------------------------- #
#                                                       Import                                                         #
# -------------------------------------------------------------------------------------------------------------------- #

import pygame
import random
import os
import time
from win32api import GetSystemMetrics

# -------------------------------------------------------------------------------------------------------------------- #
#                                    Definitionen von (globalen) Klassen & Funktionen                                  #
# -------------------------------------------------------------------------------------------------------------------- #

# Klassen kann man sich als Container für Daten und Funktionen vorstellen.
# Man benutzt Klassen dann, wenn man mehrere kleine Daten in einen großen Container packen will (machen wir hier)
# oder wenn man von diesen Daten mehrere Kopien mit unterschiedlichen Werten braucht (z.B. für den Snek-Schwanz später)
# Klassen sind Blueprints, die erst im Speicher 'leben' wenn man sie referenziert oder mit eigenem Namen instanziert
# Wir instanzieren diese Klasse später (Zeile 46,47) mit dem Namen ScreenSize damit wir Zugriff auf ihre Daten haben
class ScreenSizeDimensions:
    max_resolution_X = GetSystemMetrics(0)
    max_resolution_Y = GetSystemMetrics(1)
    is_fullscreen = False

    # Funktion, die automatisch!! aufgerufen wird, wenn man die Klasse hier instanziert.
    def __init__(self, x = 800, y = 600):
        # Standardmäßig ist die Basis-Auflösung auf 800x600 gesetzt. Kann man aber beim Instanzieren ändern.
        self.base_resolution_X = x
        self.base_resolution_Y = y
        # stellt die aktuelle Auflösung auch direkt auf die gewählte Basis-Auflösung ein
        self.current_resolution_X = x
        self.current_resolution_Y = y

    # Funktion, die aufgerufen wird, wenn man den Inhalt der gesamten Klasse mit print() anzeigen lassen will
    def __str__(self):
        return "base res is X: % s, Y: % s --- " \
               "current res is X: % s, Y: % s --- " \
               "max res is X: % s, Y: % s --- " \
               "is_fullscreen is set to: % s \n" % (self.base_resolution_X, self.base_resolution_Y,
                                                    self.current_resolution_X, self.current_resolution_Y,
                                                    self.max_resolution_X, self.max_resolution_Y,
                                                    self.is_fullscreen)

# Funktion für das Umschalten zwischen Fullscreen und Windowed (mit Border)
def ToggleFullscreen(ScreenSize):
    if ScreenSize.is_fullscreen == False:

        # setzt die aktuelle Auflösung auf Maximum (wird aber erst im nächsten Tick / Update umgesetzt)
        ScreenSize.current_resolution_X = ScreenSize.max_resolution_X
        ScreenSize.current_resolution_Y = ScreenSize.max_resolution_Y

        # ist ne eingebaute Funktion von pygame.display, die die Auflösung allerdings nicht ändert
        pygame.display.toggle_fullscreen()

        # hier tracken wir einfach selbst, ob gerade Fullscreen aktiv ist oder nicht
        ScreenSize.is_fullscreen = True

        #print("Enabled Fullscreen")
        #print(ScreenSize)
    else:
        # Damit wir die Position des Fensters wieder auf die Ausgangsposition bringen können,
        # müssen wir (- das ist richtig dumm -) das Software Display erstmal killen...
        pygame.display.quit()

        # ...dann die neue Position setzen ...
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (128, 128)

        # ...und dann das Software Display wieder neu aufsetzen...
        pygame.display.init()

        # ...dann die neue Auflösung setzen...
        ScreenSize.current_resolution_X = ScreenSize.base_resolution_X
        ScreenSize.current_resolution_Y = ScreenSize.base_resolution_Y

        # ...und uns wieder merken, dass wir jetzt nicht mehr im Fullscreen sind
        ScreenSize.is_fullscreen = False

        #print("Disabled Fullscreen")
        #print(ScreenSize)

def Update_snek_speed(snek_speed):
    result = (snek_speed * snek_speed) / (snek_speed * 0.8)
    if result > 50:
        result = 50
    return result

# Hier definieren wir unsere Haupt-Funktion, in der sich im Prinzip alles abspielen wird.
def main():

    # ---------------------------------------------------------------------------------------------------------------- #
    #                                           Instanzieren & Initialisieren                                          #
    # ---------------------------------------------------------------------------------------------------------------- #

    # Hier wird die Clock Variable instanziert und damit der Tick verfügbar gemacht
    clock = pygame.time.Clock()
    game_is_running = True
    game_over = False

    # Position des Fensters auf dem aktuellen Bildschirm (muss! vor der Initialisierung des Screens gemacht werden)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (128, 128)

    # Hier wird die Klasse ScreenSizeDimensions instanziert und unsere Standard-Auflösung für das Game gesetzt.
    ScreenSize = ScreenSizeDimensions(800, 600)
    border_distance = 10
    BorderRect = pygame.Rect(0 + border_distance,
                             0 + border_distance,
                             ScreenSize.current_resolution_X - border_distance*2,
                             ScreenSize.current_resolution_Y - border_distance*2)

    #print("Initiating ScreenSize Dimensions \n" + str(ScreenSize))

    # Game Score
    Score_Color = (16,16,16)
    Score = 0

    # Hier wird unser Font Gedöns initialisiert
    pygame.font.init()
    #print(pygame.font.get_fonts())
    Game_over_Font = pygame.font.SysFont("comicsansms",size=24, bold=True)
    Score_Font = pygame.font.SysFont("AmericanTypewriter", size=480, bold=True)
    Game_over_Surface = Game_over_Font.render("Game Over du Arsch - press R to restart",True,(0,255,0))
    Score_Surface = Score_Font.render(str(Score), True, Score_Color)

    # Hier wird das Software Display initiiert und die Größe direkt mit unserer Standard-Auflösung versetzt
    pygame.display.init()
    pygame.display.set_mode((ScreenSize.base_resolution_X, ScreenSize.base_resolution_Y))

    # wichtig für die DeltaTime
    prev_time = time.time()
    dt = 0

    tick_timer = 0
    desired_fps = 60

    pygame.display.set_caption("This is Snek")
    background_color = (0, 0, 0)

    # Snek stuff
    #initial_snek_length = 7
    initial_snek_speed = 10     # Wie viele Movements pro Sekunde die Schlange macht
    white = (255, 255, 255)
    snek_thicc = 20
    snek_direction_x = snek_thicc   #brauchen wir, damit sie anfangs nach rechts los läuft
    snek_direction_y = 0
    snek_head_position_x = ScreenSize.current_resolution_X / 2
    snek_head_position_y = ScreenSize.current_resolution_Y / 2
    snek_speed = initial_snek_speed

    # Food stuff
    food_thicc = snek_thicc

    # Snek construction
    #counter = 0
    #snek = [(float,float)]
    #for bodyparts in range (initial_snek_length):
    #    counter = counter + 1
    #    snek = snek.insert((snek_head_position_x - snek_thicc * counter, snek_head_position_y))
    snek = [(snek_head_position_x, snek_head_position_y), (snek_head_position_x - snek_thicc, snek_head_position_y), (snek_head_position_x - snek_thicc * 2, snek_head_position_y)]

    # Snek Food
    # TODO: Food kann manchmal außerhalb unserer Begrenzung spawnen. Das ist schlecht. Grad kein Bock das zu machen.
    def Spawn_food():
        food_position_x = random.randint(border_distance, ScreenSize.current_resolution_X - border_distance * 2).__round__(-1 * int(food_thicc/10))
        food_position_y = random.randint(border_distance, ScreenSize.current_resolution_Y - border_distance * 2).__round__(-1 * int(food_thicc/10))
        return food_position_x, food_position_y

    food_position_x, food_position_y = Spawn_food()

    # das ist, wie häufig die key-presses pro Sekunde abgefragt werden
    # pygame.key.set_repeat((int)(1000 / (desired_fps * 4)))
    last_key_pressed = 4    #da snek nach rechts startet muss input nach links disabled werden
    new_direction_selected = False
    red = (255, 0, 0)

    # ---------------------------------------------------------------------------------------------------------------- #
    #                                                   Update                                                         #
    # ---------------------------------------------------------------------------------------------------------------- #

    # Alles was in diesem while-Loop passiert (typischerweise Update & Draw) findet jeden Frame / Tick statt!
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

        # hier wird geguckt, ob das Quit-Event aufgerufen wurde (oder so)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            # hier wird geguckt, ob aktuell irgendwelche Tasten gedrückt sind / werden,
            # indem er sich (wohlbemerkt, jeden Tick!) die Tastendruck-Zustände aller!! Tasten in einer Liste holt...
            keys_pressed = pygame.key.get_pressed()

            # ...und wir die relevanten Tasten dann abfragen. Hier die Escape-Taste.
            if keys_pressed[pygame.K_ESCAPE]:
                game_is_running = False

            if new_direction_selected is False:
                if keys_pressed[pygame.K_UP] and last_key_pressed != 2:
                    last_key_pressed = 1
                    snek_direction_x = 0
                    snek_direction_y = -snek_thicc
                    new_direction_selected = True
                    break
                if keys_pressed[pygame.K_DOWN] and last_key_pressed != 1:
                    last_key_pressed = 2
                    snek_direction_x = 0
                    snek_direction_y = snek_thicc
                    new_direction_selected = True
                    break
                if keys_pressed[pygame.K_LEFT] and last_key_pressed != 4:
                    last_key_pressed = 3
                    snek_direction_x = -snek_thicc
                    snek_direction_y = 0
                    new_direction_selected = True
                    break
                if keys_pressed[pygame.K_RIGHT] and last_key_pressed != 3:
                    last_key_pressed = 4
                    snek_direction_x = snek_thicc
                    snek_direction_y = 0
                    new_direction_selected = True

            # hier gucken wir, welche Tasten gerade aufgehört wurden zu drücken. Hat den Vorteil, dass man nur 1 Event
            # reinbekommt, selbst wenn man die Taste vorher 3 Sekunden lang gedrückt hat.
            if event.type == pygame.KEYUP:

                # Ich hab mir die Taste F für das Fullscreen togglen ausgesucht.
                if event.key == pygame.K_f:
                # Also rufen wir die selbstgeschriebene Toggle Funktion auf und geben ihr unseren Container
                # mit den ganzen Daten zur aktuellen Größe, maximalen Größe, etc. mit
                    ToggleFullscreen(ScreenSize)

                if event.key == pygame.K_r:
                    # hier restarten wir
                    snek_head_position_x = ScreenSize.current_resolution_X / 2
                    snek_head_position_y = ScreenSize.current_resolution_Y / 2
                    snek = [(snek_head_position_x, snek_head_position_y), (snek_head_position_x - snek_thicc, snek_head_position_y),
                            (snek_head_position_x - snek_thicc * 2, snek_head_position_y)]
                    snek_direction_x = snek_thicc  # wir laufen wieder nach rechts los
                    last_key_pressed = 4  # wir blockieren wieder, dass man nicht nach links laufen kann
                    snek_direction_y = 0
                    snek_speed = initial_snek_speed
                    game_over = False
                    Score = 0
                    Score_Surface = Score_Font.render(str(Score), True, Score_Color)


        if game_over == False:
            tick_timer = tick_timer + dt
            # sorgt dafür, dass erst nach einer bestimmten Anzahl von Ticks die Position unserer Snek upgedatet wird
            if tick_timer >= 1 / snek_speed:   # unsere Snek-Geschwindigkeit definiert, wie häufig wir Kollision und ähnliches updaten
                new_direction_selected = False  # nur ein input alle paar Ticks wird akzeptiert, weitere werden ignoriert
                tick_timer = 0

                # hier wird die neue Position (für den Kopf) ausgerechnet
                snek_head_position_x = snek_head_position_x + snek_direction_x
                snek_head_position_y = snek_head_position_y + snek_direction_y

                # Auf Basis der neuen Position wird ein neuer Kopf gebaut und der Schwanz gelöscht.
                # Das machen wir deshalb, weil alle "Mittelteile" eigentlich an ihrer Position bleiben.
                snek.insert(0, (snek_head_position_x, snek_head_position_y))
                snek.pop(snek.__len__() - 1)


                # ----------------- Collision Stuff ----------------- #

                # wenn snek auf essen trifft, dann passiert das
                if snek_head_position_x == food_position_x and snek_head_position_y == food_position_y:
                    # Score wird um eins erhöht & das dazugehörige Draw-Element geupdatet
                    Score = Score + 1
                    Score_Surface = Score_Font.render(str(Score), True, Score_Color)
                    # snek wird schneller
                    snek_speed = Update_snek_speed(snek_speed)
                    print("snek speed currently at: "+str(snek_speed))
                    # snek wird länger
                    snek.insert(snek.__len__(), (snek_head_position_x, snek_head_position_y))
                    # food wird neu platziert
                    food_position_x, food_position_y = Spawn_food()

                # guckt, ob die snek innerhalb unserer "Arena" ist, bzw. im nächsten Tick sein wird.
                # Wenn sie an die Kante kommt, kollidiert sie nicht mehr mit unserem BorderRect und dann ist game over
                if BorderRect.collidepoint(snek_head_position_x + snek_direction_x, snek_head_position_y + snek_direction_y):

                    # guckt, ob irgendein bodypart mit dem Kopf kollidiert
                    snek_head = snek[0]
                    snek_tail = snek[snek.__len__()-1]
                    for bodypart in snek:
                        if bodypart is not snek_head and bodypart is not snek_tail:
                            if snek[0] == bodypart:
                                game_over = True
                                break
                else:
                    game_over = True

                #TODO: fixen, dass der Fullscreen Modus alles richtig mit-skaliert
                #TODO: Skalierung vom Score. Der sieht noch nicht so richtig geil aus

    # ---------------------------------------------------------------------------------------------------------------- #
    #                                                     Draw                                                         #
    # ---------------------------------------------------------------------------------------------------------------- #

        # Aktualisierung der Auflösung (falls zwischenzeitlich geändert)
        screen = pygame.display.set_mode((ScreenSize.current_resolution_X, ScreenSize.current_resolution_Y))

        # hier wird die Hintergrundfarbe reingeladen
        screen.fill(background_color)

        # hier wird der Score in den Hintergrund gezeichnet
        screen.blit(Score_Surface, (40, 40))

        # Wir zeichnen alle Körperteile in der Liste
        for pos in snek:
            pygame.draw.rect(screen, white, (pos[0], pos[1], snek_thicc, snek_thicc))

        # Food Draw
        pygame.draw.rect(screen, white, (food_position_x, food_position_y, food_thicc, food_thicc), width=1)

        # Border Draw
        #test = pygame.draw.polygon(screen, red, BorderVertices, 4)
        pygame.draw.rect(screen, red, BorderRect, width=4)
        #print(type(test))

        # Game Over Screen
        if game_over == True:
            screen.blit(Game_over_Surface, (100, 100))
            Score_Surface = Score_Font.render(str(Score), True, (200, 155, 12))

        # hier wird das Display refreshed
        pygame.display.flip()


# -------------------------------------------------------------------------------------------------------------------- #
#                                                       Run                                                            #
# -------------------------------------------------------------------------------------------------------------------- #

# Hier wird unsere Hauptfunktion aufgerufen. Wenn wir das weglassen würden hätten wir in diesem Programm eigentlich
# nur andere Dateien importiert und Daten & Funktionen definiert, aber halt nix wirklich ausgeführt.
main()
