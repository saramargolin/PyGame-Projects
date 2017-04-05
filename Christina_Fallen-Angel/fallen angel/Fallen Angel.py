
'''
-Afterlife Arts

-Fallen Angel

-The objects we are using in our game are: The keyboard, image, Sound and
Animation.

-To play the game you should press space bar. TO shot the press s. When the angel
collects souls its health and score increases. If the angel hits the demon or
devil its health decreases. If the angel shoots the demon or devil they will
disapear and its health will increase. After 50 souls are collected there will
be a diamond that will lead to the way to heaven and the player wins.
Be aware there are suprises. 
  
-When we were writing the codes we had problems such as getting the
angel(which is what the player controls) to move or follow the commands we wrote.
the image didnt appear where it was suppose to. It was hard to make the diamond
appear when it was suppose to. It was hard to make the demons  

''' 

from gamelib import*

game = Game(800,600,"Fallen Angel")

bk = Animation("image\\bk3.png",20,game,3200/4,3000/5,10)
game.setBackground(bk)

game.drawBackground()
title = Image("image\\logo.png",game)
bk.draw()
title.draw()
title.resizeTo(200,500)
 
game.drawText("Press [SPACE] to play",340,450)
game.drawText("Press 's' to shoot",355,495)
game.drawText("Use Arrows to move the Angel",310,473)

game.update(1)  
game.wait(K_SPACE)

instruction = Image("image\\Capture.png",game)

instruction.resizeTo(800,600)
instruction.draw()
game.update(1)  

instruction2 = Image("image\\instruction2.png",game)
instruction2.resizeTo(800,600)
instruction2.draw()
game.update(1)


angel = Animation( "image\\angels.png",4,game, 320/4,256/1,2)

ball = Animation( "image\\ball.png",30,game, 2000/5,2400/6,20)
ball.moveTo(angel.x,angel.y)
ball.resizeTo(40,40)



demon = Animation("image\\demon4.png",8,game,240/3,249/3,10)
demon.setSpeed(6,90)

soul = []
for num in range(300):
    soul.append(Image("image\\spirit.png",game))

for s in soul:
    s.resizeBy(-75)
    x = game.width + randint(100 ,20500)
    y = randint (0,600)
    sp  = randint(6,8)
    s.moveTo(x,y)
    s.setSpeed(sp,90)

demon = []
for num in range(200):
    demon.append(Animation("image\\demon4.png",8,game,240/3,249/3,10))
for d in demon:
        x = game.width + randint(0 ,20500)
        y = randint (0,600)
        s = randint(4,10)
        d.moveTo(x,y)
        d.setSpeed(s,90)

devil = []
for num in range(10):
    devil.append(Animation("image\\11.png",8,game,288/2,356/4,9)) 
for d in devil:
    x =game.width + randint(0 ,1000)
    y = randint (50,550)
    s = randint(4,10)
    d.moveTo(x,y)
    d.setSpeed(s,90)
        
devil2 = []
for num in range(20):
    devil2.append(Animation("image\\11.png",8,game,288/2,356/4,9)) 
for d in devil2:
    x = game.width + randint(0 ,1000)
    y = randint (50,550)
    s = randint(4,10)
    d.moveTo(x,y)
    d.setSpeed(s,90)
        
devil3 = []
for num in range(30):
    devil3.append(Animation("image\\11.png",8,game,288/2,356/4,8)) 
for d in devil3:
    x = game.width + randint(0 ,2000)
    y = randint (50,550)
    s = randint(4,10)
    d.moveTo(x,y)
    d.setSpeed(s,90)

bks = Sound("image\\hell.wav",1)
glass = Sound("image\\glassping.wav",2)
pain = Sound("image\\pain.wav",3)
throw = Sound("image\\throw.wav",4)
ch = Sound("image\\ZombieComeHere.wav",5)
vb = Sound("image\\VampireBite.wav",6)
Zip = Sound("image\\ZIP.wav",7)
soj = Sound("image\\SOJ.wav",1)

        
a = Image("image\\diamond1.png",game)
a.moveTo(800,900)
a.resizeBy(-70)

fi = Image("image\\fi.jpg",game)
fi.resizeTo(800,600)

heaven = Image("image\\heaven.jpg",game)




while not game.over:
    game.processInput()
    game.scrollBackground("left",2)

    bks.play()
    bk.move()
    angel.move()

    
    

        
    for s in soul:
       s.move()
       if angel.collidedWith(s):
           s.visible = False
           game.score+=1
           angel.health+=20
           glass.play()

    for d in demon:
        d.move()
        if angel.collidedWith(d):
            angel.health-=50
            pain.play()
        if ball.collidedWith(d):
            vb.play()
            d.visible = False
            angel.health+=50

    if game.score>=15:
        ch.play()
        for d in devil:
            d.move()
            if ball.collidedWith(d):
                d.health-=30
                angel.health+=200
                Zip.play()
                ball.moveTo(angel.x,angel.y)
            if angel.collidedWith(d):
                pain.play()
                angel.health-=200
            if d.health<=0:
                d.visible=False

    if game.score>=30:
        for d in devil2:
            ch.play()
            d.move()
            if ball.collidedWith(d):
                d.health-=25
                angel.health+=200
                Zip.play()
                ball.moveTo(angel.x,angel.y)
            if angel.collidedWith(d):
                pain.play()
                angel.health-=200
            if d.health<=0:
                d.visible=False
    
    if game.score>=5:
        a.moveTo(600,100)
        a.draw()
        a.makeVisible()
        for d in devil3:
            bks.play()
            d.move()
            if ball.collidedWith(d):
                d.health-=15
                angel.health+=200
                Zip.play()
                ball.moveTo(angel.x,angel.y)
            if angel.collidedWith(d):
                pain.play()
                angel.health-=200
            if d.health<=0:
                d.visible=False
                
                


        
    game.drawText("Health: " + str(angel.health),5,22)

    game.drawText("Soul: " + str(game.score),5,37)
                
    if keys.Pressed[K_s]:
        ball.visible = True
        ball.moveTo(angel.x,angel.y)
        ball.setSpeed(10 , 270)
        throw.play()        
    ball.move()
    
        
    if angel.collidedWith(a):
        game.over = True
        soj.play() 
        for s in soul:
            s.visible = False
        for d in devil3:
            d.visible = False
        game.setBackground(heaven)
        heaven.resizeTo(800,600)
        heaven.moveTo(400,300)
        game.drawText("WINNER!!!!",245,380,Font(blue,95,white))
        angel.moveTo(400,300)
        

    if keys.Pressed[K_LEFT]:
        angel.x-=5
    if keys.Pressed[K_RIGHT]:
        angel.x+=5
    if keys.Pressed[K_UP]:
        angel.y-=5
    if keys.Pressed[K_DOWN]:
        angel.y+=5

    if angel.health<=0:
        game.over = True
        game.setBackground(fi)
        fi.resizeTo(800,600)
        fi.draw()
        game.drawText("LOSERRR",270,380,Font(black,90,yellow))

    game.update(20)
    
game.drawText("Game Over",245,200,Font(red,90,blue))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(red,40,blue))
game.update()
game.wait(K_ESCAPE)
game.quit()


game.quit()


