
from gamelib import *
#The name of our game is Escape

game = Game(1100,900,"Escape")
p1i = Animation("Escape\\p1idle.png",8,game,282/3,366/3,10)
p1r = Animation("Escape\\p1run.png",8,game,208/2,412/4,8)
key = Image("Escape\\key.png",game)
key2 = Image("Escape\\key2.gif",game)
key3 = Image("Escape\\k.gif",game)
bk2 = Image("Escape\\room2.jpg",game)
bk3 = Image("Escape\\room3.png",game)
g1 = Animation("Escape\\spoopy.png",8,game,1000/2,1500/4,6)
end = Image("Escape\\capture.jpg",game)

#start screen
bk=Image("Escape\\startup.png",game)
bk.resizeTo(game.width,game.height)
bk.draw()
game.update(1)
game.wait(K_SPACE)
#game.drawBackground()
#First Background
bk1 = Image("Escape\\room1.gif",game)
bk1.resizeBy(90)
blk = Image("Escape\\ihop.jpg",game)
blk.resizeTo(game.width,game.height)
p1i.moveTo(200,300)
p1r.moveTo(p1i.x,p1i.y)
key.resizeBy(-70)
bk2.resizeTo(game.width, game.height)
game.setBackground(bk1)
g1.resizeBy(-70)
bk3.resizeTo(game.width, game.height)
game.setBackground(bk1)
key2.resizeBy(50)
while not game.over:

    game.processInput()
    blk.draw()
    game.drawBackground()
    key.draw()
    #g1.moveTowards(p1i,2)
    g1.moveTowards(p1r,2)
    p1i.draw()
            
    game.drawText("Collect keys to get the next room!", game.width/2 + 80, game.height - 50,Font(yellow,40,green))
    game.drawText("Avoid the ghost",game.width/2 - 80,game.height + 50,Font(yellow,40,green))
    #problem 1: changing the direction shes facing in when she is running.
    if keys.Pressed[K_RIGHT]:
        p1i.visible = False
        p1r.draw()
        p1r.x += 3
    elif keys.Pressed[K_DOWN]:
        p1i.visible = False
        p1r.draw()
        p1r.y += 3
    elif keys.Pressed[K_LEFT]:
        p1i.visible = False
        p1r.draw()
        p1r.x -= 3
    elif keys.Pressed[K_UP]:
        p1i.visible = False
        p1r.draw()
        p1r.y -= 3
    else:
        p1i.visible = True
        p1i.draw()
        p1i.moveTo(p1r.x,p1r.y)

    #problem 2: going to a new room after a key is collected.
    if p1i.collidedWith(key) or p1r.collidedWith(key):
        game.setBackground(bk2)
        game.drawBackground()
        key.visible = False
        #key2.moveTo(400,-420)
        key2.draw()
        g1.moveTowards(p1r,4)
        
    if p1i.collidedWith(key2) or p1r.collidedWith(key2):
        game.setBackground(bk3)
        game.drawBackground()
        key3.draw()
        key2.visible = False
        
    
    if p1i.collidedWith(g1) or p1r.collidedWith(g1):
        p1i.health-=1
    if p1i.health<0:
        game.over =True
        
    game.drawText("Health = " + str(p1i.health),500,0)
    game.displayScore()
    
    game.update(60)
    
end.resizeTo(game.width,game.height)
end.draw()
game.update(1)
game.wait(K_ESCAPE)

game.quit()

