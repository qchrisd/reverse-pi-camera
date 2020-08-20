# Import dependencies
import pygame
import pygame.camera
import sys

# Initialize Pygame and create the screen (window)
pygame.init()
window = pygame.display.set_mode((640,480))

# Initialize the camera and start it for image capturing
pygame.camera.init()
cameras = pygame.camera.list_cameras()
print(cameras)
cam = pygame.camera.Camera(cameras[0], (640, 480))
cam.start()

# Create the pygame surface (unsure what this does)
frame = pygame.Surface((640,480))

while True:
    # Handles events
    for event in pygame.event.get():
        # If the program was ended then exit the application
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            
    # Gets an image and puts it on the previously created surface
    cam.get_image(frame)
    
    # blits the surface onto the screen at the orign of the window
    window.blit(frame, (0,0))

    # Sends the blitted things to the frame buffor for display
    pygame.display.update()
