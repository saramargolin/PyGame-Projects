
from gamelib import*

game = Game(922,518,"Sword Dodger")


bk = Image("images\\dojo.jpg",game)
bk.draw()


heart = Image("images\\heart.png",game)
bomb = Image("images\\bomb.png",game)
ninja = Image("images\\ninja.png",game)
sword2 = Image("images\\sword2.png",game)
sword = Image("images\\sword.png",game)
end = Image("images\\game-over.png",game)



sword.setSpeed(17,90)
bomb.setSpeed(10,90)
heart.setSpeed(10,90)
sword2.setSpeed(17,90)
ninja.moveTo(100,450)
count = 0

game.drawText("Sword Dodger",game.width/4 ,game.height/4,Font(red,90,blue))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(blue,40,green))
game.update()
game.wait(K_SPACE)


while not game.over:
    game.processInput()
    
    bk.draw()
    ninja.move()
    ninja.draw()
    ninja.resizeTo(100,100)
    sword.resizeTo(200,ninja.height)
    sword2.resizeTo(200,ninja.height)
    bomb.resizeTo(100,ninja.height)
    heart.resizeTo(100,ninja.height)
    end.resizeTo(922,518)
    sword.move()
    sword2.move()
    bomb.move()
    heart.move()
    

    
        
    if bomb.isOffScreen("left"):
        x = game.width + 200
        y = randint(120,  900)
        bomb.moveTo( x, y )
        bomb.visible = True

    if heart.isOffScreen("left"):
        x = game.width + 200
        y = randint(170,  2000)
        heart.moveTo( x, y )
        heart.visible = True

    
    if sword2.isOffScreen("left"):
        x = game.width + 200
        y = randint(170,  490)
        sword2.moveTo( x, y )
        sword2.visible = True
        

    if sword.isOffScreen("left"):
        x = game.width + 100
        y = randint(100,  518)
        sword.moveTo( x, y )
        sword.visible = True

        
    if ninja.isOffScreen("all"):
        ninja.moveTo(randint(100,300),randint(-280,510))
        
        
    if ninja.collidedWith(sword2):
        ninja.damage+=10
        sword2.visible = False

        
    if ninja.collidedWith(sword):
        ninja.damage+=10
        sword.visible = False 

        
    if ninja.collidedWith(bomb):
        ninja.damage+=15
        bomb.visible = False
        
    if ninja.collidedWith(heart):
        ninja.damage-=10
        heart.visible = False

    if ninja.damage>=100:#condition (if statement)
        end.draw()
        game.update()
        game.wait(K_SPACE)
        
        

    
        
    '''if ninja.collidedWith(speed):#I cant get the ninja to move faster once it collides with the bolt
        speed.visible = False'''
    
    if keys.Pressed[K_LEFT]:
        ninja.moveX(-5)
        
    if keys.Pressed[K_UP]:
        ninja.moveY(-5)
        
    if keys.Pressed[K_RIGHT]:
        ninja.moveX(5)
        
    if keys.Pressed[K_DOWN]:
        ninja.moveY(5)
        
    if game.score>=100:
        game.over = True
        
    game.drawText("Ninja Damage: " + str(ninja.damage),5,5)
    game.update(60)
game.quit()
