import pygame
import random
x = 0
y = 0
def main():
    try:
        pygame.init()
        x = 0
        y = 0
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        clock = pygame.time.Clock()
        running = True


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (u, v) = event.pos
                    h_square = u // 32
                    v_square = v // 32
                    position = (h_square, v_square)
                    if position == (x,y):
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x*32, y*32)))
            # Horizontal Lines
            for i in range(1, 17):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            # Vertical Lines
            for j in range(1, 21):
                pygame.draw.line(screen, "black", (j * 32, 0), (j * 32, 512))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()