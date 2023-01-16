import pygame
import sys
import random

#Get the picture
src_img = sys.argv[1]

#Load the image
img = pygame.image.load(src_img)

#Get the size of the image
(w, h) = img.get_size()
win = pygame.display.set_mode((w, h))

#Fill background with white
win.fill((255, 255, 255))

#Visit each pixel and draw a circle in that pixel
for y in range (h):
	for x in range (w):
		(r, g, b, _) = img.get_at((x, y))
		
		randomx = random.randint(x, x + 3)
		randomy = random.randint(y, y + 3)
		
		#Draw red dots
		for _ in range (1, r, 50):
			pygame.draw.circle(win, (255, 0, 0), (random.randint(x, x + 3), random.randint(y, y + 3)), 1)
		
		#Draw green dots
		for _ in range (1, g, 50):
			pygame.draw.circle(win, (0, 255, 0), (random.randint(x, x + 3), random.randint(y, y + 3)), 1)
		
		#Draw blue dots
		for _ in range (1, b, 50):
			pygame.draw.circle(win, (0, 0, 255), (random.randint(x, x + 3), random.randint(y, y + 3)), 1)
		
		#Draw in black dots
		for _ in range (1, _, 50):
			pygame.draw.circle(win, (0, 0, 0), (random.randint(x, x + 3), random.randint(y, y + 3)), 1)
		
	#Update the display
	pygame.display.update()
	
#Update the display
pygame.display.update()

#Save image
pygame.image.save(win, "redraw.png")

#Keep it up for 3 seconds
pygame.time.delay(3000)
