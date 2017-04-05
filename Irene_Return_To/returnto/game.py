#Group member:Fangfang(Daisy),Inhye,Halle.
#Group Name:Triad
#Game Name:Return To




from gamelib import *

game = Game(800,600,"Return To")

#objects

screen = Image("images\\screen.png",game)
screen.resizeTo(800,600)
title = Image("images\\title.png",game)
title.moveTo(400,150)
title.resizeBy(10)
key = Image("images\\keys.png",game)
key.moveTo(640,450)
key.resizeBy(-30)

bob = Animation("images\\bob\\walk1_",4,game)
bob.moveTo(700,275)

ghost= Image("images\\monster.png",game)
ghost.moveTo(300,275)
ghost2= Image("images\\monster.png",game)
ghost3= Image("images\\monster.png",game)
ghost4= Image("images\\monster.png",game)
ghost3.moveTo(400,275)
ghost4.moveTo(50,400)
ghost3.resizeBy(-30)
ghost4.resizeBy(-30)

lantern = Image("images\\lantern.png",game)
lantern.resizeBy(-40)
lantern.moveTo(680,280)

ghost.setSpeed(8,180)
ghost2.setSpeed(15,180)
ghost3.setSpeed(10,180)
ghost4.setSpeed(5,180)

candy= Image("images\\candy.png",game)
candy.moveTo(200,275)

bk1= Image("images\\greenbk.png",game)
game.setBackground(bk1)

start = Image("images\\start.png",game)
lost = Image("images\\lost.png",game)
win = Image("images\\win.png",game)
win2 = Image("images\\win2.png",game)
extras = Image("images\\extras.png",game)
extras.resizeTo(800,600)
ending = Image("images\\ending.png",game)
ending.resizeTo(800,600)


bkm = Sound("bgm.wav",1)
game.setMusic("bbgm.wav")
cute = Sound("CollidedWithCandy.wav",2)
ncute = Sound("dfasfsdf_converted.wav",2)
gameover = Sound("gameover.wav",1)
click = Sound("pickup.wav",3)


##### Initial page
game.playMusic()
screen.draw()
title.draw()
key.draw()
game.drawText("By Triad",350,250,Font(white,40,blue))
game.drawText("Press[SPACE] To Start",500,500,Font(yellow,30,blue))
game.update()
game.wait(K_SPACE)

####
bk1.draw()
key.draw()
game.drawText("Bob lost his memory, but somehow he knew that the “candy”",90,200,Font(black,30,yellow))
game.drawText("in the cave can help him restore his memory.",90,230,Font(black,30,yellow))
time.sleep(0.5)
game.wait(K_SPACE)

game.drawText("Press[SPACE] To Continue",500,500,Font(yellow,30,blue))
game.drawText("Player has to help bob to restore his memory!",100,340,Font(black,30,yellow))
game.drawText("TIPS: If Bob collides with the ghosts, he will be mentally damaged.",100,370,Font(yellow,25,black))
game.drawText("As Bob eats the candy, part of his memory will be restored",140,400,Font(yellow,25,black))
game.update()
time.sleep(1)
game.wait(K_SPACE)

bk1.draw()
start.draw()
game.drawText("Press[LEFT] To START",500,500,Font(yellow,30,blue))

game.update(1)
game.wait(K_LEFT)
game.stopMusic()


#variables
memory = 0
sanity = 100

while not game.over:
    game.processInput()
    game.scrollBackground("left",1)
    if keys.Pressed[K_LEFT] or keys.Pressed[K_RIGHT]:
        click.play()

    x=randint(100,600)
    xx=randint(0,800)
    mm = randint(2,5)
    
    #ghost.setSpeed(s,180)
    #ghost2.setSpeed(s,180)
    #ghost3.setSpeed(s,180)
    #ghost4.setSpeed(s,180)
    
    bob.draw()
    lantern.draw()
    bkm.play()
    
    game.drawText("starting point",lantern.x-40,lantern.y-40,Font(white,20))
    
    ghost.move()
    ghost2.move()
    ghost3.move()
    ghost4.move()
    candy.draw()
    if ghost.isOffScreen() or ghost2.isOffScreen() or ghost3.isOffScreen() or ghost4.isOffScreen() :
        click.play()
        ghost.setSpeed(20,180)
        ghost2.setSpeed(15,180)
        ghost.moveTo(300,-20)
        ghost2.moveTo(x,0)
        ghost3.moveTo(400,275)
        ghost4.moveTo(50,275)
        ghost3.setSpeed(15,180)
        ghost4.setSpeed(8,180)
        
    if keys.Pressed[K_LEFT]:
        bob.x-=10
    if keys.Pressed[K_RIGHT]:
        bob.x+=10

    if bob.collidedWith(ghost) or bob.collidedWith(ghost2) or bob.collidedWith(ghost3):
        ncute.play()
        memory-=mm
        sanity-=10
        ghost.moveTo(300,-20)
        bob.moveTo(680,275)

    if bob.isOffScreen():
        bob.moveTo(700,275)

    if candy.collidedWith(bob):
        memory+=10
        cute.play()
        candy.visible= False
        candy.moveTo(xx,275)
        candy.visible=True


    if memory <=0:
        memory = 0
    if memory>=100:
        memory-=(memory-100)
     ####    
    if memory==100 and sanity <= 50:
        extras.draw()
        win.draw()
        game.drawText("Bob remembered everything! ...except for his family.",140,200,Font(black,30,yellow))
        game.drawText("Happy Ending?",300,350,Font(black,50,yellow))
        game.drawText("Press [Space] to Exit",320,500)
        game.drawText("Thank you for playing",320,530)
        game.over=True
        candy.visible=False

    if memory==100 and sanity >= 50:
        ending.draw()
        win2.draw()
        game.drawText("Bob remembered his family were ......and returned to ",110,200,Font(black,30,yellow))
        game.drawText("his hometown.",90,230,Font(black,30,yellow))
        game.drawText("The End",300,350,Font(black,50,yellow))
        game.drawText("Press [Space] to Exit",320,500)
        game.drawText("Thank you for playing",320,530)
        game.over=True
        candy.visible=False
        
        
    if sanity <=0:
        gameover.play()
        lost.draw()
        game.drawText("Bob became a ghost just like his family.",110,200,Font(black,30,yellow))
        game.drawText("Try Again",320,350,Font(black,50,yellow))
        game.drawText("Press [Space] to Exit",320,400)
        game.over=True

    




    game.drawText("Memory: " + str(memory) + "%",5,5)
    game.drawText("Sanity: " + str(sanity)  + "%" ,5, 22)
    game.update(10)


game.wait(K_SPACE)
game.quit()



