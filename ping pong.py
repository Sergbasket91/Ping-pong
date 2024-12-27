from pygame import *
font.init()

main_win = display.set_mode((700, 500))
display.set_caption('ping-pong')
main_win.fill((51, 102, 204))

clock = time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (size1, size2))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.speed = p_speed
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y <= 345:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y <= 345:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed

racket_l = Racket('racket.png', 0, 230, 5, 30, 150)
racket_r = Racket('racket.png', 670, 230, 5, 30, 150)


# class Ball(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y >= 500:
#             self.rect.y = 0
#             lost += 1
#             self.rect.x = randint(50, 650)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    racket_l.reset()
    racket_l.update_l()

    racket_r.reset()
    racket_r.update_r()


    display.update()
    main_win.fill((51, 102, 204))
    clock.tick(60)