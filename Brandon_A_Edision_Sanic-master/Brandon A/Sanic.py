#Group:Monsters Co
#Members:Brandon A, Brandon F, Shameel J Pd 7
#Game:Sanic
from gamelib import*

game = Game(800,600,"Game")

bk = Image("sanicimages\\sonicofbg.png",game)
bk.resizeTo(game.width, game.height)

#rings = [] #empty list

title = Image("sanicimages\\title.png",game)
death = Image("sanicimages\\death.png",game)
win = Image("sanicimages\\win.png",game)

game.setBackground(bk)
#font=Font(color = 240,50)

title.resizeTo(game.width, game.height)
title.draw()
game.drawText("Press [SPACE] to play",325,500)
game.drawText("Monsters Co.",1,580)
game.drawText("CONTROLS: Press Space To Jump",10,10)
game.drawText("Fire -5 health -5 score", 630,10)
game.drawText("Spikes -10 health -10 score", 590,30)
#game.drawText("SANIC",400,300)
game.update(1)
game.wait(K_SPACE)

sanic = Animation("sanicimages\\sonic.png",16,game,808/8,260/2)
#x = game.width + 100
#y = randint(300,500)
#sanic.moveTo ( x, y )
#sanic.setSpeed(5,90)

sanic.moveTo(sanic.x,460)


spike = Image("sanicimages\\spike.png",game)
x = game.width + 500
y = randint(499, 500)
spike.moveTo ( x, y )
spike.setSpeed(5,90)
spike.resizeBy(-15)

spike.moveTo(sanic.x,460)

ring = Animation("sanicimages\\ring2.png",64,game, 512/8, 512/8)
x = game.width + 100
y = randint(400, 500)
ring.moveTo( x, y )
ring.setSpeed(5,90)
ring.resizeBy(-25)

fire = Animation("sanicimages\\fire2.png",16,game,800/4, 800/4)
x = game.width + 100
y = randint(499,500)
fire.moveTo ( x, y )
fire.setSpeed(5,90)
fire.resizeBy(-20)


#for times in range(10):
    #rings.append( Animation("sanicimages\\ring2.png",64,game, 512/8, 512/8) )

jumping = False #Used to check to see if you are jumping
landed = False #Used to check to see if you have landed on the ground
factor = 1 #Used for a slowing effect of the jumping

sanic.health=110
game.score=10

while not game.over:
    game.processInput()
    game.scrollBackground("left",5)
    
    bk.draw()
    sanic.draw()
    ring.move()
    spike.move()
    fire.move()
    

    
    #if keys.Pressed[K_UP]:
        #sanic.y-=4

    #if keys.Pressed[K_DOWN]:
        #sanic.y+=4



    if sanic.collidedWith(ring):
        game.score+=25
        ring.visible = False
        x = game.width + 100
        y = randint(300, 500)
        ring.moveTo(x, y)
        ring.visible = True
        ring.move()
       
    if sanic.collidedWith(spike):
        sanic.health-=10
        game.score-=10
        spike.visible = False
        x = game.width + 500
        y = randint(499, 500)
        spike.moveTo(x, y )
        spike.visible = True
        spike.draw()

    if sanic.collidedWith(fire):
        sanic.health-=5
        game.score-=5
        fire.visible = False
        x = game.width + 400
        y = randint(400, 500)
        fire.moveTo(x, y )
        fire.visible = True
        fire.move()

    if ring.isOffScreen("left"):
        x = game.width + 300
        y = randint(100, 400)
        ring.moveTo(x, y)
        #ring.moveTo( bk.x, bk.y +175)

    if spike.isOffScreen("left"):
        x = game.width + 500
        y = (100, 500)
        spike.moveTo(900,500)
        #spike.moveTo( bk.x, bk.y +175)


    if fire.isOffScreen("left"):
        x = game.width + 700
        y = (100,500)
        fire.moveTo(900,500)

    


    if sanic.health<=0:
        game.drawText("You lose!",300,0)
        game.over=True
        death.resizeTo(game.width, game.height)
        death.draw()



    if game.score>=1000:
        game.drawText("You win!",500,0)
        game.over = True
        win.resizeTo(game.width, game.height)
        win.draw()


    if sanic.y < 455:
        landed = False
        #if sanic.collidedWith(bar,"rectangle"):
            #landed = True
        #300 is the floor.  Decision can be replaced with a more complex condition based on game
    else:
        landed = True
        
    if jumping:
        sanic.y -= 27 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True
            
    if not landed:
        sanic.y += 9
        #If you haven't landed then you are in the air, so you should fall.

  


    






    game.drawText("Health =  " + str(sanic.health),500,0)
    game.displayScore()


    game.update(60)




    
#game.drawText("Game Over",game.width/4,game.height/1,Font(black,90,blue))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 60,Font(blue,40,black))
game.update()
game.wait(K_ESCAPE)
game.quit()
    
game.quit()
