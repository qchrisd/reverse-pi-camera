# Import dependencies
import pygame
import pygame.camera

# Initialize Pygame and create the screen (window)
pygame.init()
screen = pygame.display.set_mode((600,440))

# Initialize the camera and start it for image capturing
pygame.camera.init()
cam = pygame.camera.Camera('/dev/video0', (640, 480), 'RGB')
cam.start()

# Create the pygame surface (unsure what this does)
surface = pygame.Surface((640,480))

while True:
    # Gets an image and puts it on the previously created surface
    cam.get_image(surface)
    
    # blits the surface onto the screen at the orign of the window
    screen.blit(surface, (0,0))

    # Sends the blitted things to the frame buffor for display
    pygame.display.update()
