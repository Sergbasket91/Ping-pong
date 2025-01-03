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

ball = GameSprite('tenis_ball.png', 330, 230, 3, 50, 50)
finish = False
speed_x = 3
speed_y = 3

text = font.Font(None, 35)
lose_l = text.render('Игрок 1 проиграл!', True, (255, 0, 0))
lose_r = text.render('Игрок 2 проиграл!', True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y <= 0 or ball.rect.y >= 450:
        speed_y *= -1
    if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
        speed_x *= -1
    if ball.rect.x >= 650:
        finish = True
        main_win.blit(lose_r, (200, 200))
    if ball.rect.x <= 0:
        finish = True
        main_win.blit(lose_l, (200, 200))
    
    racket_l.reset()
    racket_l.update_l()

    racket_r.reset()
    racket_r.update_r()

    ball.reset()

    display.update()
    main_win.fill((51, 102, 204))
    clock.tick(60)