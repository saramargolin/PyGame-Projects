#Matthew Dullahan Jeremy Dawson
#Winterfell Games
#Scott Pilgrim Road Rage

from gamelib import*

game = Game(800,600,"Scott Pilgrim RR")


scott = Animation("images\\SR.png",8,game,863/8,141/1,4)




bk = Image("images\\BK.png",game)


game.setBackground(bk)
bk.resizeBy(-10)
scott.resizeBy(-20)




LOSE = Image("images\\LOSE.jpg",game)
WIN = Image("images\\WIN.jpg",game)


WIN.resizeBy(100)
LOSE.resizeTo(game.width,game.height)



money = []
cops = []

game.drawBackground()
game.drawText("Scott Pilgrim Road Rage",game.width/6 ,game.height/6,Font(green,73,red))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(red,40,green))
game.drawText("Press ARROW KEYS to move",game.width/2 - 400,game.height - 50,Font(red,35,green))
game.update(1)
game.wait(K_SPACE)



for times in range(45):
    cops.append(Image("images\\COPCAR.gif",game))

for c in cops:
    x = game.width + randint(50,15000)
    y = randint(100,600) 
    s = 6
    c.moveTo(x,y)
    c.setSpeed(s,90)
    c.resizeBy(-65)



for times in range(20):
    money.append(Image("images\\money.png",game))


for m in money:
    x = game.width + randint(0,15000)
    y = randint(100,600)
    r = 2
    m.setSpeed(r,90)
    m.resizeBy(-85)
    



while not game.over:
    game.processInput()
    
    game.scrollBackground("left",2)


   
    
    scott.move()

    
    if keys.Pressed[K_UP]:
        scott.moveY(-6)

    if keys.Pressed[K_DOWN]:
        scott.moveY(6)

    if keys.Pressed[K_LEFT]:
        scott.moveX(-6)

    if keys.Pressed[K_RIGHT]:
        scott.moveX(6)


    for c in cops:
        c.move()
        if c.isOffScreen("left"):
            x = game.width + randint(0,15000) 
            y = randint(0,900) 
            c.moveTo(x,y) #why do the cop cars continue to overlap each other?
        if c.collidedWith(scott):
            scott.visible = False
            LOSE.draw()
            game.over = True
            c.visible = False

    for m in money:
        m.move()
        if m.isOffScreen("left"):
            x = game.width + randint(0,15000) 
            y = randint(100,600) 
            m.moveTo(x,y)
        if m.collidedWith(scott):
            game.score +=1
            m.moveTo(game.width + 200,y)




    if game.score>180:
        game.over = True
        WIN.draw()




    game.displayScore()
        
            

    game.update(60)

    




    




game.drawText("Press [SPACE] to Exit  "+ str(game.score),game.width/7 ,game.height/2,Font(red,73,green))
game.update(1)
game.wait(K_SPACE)
game.quit()


            
        


    
  


