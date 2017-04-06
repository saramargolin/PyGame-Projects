#Group:J.M.
#Group member:Mengting Chen,Jenny Zhang
##Game Name:Frog diving

from gamelib import *

game = Game(800,600,"Game")

bk = Image("images\\bk.png",game)
bk.resizeTo(game.width, game.height)
bk.draw()

game.setBackground(bk)

pool = Animation("images\\pool.gif",1,game,360,270,1)
pool.resizeTo(800,400)
pool.moveTo(400,500)
pool.setSpeed(15,90)

frog = Animation("images\\fg.png",2,game,31,28,15)
frog.resizeTo(100,100)
frog.moveTo( 400,200 )
frog.setSpeed(6,60)

circle = Image("images\\circle.png",game)
circle.moveTo( 800,375)
circle.setSpeed(10,90)  
circle.resizeTo(150,150)

target = Image("images\\target.png",game)
target.moveTo(100,525)
target.setSpeed(20,90)
target.resizeTo(135,135)

lose =  Image("images\\you_lose.png",game)
lose.resizeTo(game.width, game.height)

win = Image("images\\you_win.png",game)
win.resizeTo(game.width, game.height)

title = Image("images\\logo.png",game)
title.resizeTo(500,300)
title.moveTo(425,300)
bk.draw()
title.draw()
game.drawText("By:J.M.",100,390,Font(black,35,white))
game.drawText("Press [SPACE] start game and control the frog going up,Press [UP] go up",20,450)
game.drawText("Press [LEFT]going left, and Press [RIGHT] going right",20,500)
game.update(1)
game.wait(K_SPACE)

while not game.over:
    game.processInput()
    bk.move()
    pool.draw()
    circle.move()
    target.move()
    frog.draw()


    if keys.Pressed[K_SPACE]:
        frog.y += 5  

    if keys.Pressed[K_LEFT]:
        frog.x -= 10

    if keys.Pressed[K_RIGHT]:
        frog.x += 10

    if keys.Pressed[K_UP]:
        frog.y -= 10

    if frog.collidedWith(target):
        game.score +=5
        frog.y -=100
        frog.visible = True

    if circle.isOffScreen("left"):
        circle.moveTo(800,375)

    if target.isOffScreen("left"):
        target.moveTo(800,525)

    if frog.collidedWith(circle):
        game.over=True
        lose.draw()

    if frog.collidedWith(target):
        game.score +=1
        frog.visible = True

    if game.score>=50:
        game.over=True
        win.draw()


    game.displayScore()
    game.update(30)

game.drawText("Press [SPACE] to Exit"+ str(game.score),320,400)
game.update(1)
game.wait(K_SPACE)
game.quit()




