



from gamelib import *
from SocialMedia import *
game = Game(800,600,"Game")
bkkk = Image("SocialMedia\\bkkk.jpg",game)
game.setBackground(bkkk)

minuspoint = Image("SocialMedia\\minuspoint.png",game)
losepoint = Image("SocialMedia\\losepoint.png",game)
die = Image("SocialMedia\\die.png",game)
dubbed = Image("SocialMedia\\dubbed.png",game)
player1 = Image("SocialMedia\\player1.png",game)
player2 = Image("SocialMedia\\player2.png",game)
thumbsdown = Image("SocialMedia\\thumbsdown.png",game)
thumbsup = Image("SocialMedia\\thumbsup.png",game)
like = Image("SocialMedia\\likes.png",game)
bkkk.resizeTo(800,600)
dies = []
dubs = []
minuspoints = []
losepoints = []
thumbsdowns = []
thumbsups = []
likes = []

title = Image("SocialMedia\\Title.png",game)
title.resizeTo(800,600)
bkkk.draw()
title.draw()
game.drawText("Player 1 ARROW KEYS ",320,400,Font(black,30))
game.drawText("Player 2 WASD ",320,380,Font(black,30))
game.drawText("Collect the Hearts/Thumbs to win!",320,450,Font(black,30))
game.drawText("Press [Space] To Play",320,420,Font(black,30))
game.update(1)
game.wait(K_SPACE)





for times in range(50):
    dies.append(Image("SocialMedia\\die.png",game))
    
for d in dies:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    d.moveTo(x,y)
    d.setSpeed(s,180)
    d.resizeTo(50,50)

for times in range(50):
    dubs.append(Image("SocialMedia\\dubbed.png",game))
    
for d2 in dubs:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    d2.moveTo(x,y)
    d2.setSpeed(s,180)
    d2.resizeTo(50,50)
    
for times in range(50):
    minuspoints.append(Image("SocialMedia\\minuspoint.png",game))
    
for m in minuspoints:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    m.moveTo(x,y)
    m.setSpeed(s,180)
    m.resizeTo(50,50)

for times in range(50):
    losepoints.append(Image("SocialMedia\\losepoint.png",game))
    
for l in losepoints:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    l.moveTo(x,y)
    l.setSpeed(s,180)
    l.resizeTo(50,50)

for times in range(50):
    thumbsdowns.append(Image("SocialMedia\\thumbsdown.png",game))
    
for t in thumbsdowns:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    t.moveTo(x,y)
    t.setSpeed(s,180)
    t.resizeTo(50,50)

for times in range(50):
    thumbsups.append(Image("SocialMedia\\thumbsup.png",game))
    
for t2 in thumbsups:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    t2.moveTo(x,y)
    t2.setSpeed(s,180)
    t2.resizeTo(50,50)
for times in range(50):
    likes.append(Image("SocialMedia\\likes.png",game))
    
for L2 in likes:
    x = randint(50,750)
    y = game.height - randint(100, 10500)
    s = randint(2,5)
    L2.moveTo(x,y)
    L2.setSpeed(s,180)
    L2.resizeTo(50,50)




while not game.over:
    game.processInput()
    minuspoint.draw()
    losepoint.draw()
    thumbsup.draw()
    thumbsdown.draw()
    die.draw()
    like.draw()
    dubbed.draw()
    game.drawBackground()
    minuspoint.moveTo(-1000,1000)
    losepoint.moveTo(-1000,1000)
    dubbed.moveTo(-1000,1000)
    thumbsup.moveTo(-1000,1000)
    like.moveTo(-1000,1000)
    die.moveTo(-1000,1000)

    player2.draw()
    player1.draw()
    player1.resizeTo(50,50)
    player2.resizeTo(50,50)

    for l in losepoints:#loop will go through the list
        l.move()
        if player1.collidedWith(l):
            player1.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            l.moveTo(x,y)
        if player2.collidedWith(l):
            player2.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            l.moveTo(x,y)
    for L2 in likes:#loop will go through the list
        L2.move()
        if player1.collidedWith(L2):
            player1.damage +=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            L2.moveTo(x,y)
        if player2.collidedWith(L2):
            player2.damage +=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            L2.moveTo(x,y)

    for d in dies:#loop will go through the list
        d.move()
        if player1.collidedWith(d):
            game.drawText("PLAYER 2 WINS!",0,0,Font(black,30))

            game.over = True
            
        if player2.collidedWith(d):
            game.drawText("PLAYER 1 WINS!",0,0,Font(black,30))

            game.over = True
            
           
        
    for d2 in dubs:#loop will go through the list
        d2.move()
        if player1.collidedWith(d2):
            player1.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            d2.moveTo(x,y)
        if player2.collidedWith(d2):
            player2.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            d2.moveTo(x,y)
    for m in minuspoints:#loop will go through the list
        m.move()
        if player1.collidedWith(m):
            player1.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            m.moveTo(x,y)
        if player2.collidedWith(m):
            player2.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            m.moveTo(x,y)
            
    for t in thumbsdowns:#loop will go through the list
        t.move()
        if player1.collidedWith(t):
            player1.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            t.moveTo(x,y)
        if player2.collidedWith(t):
            player2.damage -=1
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            t.moveTo(x,y)

    for t2 in thumbsups:#loop will go through the list
        t2.move()
        if player1.collidedWith(t2):
            player1.damage +=2
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            t2.moveTo(x,y)
        if player2.collidedWith(t2):
            player2.damage +=2
            x = randint(50,750)
            y = game.height - randint(100, 10500)
            s = randint(2,5)
            t2.moveTo(x,y)

    if player1.collidedWith(losepoint):
        player1.damage -=1
    if player2.collidedWith(losepoint):
        player2.damage -=1

    

    if player1.damage>=50:#condition (if statement)
        game.drawText("PLAYER 1 WINS!!!!",0,0,Font(black,30))
        game.over=True
    if player2.damage>=50:#condition (if statement)
        game.drawText("PLAYER 2 WINS!!!!",0,0,Font(black,30))
        game.over=True



    '''if player1.damage<=-15:#condition (if statement)
        game.drawText("PLAYER 2 WINS!!!!",300,275)
        game.over=True
    if player2.damage<=-15:#condition (if statement)
        game.drawText("PLAYER 1 WINS!!!!",300,275)
        game.over=True'''


    


        
    if keys.Pressed[K_LEFT]:
        player1.x -=3
    if keys.Pressed[K_RIGHT]:
        player1.x +=3
    if keys.Pressed[K_DOWN]:
        player1.y +=3
        
    if keys.Pressed[K_UP]:
        player1.y -=3
    else:
        player1.speed *= 0.99

    if keys.Pressed[K_a]:
        player2.x -=3
    if keys.Pressed[K_d]:
        player2.x +=3
    if keys.Pressed[K_s]:
        player2.y +=3
    if keys.Pressed[K_w]:
        player2.y -=3
    else:
        player2.speed *= 0.99

    game.drawText("Player 1: " + str(player1.damage),20,50)
    game.drawText("Player 2: " + str(player2.damage),120,50)


         










    
    game.update(50)
game.wait(K_ESCAPE)
game.quit()

    
