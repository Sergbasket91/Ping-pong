from pygame import *
font.init()

main_win = display.set_mode((700, 500))
main_win.fill((51, 102, 204))

clock = time.Clock()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)

