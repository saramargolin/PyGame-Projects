#Alvin Dai, Mary Correa Ortega, Victor Cherres
#Black Wolves
#Journey To Paradise

from gamelib import *

game = Game(970,540,"Journey To Paradise")

bk = Image("image\\sky2.jpg",game)
bk.resizeTo(game.width, game.height)


game.setBackground(bk)

player= Image("image\\up.png",game)
player.resizeBy(-75)
player.moveTo(50,180) 
player.setSpeed(5,90)

plane= Image("image\\plane.png",game)
plane.resizeBy(-60)
plane.moveTo(970,270)
plane.setSpeed(5,90)

fuel=1000


title = Image("image\\paradise.jpg",game)
title.resizeTo(game.width, game.height)
bk.draw()
title.draw()
game.drawText("Journey To Paradise",323,180,Font(yellow,30,yellow))
game.drawText("By:Black Wolves",325,200,Font(yellow,30,yellow))
game.drawText("Instruction: Use ARROW keys to dodge obstacles and collect items.",323,330)
game.drawText("Press [SPACE] to play",600,400)
game.update(1)
game.wait(K_SPACE)

gameover =  Image("image\\gameover.png",game)
gameover.resizeBy(-80)





#Challenge: Tried to spread the clouds apart and appear as if it scrolled from right to left
clouds = []

for times in range(7):
    clouds.append(Image("image\\cloud2.png",game))

for c in clouds:
    c.resizeBy(-60)
    c.setSpeed(2,90)
    x = randint(50,1500)
    y = randint(100,400)
    c.moveTo(x,y)

balloon3=[]

for times in range(2):
    balloon3.append(Image("image\\balloon3.png",game))

for b in balloon3:
    b.resizeBy(-64)
    b.setSpeed(2,90)
    x = randint(50,1500)
    y = randint(100,400)
    b.moveTo(x,y)


gas=[]

for times in range(5):
    gas.append(Image("image\\gas.png",game))

for g in gas:
    g.resizeBy(-84)
    g.setSpeed(2,90)
    x = randint(50,1500)
    y = randint(100,400)
    g.moveTo(x,y)

pet=[]

for times in range(4):
    pet.append(Animation("image\\pet.png",22,game,1200/5,1570/5,4))

for p in pet:
    p.resizeBy(-55)
    p.setSpeed(2,90)
    x = randint(1000,1500)
    y = randint(100,400)
    p.moveTo(x,y)
    
    
    

while not game.over:
    game.processInput()
    bk.draw()
    player.draw()
    plane.draw()
    plane.move()
    
    
    fuel-=.5
    
    for c in clouds:
        c.move()
        if c.isOffScreen("left"):
            x = randint(1000,1500)
            y = randint(100,400)
            c.moveTo(x,y)


    for b in balloon3:
        b.move()
       
        if player.collidedWith(b):
            player.health+=10
            b.visible=False

        if b.isOffScreen("left"):
            x = randint(1000,1500)
            y = randint(100,400)
            b.moveTo(x,y)
            b.visible=True


    for g in gas:
        g.move()
       
        if player.collidedWith(g):
            fuel+=100
            g.visible=False

        if g.isOffScreen("left"):
            x = randint(1000,1500)

            y = randint(100,400)
            g.moveTo(x,y)
            g.visible=True

    for p in pet:
        p.move()
        p.x-=3

        if player.collidedWith(p):
            player.health-=.5

        if p.isOffScreen("left"):
            x = randint(1000,1500)
            y = randint(100,400)
            p.moveTo(x,y)
    


    if keys.Pressed[K_LEFT]:
        player.x-=5
    if keys.Pressed[K_RIGHT]:
        player.x+=5
    if keys.Pressed[K_UP]:
        player.y-=5
    if keys.Pressed[K_DOWN]:
        player.y+=5


    if plane.isOffScreen("left"):
        x= game.width + 100
        y= randint(100,500)
        plane.moveTo(x,y)
        plane.visible=True
    
    if player.collidedWith(plane):
        game.over=True
        

    if player.health<=0 or fuel<=0:
        game.over=True
        
        
    game.drawText("Health: " + str(player.health),5,5)
    game.drawText("Fuel: " + str(fuel),500,5)
    game.update(60)

gameover.draw()
game.drawText("Press [SPACE] to Exit",400,400)
game.update(1)
game.wait(K_SPACE)
game.quit() 




