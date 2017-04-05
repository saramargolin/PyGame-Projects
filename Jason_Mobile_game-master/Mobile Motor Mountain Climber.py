from gamelib import *

game = Game(1280,640,"Mobile Motor Mountain Climber")

bk = Image ("mobilebackground.png",game)
bk.resizeTo(game.width,game.height)

jumping = False
landed = False 
factor = 1 


game.setBackground(bk)

title = Image("gamelogo.png",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to play",550,400)
game.drawText("Press [SPACE] to jump",550,425)
game.drawText("Press the left/right arrow keys to move forward or stop",450,450)
game.drawText("Press the up arrow while midair to do a super jump",480,475)
game.drawText("Don't stay on the platform, you lose points! Keep on jumping!",400,500)
game.update(1)
game.wait(K_SPACE)

platform = Image("platform.png",game)
x = 700
y = randint(300,500)
platform.moveTo( x, 405 )
platform.setSpeed(8,90)
platform.resizeBy(-25)

platform2 = Image("platform.png",game)
x = 1200
y = randint(300,500)
platform2.moveTo( x, y )
platform2.setSpeed(8,90)
platform2.resizeBy(-25)

platform3 = Image("platform.png",game)
x = 1600
y = randint(300,500)
platform3.moveTo( x, y )
platform3.setSpeed(8,90)
platform3.resizeBy(-25)

platform4 = Image("platform.png",game)
x = 2000
y = randint(300,500)
platform4.moveTo( x, y )
platform4.setSpeed(8,90)
platform4.resizeBy(-25)

car = Image("greencar.png",game)
car.resizeBy(-75)


gascan = Image ("gascan.png",game)
x = 700
y = randint(300, 500)
gascan.moveTo( x, 350 )
gascan.setSpeed(8,90)
gascan.resizeBy(-25)

gamewin =  Image("mmgamewin.png",game)


gameover =  Image("mmgamelose.png",game)





while not game.over:
     game.processInput()
     game.scrollBackground("left",8)
     car.draw()
     car.move()
     gascan.draw()
     gascan.move()
     platform.draw()
     platform.move()
     platform2.draw()
     platform2.move()
     platform3.draw()
     platform3.move()
     platform4.draw()
     platform4.move()



     

     if platform.isOffScreen("left"):
          x = game.width + 200
          y = randint(300,400)
          platform.moveTo( x, 400 )
          platform.visible = True

     if platform2.isOffScreen("left"):
          x = game.width + 200
          y = randint(300,500)
          platform2.moveTo( x, y )
          platform2.visible = True

     if platform3.isOffScreen("left"):
          x = game.width + 200
          y = randint(300,500)
          platform3.moveTo( x, y )
          platform3.visible = True

     if platform4.isOffScreen("left"):
          x = game.width + 200
          y = randint(300,500)
          platform4.moveTo( x, y )
          platform4.visible = True


     if keys.Pressed[K_LEFT]:
        car.x -= 7
        
     if keys.Pressed[K_RIGHT]:
        car.x += 6

     if keys.Pressed[K_UP]:
        car.y -= 6
        
     

     
     if car.y < 900:
        landed = False
        if car.collidedWith(platform,"rectangle"):
            landed = True
            platform.x+=2
            game.score-=1
        if car.collidedWith(platform2,"rectangle"):
            landed = True
            game.score-=1
        if car.collidedWith(platform3,"rectangle"):
            landed = True
            platform3.y+=19
            game.score-=1
        if car.collidedWith(platform4,"rectangle"):
            landed = True
            game.score-=1
            
     else:
        landed = True
        
     if jumping:
        car.y -= 27 * factor
        factor *= .95
        landed = False
        if factor < .18:
            jumping = False
            factor = 1
            
     if keys.Pressed[K_SPACE] and landed and not jumping:
            jumping = True
            
     if not landed:
        car.y += 11                                                                 

     if gascan.isOffScreen("left"):
          x = game.width + 283
          y = randint(300,500)
          gascan.moveTo( x, 350 )
          gascan.visible = True

     if car.y > 900:
        game.over = True
        gameover.draw()
        
     game.drawText("Score: " + str(game.score),5,5)

     if car.collidedWith(gascan,"rectangle"):
          gascan.visible = False
          game.score+=40

     if game.score>=299:
        game.over=True
        gamewin.draw()

     if game.score<=0:
        game.over=True
        gameover.draw()
          
#Goal: The goal of my game is to make the car jump from one platform to another,
#collecting gas cans along the way.



     game.update(60)


