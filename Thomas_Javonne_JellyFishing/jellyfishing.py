

#thomas desirae javonne gamers inc
#gone jellyfishing
#catch as many jellyfish before time runs out


from gamelib import*

game = Game(800,600,"Gone Jellyfishing",time =35)
bk = Image("images\\jellyfishfields.jpg",game)
game.setBackground(bk)

bubble = Image("images\\bubbles.png",game)
jelly = Animation("images\\jelly.png",12,game,1024/4,1024/3,2)
bob = Image("images\\bob.png",game)

bob.resizeTo(150,150)
jelly.resizeTo(150,150)
bubble.resizeTo(150,150)
plankton = Image("images\\Plankton_1.png",game)
plankton.resizeTo(150,150)
jelly2 = Animation("images\\jelly.png",12,game,1024/4,1024/3,2)
jelly2.resizeTo(150,150)


jellyfish = []


for times in range(10):
    
    jellyfish.append(Animation("images\\jelly.png",12,game,1024/4,1024/3,2))

   




for jellyf in jellyfish:
    x = game.width + randint(100 ,500)

    y = randint(5 ,550)
   
    jellyf.moveTo(x,y)
    jellyf.setSpeed(8,90)
    
    jellyf.resizeTo(150,150)



title = Image("images\\SPACE.jpg",game)
end = Image("images\\END SCREEN.jpg",game)
title.resizeTo(game.width,game.height)
title.draw()
game.drawText("Press [SPACE] to play",800,600)
game.update(1)
game.wait(K_SPACE)

while not game.over:
    game.processInput()
    bk.draw()
    game.scrollBackground("left",3)
    jelly.draw()         
    #crosshair.moveTo(mouse.x, mouse.y)
    bob.draw()#use arrow keys to move spongebob
    #bubble.draw()
    jelly.moveTo(bob.x - 20,bob.y + 100)
    plankton.draw()
    jelly2.draw()
    jelly2.moveTo(plankton.x-20,plankton.y+100)
    #plankton.moveTo(700,bob.y)


    if bob.collidedWith(plankton):
        bob.health-=1
    if bob.health <= 0:
        game.over = True


    for j in jellyfish:
        j.move()
        
        if bob.collidedWith(j):
            game.score += 1
            x = game.width + randint(100 ,500)
            y = randint(5 ,550)
            j.moveTo(x,y)

            
            
        if j.isOffScreen("left"):
            x = game.width + randint(100 ,500)
            y = randint(5 ,550)
            j.moveTo(x,y)


    if keys.Pressed[K_LEFT]:
        bob.x -= 10
    if keys.Pressed[K_RIGHT]:
       bob.x += 10

 
    if keys.Pressed[K_DOWN]:
        bob.y += 10

    if keys.Pressed[K_UP]:
        bob.y -= 10

    if game.time <= 0:
        game.over = True
        



    plankton.setSpeed(4,90)
    plankton.move()

    if plankton.isOffScreen("left"):
        y = randint(100,500)
        plankton.moveTo(1000,y)

        
        

    game.drawText("Score:" + str(game.score),5,5)
    game.drawText("Time Left: " + str(game.time),700,5)
    game.drawText("Your Health: " + str(bob.health),400,5)





    game.update(60)


end.draw()
game.drawText("Press [SPACE] to Exit       Your Score "+ str(game.score),290,400)
game.update(1)
game.wait(K_SPACE)
game.quit()


