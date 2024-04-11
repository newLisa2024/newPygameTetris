import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('тестовый проект')

image1 = pygame.image.load('picPython1.png',)
image1 = pygame.transform.scale(image1, (100, 100))
image_rect1 = image1.get_rect()

image2 = pygame.image.load('pycharm.png',)
image2 = pygame.transform.scale(image2, (100, 100))
image_rect2 = image1.get_rect()

# speed = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX
            image_rect1.y = mouseY

    if image_rect1.colliderect(image_rect2):
        print('Произошло столкновение')

   # keys = pygame.key.get_pressed()
   # if keys[pygame.K_LEFT]:
   #    image_rect.x -= speed
   # if keys[pygame.K_RIGHT]:
   #     image_rect.x += speed
   # if keys[pygame.K_UP]:
   #     image_rect.y -= speed
   # if keys[pygame.K_DOWN]:
   #     image_rect.y += speed
    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()