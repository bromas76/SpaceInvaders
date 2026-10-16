import sys

import pygame

from settings import Settings

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initilize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self


class SpaceInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Space Invaders")

        # Set the background color.
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw te screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SpaceInvaders()
    ai.run_game()
