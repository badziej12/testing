import pygame, sys
from pygame.locals import *
from rocket import Rocket

class Game(object):
    def __init__(self) -> None:
        # Config
        self.tps_max = 100.0

        # Initialization
        pygame.init()
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.screen = pygame.display.set_mode((1280, 720))
        self.player = Rocket(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            # Ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            while self.tps_delta > 1/self.tps_max:
                self.tick()
                self.tps_delta -=1/self.tps_max


                keys = pygame.key.get_pressed()

            # Drawing
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
                        

     



    def tick(self):
        self.player.tick()

    def draw(self):
        # Drawing
        self.player.draw()
       
if __name__ == "__main__":
    Game()
            





        


  