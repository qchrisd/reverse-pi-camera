# Import dependencies
import pygame
import pygame.camera
import pygame.font
import sys
import board
import adafruit_hcsr04 as hcsr

# Initialize Pygame and create the screen (window)
pygame.init()
window = pygame.display.set_mode((640,480))

# Initialize the camera and start it for image capturing
pygame.camera.init()
cameras = pygame.camera.list_cameras()
print(cameras)
cam = pygame.camera.Camera(cameras[0], (640, 480))
cam.start()

# Create a font object to hold text
pygame.font.init()
d1 = pygame.font.Font(None, 50)

# Create the pygame surface (unsure what this does)
frame = pygame.Surface((640,480))

# initialize the distance sensor for proper GPIO pin release
with hcsr.HCSR04(trigger_pin=board.D16, echo_pin=board.D20) as sonar:
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
        
        # Gets the distance from the US sensor
        distance = sonar.distance
        
        # Writes distance to the frame
        text = d1.render("{0:.0f}".format(distance), False, (255,255,255))
        frame.blit(text, (50,50))
        
        # blits the surface onto the screen at the orign of the window
        window.blit(frame, (0,0))

        # Sends the blitted things to the frame buffor for display
        pygame.display.update()
