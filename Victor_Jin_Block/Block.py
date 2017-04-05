


from gamelib import *

game = Game(800,600,"Block!")

start=Animation("images//start.gif",84,game,800,600)

bk = Image("images//castle.jpg",game)
bk.resizeTo(game.width,game.height)

run = Animation("images//run ",14,game)
attack = Animation("images//attack ",16,game)
idle = Animation("images//idle ",14,game)
#fly=Animation("images//fireball ",4,game)


runs = Animation("images//runs ",14,game)
attacks = Animation("images//attacks ",15,game)
idles = Animation("images//idle ",14,game)

title = Image("images//Logo.png",game)
title.resizeBy(-15)

bk.draw()
#start.draw()
#start.play()
title.draw()

#game.drawText("Press [SPACE] to play",320,400)
game.update(24)
game.wait(K_SPACE)


fall=[]
for times in range(10):
    fall.append(Animation("images//fireball ",4,game))

for f in fall:
    x = randint(0,800)
    y = randint(-1000,-100)
    #s = randint(2,5)
    f.moveTo(x,y)

    f.draw()
    #f.setSpeed(s,180)





idle.moveTo(300,550)
idles.moveTo(300,550)

run.stop()
run.resizeBy(100)
attack.resizeBy(100)
idle.resizeBy(100)

runs.resizeBy(-50)
attacks.resizeBy(-50)
idles.resizeBy(100)



song=Sound("sound.wav",1)

while not game.over:
    game.processInput()

    song.play()
    
    attack.stop()
    attacks.stop()
    idle.visible=True
    attack.visible=False
    attacks.visible=False

    for f in fall:
        f.rotateTowards(idle)
        f.moveTowards(idle,2)

    

    

    bk.draw()
    if keys.Pressed[K_a]:
        
        
        idle.visible=False
        runs.visible=True
        attack.visible=False
        attacks.visible=False
        runs.nextFrame()
        idle.moveX(-8)
        runs.moveX(-8)
        run.moveX(-8)
        attack.moveX(-8)
        attacks.moveX(-8)
        

        
        runs.moveTo(run.x,run.y)

    elif keys.Pressed[K_d]:
        
        #idle.moveTo(run.x,run.y)
        idle.visible=False
        run.visible=True
        attack.visible=False
        attacks.visible=False
        runs.visible=False
        run.nextFrame()
        idle.moveX(8)
        run.moveX(8)
        runs.moveX(8)
        attack.moveX(8)
        attacks.moveX(8)
        attack.visible=False
        runs.visible=False











        
        
    elif keys.Pressed[K_LEFT]:
        
        attacks.visible=True
        attacks.moveTo(idle.x,idle.y)
        attacks.nextFrame()
        attacks.draw()
        attacks.stop()

        
    elif keys.Pressed[K_RIGHT]:
        
        #attack.moveTo(run.x,run.y)
        #attack.moveTo(runs.x,runs.y)
        attack.visible=True
        attack.moveTo(idle.x,idle.y)
        attack.nextFrame()
        attack.draw()
        attack.stop()
    else:
        idle.moveTo(run.x,run.y)
        idle.draw()

        

    for f in fall:
        f.move()
        
            

            
            
        if f.collidedWith(attack):
            x = randint(0,800)
            y = randint(-1000,-100)
            f.moveTo(x,y)

        if f.collidedWith(attacks):
            x = randint(0,800)
            y = randint(-1000,-100)
            f.moveTo(x,y)

        if f.collidedWith(idle):
            idle.health-=5  
            x = randint(0,800)
            y = randint(-1000,-100)
            f.moveTo(x,y)
        if f.collidedWith(run):
            idle.health-=5
            x = randint(0,800)
            y = randint(-1000,-100)
            f.moveTo(x,y)
        if f.collidedWith(runs):
            idle.health-=5
            x = randint(0,800)
            y = randint(-1000,-100)
            f.moveTo(x,y)

    
        

    if idle.health<=0:
        game.over=True
    if run.health<=0:
        game.over=True

    game.drawText("Health: " + str(idle.health),5,5)


    
    
    game.update(20)
game.quit()


