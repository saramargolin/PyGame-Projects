from gamelib import *

game = Game(600,400,"Jumping")
bk = Image("characters//background//Stage_Akuma.gif",game)
bk.resizeTo(game.width, game.height)

loading = Image("games//death battles//images//loading.gif",game)
loading.resizeTo(game.width, game.height)

eegg = Image("games//death battles//images//images.jpg",game)
eegg.resizeTo(game.width,game.height)

############################HAGGAR2#############################################

haggar2 = Image("characters//haggar evil//haggare idle.png",game)
haggar2.moveTo(400,100)

haggarpu2 = Animation("characters//haggar evil//haggare punch1 ",3,game)
haggarpu2.moveTo(haggar2.x,haggar2.y)
haggarpu2.stop()

haggarp22 = Animation("characters//haggar evil//haggare punch2 ",3,game)
haggarp22.moveTo(haggar2.x,haggar2.y)
haggarp22.stop()

haggarw2 = Animation("characters//haggar evil//haggare ",6,game)
haggarw2.moveTo(haggar2.x,haggar2.y)
haggarw2.stop()
############################HAGGAR############################################

haggar = Image("characters//haggar//haggar_idle.png",game)
haggar.moveTo(200,100)

haggarp = Animation("characters//haggar//haggar punch1 ",3,game)
haggarp.moveTo(haggar.x,haggar.y)
haggarp.stop()

haggarp2 = Animation("characters//haggar//haggar punch2 ",3,game)
haggarp2.moveTo(haggar.x,haggar.y)
haggarp2.stop()

haggarw = Animation("characters//haggar//haggar ",6,game)
haggarw.moveTo(haggar.x,haggar.y)
haggarw.stop()

#bar = Image("images\\paddle.png",game)
#bar.setSpeed(4,90)

haggar.health = 500
haggar2.health = 500
jumping2 = False
jumping = False
landed2 = False
landed = False
factor2 = 1
factor = 1

loading.draw()
game.drawText("Press space to play",200,250)
game.drawText("player 1: (W,A,D) to move and jump (F,R) to punch",140,50)
game.drawText("player 2: (I,J,L) to move and jump (H,Y) to punch",150,100)
game.update(1)
game.wait(K_SPACE)


while not game.over:
    game.processInput()
    haggarw.moveTo(haggar.x,haggar.y)
    haggarp.moveTo(haggar.x,haggar.y)
    haggarp2.moveTo(haggar.x,haggar.y)
    haggarw2.moveTo(haggar2.x,haggar2.y)
    haggarpu2.moveTo(haggar2.x,haggar2.y)
    haggarp22.moveTo(haggar2.x,haggar2.y)
    bk.draw()
    #bar.move()

    if haggar.x < 0 and haggar2.x < 0:
        eegg.draw()
    
    #if bar.isOffScreen("left"):
        #bar.moveTo(game.width,randint(250,350))
    
#########################player1vsplayer2#############################################        

    if keys.Pressed[K_a]:
        haggarw.nextFrame()
        haggar.x -= 8
        haggar.visible = False
        haggarw.visible = True
    elif keys.Pressed[K_d]:
        haggarw.prevFrame()
        haggar.x += 8
        haggar.visible = False
        haggarw.visible = True
    elif keys.Pressed[K_f]:
        haggarp.nextFrame()
        haggarp.visible = True
        haggar.visible = False
        haggarw.visible = False
    elif keys.Pressed[K_r]:
        haggarp2.nextFrame()
        haggarp2.visible = True
        haggar.visible = False
        haggarw.visible = False
    else:
        haggarw.draw()
        haggarp2.visible = False
        haggarp.visible = False
        haggarw.visible = False
        haggar.visible = True
###
    if keys.Pressed[K_j]:
        haggarw2.nextFrame()
        haggar2.x -= 8
        haggar2.visible = False
        haggarw2.visible = True
    elif keys.Pressed[K_l]:
        haggarw2.prevFrame()
        haggar2.x += 8
        haggar2.visible = False
        haggarw2.visible = True
    elif keys.Pressed[K_h]:
        haggarpu2.nextFrame()
        haggarpu2.visible = True
        haggar2.visible = False
        haggarw2.visible = False
    elif keys.Pressed[K_y]:
        haggarp22.nextFrame()
        haggarp22.visible = True
        haggar2.visible = False
        haggarw2.visible = False
    else:
        haggarw2.draw()
        haggarp22.visible = False
        haggarpu2.visible = False
        haggarw2.visible = False
        haggar2.visible = True
##
    if haggarp.collidedWith(haggar2,"rectangle") or haggarp.collidedWith(haggarpu2,"rectangle") or haggarp.collidedWith(haggarp22,"rectangle") or haggarp.collidedWith(haggarw2,"rectangle"):
        haggar.health -= 2

    if haggarp2.collidedWith(haggar2,"rectangle") or haggarp2.collidedWith(haggarpu2,"rectangle") or haggarp2.collidedWith(haggarp22,"rectangle") or haggarp2.collidedWith(haggarw2,"rectangle"):
        haggar.health -= 2

    if haggarpu2.collidedWith(haggar,"rectangle") or haggarpu2.collidedWith(haggarp,"rectangle") or haggarpu2.collidedWith(haggarp2,"rectangle") or haggarpu2.collidedWith(haggarw,"rectangle"):
        haggar2.health -= 2

    if haggarp22.collidedWith(haggar,"rectangle") or haggarp22.collidedWith(haggarp,"rectangle") or haggarp22.collidedWith(haggarp2,"rectangle") or haggarp22.collidedWith(haggarw,"rectangle"):
        haggar2.health -= 2
        
##################################Player1#############################################       
    if haggar.health < 0:
        game.drawText("player 1 wins!!!",225,100)
        game.over = True
    
    if haggar.y < 300:
        landed = False
        #if haggar.collidedWith(bar,"rectangle"):
            #landed = True
            #haggar.moveX(-4)

    else:
        landed = True
        
    if jumping:
        haggar.y -= 23 * factor
        factor *= .95
        landed = False
        
        if factor < .18:
            jumping = False
            factor = 1
    
    if keys.Pressed[K_w] and landed and not jumping:
        jumping = True
        
    if not landed:
        haggar.y += 9

#########################Player2############################################################
    if haggar2.health < 0:
        game.drawText("player 2 wins!!!",225,100)
        game.over = True

    if haggar2.y < 300:
        landed2 = False
        #if haggar.collidedWith(bar,"rectangle"):
            #landed = True
            #haggar.moveX(-4)

    else:
        landed2 = True
        
    if jumping2:
        haggar2.y -= 23 * factor2
        factor2 *= .95
        landed2 = False
        
        if factor2 < .18:
            jumping2 = False
            factor2 = 1
    
    if keys.Pressed[K_i] and landed2 and not jumping2:
        jumping2 = True
        
    if not landed2:
        haggar2.y += 9
#################################################################################        

    game.drawText("player 2: " + str(haggar.health),470,10)
    game.drawText("player 1: " + str(haggar2.health),5,10)

    haggar.draw()
    haggarp.draw()
    haggarp2.draw()
    haggar2.draw()
    haggarp2.draw()
    haggarp22.draw()
    
    game.update(20)
    
game.drawText("Press space to quit",200,150)
game.update(1)
game.wait(K_SPACE)
game.quit()


