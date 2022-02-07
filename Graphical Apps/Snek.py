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

# Hier definieren wir unsere Haupt-Funktion, in der sich im Prinzip alles abspielen wird.
def main():

    # ---------------------------------------------------------------------------------------------------------------- #
    #                                           Instanzieren & Initialisieren                                          #
    # ---------------------------------------------------------------------------------------------------------------- #

    # Hier wird die Clock Variable instanziert und damit der Tick verfügbar gemacht
    clock = pygame.time.Clock()
    game_is_running = True

    # Position des Fensters auf dem aktuellen Bildschirm (muss! vor der Initialisierung des Screens gemacht werden)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (128, 128)

    # Hier wird die Klasse ScreenSizeDimensions instanziert und unsere Standard-Auflösung für das Game gesetzt.
    ScreenSize = ScreenSizeDimensions(1600, 900)
    #print("Initiating ScreenSize Dimensions \n" + str(ScreenSize))

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
    snek_color = (255, 255, 255)
    snek_thicc = 10
    snek_direction_x = 0
    snek_direction_y = 0
    snek_position_x = ScreenSize.current_resolution_X / 2
    snek_position_y = ScreenSize.current_resolution_Y / 2
    snek = [(snek_position_x,snek_position_y),(snek_position_x + snek_thicc,snek_position_y),(snek_position_x+snek_thicc*2,snek_position_y)]

    # das ist, wie häufig die key-presses pro Sekunde abgefragt werden
    # pygame.key.set_repeat((int)(1000 / (desired_fps * 4)))


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

            if keys_pressed[pygame.K_UP]:
                snek_direction_x = 0
                snek_direction_y = -snek_thicc
            if keys_pressed[pygame.K_DOWN]:
                snek_direction_x = 0
                snek_direction_y = snek_thicc
            if keys_pressed[pygame.K_LEFT]:
                snek_direction_x = -snek_thicc
                snek_direction_y = 0
            if keys_pressed[pygame.K_RIGHT]:
                snek_direction_x = snek_thicc
                snek_direction_y = 0

            # hier gucken wir, welche Tasten gerade aufgehört wurden zu drücken. Hat den Vorteil, dass man nur 1 Event
            # reinbekommt, selbst wenn man die Taste vorher 3 Sekunden lang gedrückt hat.
            if event.type == pygame.KEYUP:

                # Ich hab mir die Taste F für das Fullscreen togglen ausgesucht.
                if event.key == pygame.K_f:
                # Also rufen wir die selbstgeschriebene Toggle Funktion auf und geben ihr unseren Container
                # mit den ganzen Daten zur aktuellen Größe, maximalen Größe, etc. mit
                    ToggleFullscreen(ScreenSize)

        # sorgt dafür, dass nur 1x pro Sekunde!! die Position unserer Snek wirklich upgedatet wird
        tick_timer = tick_timer + dt
        if tick_timer >= 1:
            tick_timer = 0
            snek_position_x = snek_position_x + snek_direction_x
            snek_position_y = snek_position_y + snek_direction_y

            # Auf Basis der neuen Position wird ein neuer Kopf gebaut und der Schwanz gelöscht.
            # Das machen wir deshalb, weil alle "Mittelteile" eigentlich an ihrer Position bleiben.
            snek.insert(0,(snek_position_x,snek_position_y))
            snek.pop(snek.__len__() - 1)

        # ---------------------------------------------------------------------------------------------------------------- #
    #                                                     Draw                                                         #
    # ---------------------------------------------------------------------------------------------------------------- #

        # Aktualisierung der Auflösung (falls zwischenzeitlich geändert)
        screen = pygame.display.set_mode((ScreenSize.current_resolution_X, ScreenSize.current_resolution_Y))

        # hier wird die Hintergrundfarbe reingeladen
        screen.fill(background_color)

        # Wir zeichnen alle Körperteile in der Liste
        for pos in snek:
            pygame.draw.rect(screen, snek_color, (pos[0], pos[1], snek_thicc, snek_thicc))

        # hier wird das Display refreshed
        pygame.display.flip()


# -------------------------------------------------------------------------------------------------------------------- #
#                                                       Run                                                            #
# -------------------------------------------------------------------------------------------------------------------- #

# Hier wird unsere Hauptfunktion aufgerufen. Wenn wir das weglassen würden hätten wir in diesem Programm eigentlich
# nur andere Dateien importiert und Daten & Funktionen definiert, aber halt nix wirklich ausgeführt.
main()
