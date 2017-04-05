#AA (Anamatronic Arts)
# By Chuhan Lin, San Joon Jung, Justin Chen
#Demon Attack
from gamelib import*

game = Game(1600,500, "Demon Attack")

bk = Animation("GameImages\\backgroundSprite.png",20,game,3200/4,1680/5)
game.setBackground(bk)
bk.resizeTo(game.width,game.height)
hero = Animation("GameImages\\heroIdle.png",4,game,207/3,134/2)
#heroMove = Animation("GameImages\\heroMove.png",1,game,71,62)
heroAttack = Animation("GameImages\\heroAttack.png",23,game,363/3,960/8)
#heroLimitAtk = Animation("GameImages\\heroLimitAtk.png",60,game,993/3,5020/20)
fireball = Animation("GameImages\\fireballSprite.png",5,game,480/2,420/3)
slash = Animation("GameImages\\slashSprite.png",7,game,576/3,576/3)
#castle = Image("GameImages\\castle.jpg",game)
blood = Animation("GameImages\\bloodSprite.png",9,game,459/3,369/3)
blood1 = Animation("GameImages\\blood1Sprite.png",9,game,450/3,411/3)
hulks = Animation("GameImages\\HulkSprite.png",16,game,608/4, 572/4)
drDoomStrike = Animation("GameImages\\drDoomStrike.png",25,game,1245/5,800/5)
heroWin = Animation("GameImages\\heroWin.png",28,game,285/3,1210/10)
drDoomStrike = Animation("GameImages\\drDoomStrike.png",25,game,1245/5,800/5)
drDoomStrike.resizeBy(40)
drDoomIntro = Image("GameImages\\drDoomIntro.png",game)
drDoomIntro.resizeBy(140)
heroWin.resizeBy(50)
drDoomStrike.resizeBy(27)


#castle.resizeTo(400,300)
#castle.moveTo(400,350)
                  
villains = []
villains2 = []
villains3 = []
hulk = []
hulk2 = []
coin = []
drDoom = []

for num in range(5):
    villains.append(Animation("GameImages\\villainSprite.png",16,game,3200/4,3200/4))

for num in range(7):
    villains2.append(Animation("GameImages\\villainSprite.png",16,game,3200/4,3200/4))

for num in range(10):
    villains3.append(Animation("GameImages\\villainSprite.png",16,game,3200/4,3200/4))

for num in range(1):
    hulk.append(Animation("GameImages\\HulkSprite.png",16,game,608/4, 572/4))

for num in range(1):
    hulk2.append(Animation("GameImages\\HulkSprite.png",16,game,608/4, 572/4))

for num in range(1):
    coin.append(Animation("GameImages\\coinSprite.png",40,game,2345/7,2154/6))

for num in range(1):
    drDoom.append(Animation("GameImages\\DrdoomSpriteWalk.png",10,game,510/2,1030/5))

for d in drDoom:
    d.moveTo(-200,363)
    d.setSpeed(4,270)
    d.resizeBy(27)
    
for h in hulk:
    h.moveTo(-300,390)
    h.setSpeed(2,270)
    h.resizeBy(40)

for h2 in hulk2:
    h2.moveTo(-300,390)
    h2.setSpeed(2,270)
    h2.resizeBy(40)
    
for v in villains:
    v.resizeTo(190,135)
    x = randint(-800,-500)
    s = randint(2,11)
    v.moveTo(x,450)
    v.setSpeed(s,270)

for v2 in villains2:
    v2.resizeTo(190,135)
    x = randint(-1000,-100)
    s = randint(2,11)
    v2.moveTo(x,450)
    v2.setSpeed(s,270)

for v3 in villains3:
    v3.resizeTo(190,135)
    x = randint(-1000,-100)
    s = randint(2,11)
    v3.moveTo(x,450)
    v3.setSpeed(s,270)

for c in coin:
    c.resizeBy(-82)
    x = randint(-800,-500)
    y = randint(310,370)
    c.moveTo(x,y)
    s = randint(4,7)
    c.setSpeed(s,270)

exp = 0
Time = 0

fireball.visible = False 
blood.resizeBy(-40)
blood.visible = False
slash.visible = False
blood1.visible = False
slash.resizeBy(-30)
blood1.resizeBy(-30)

#splash screen 1
villain = Animation("GameImages\\villainSprite.png",16,game,3200/4,3200/4)
bk1 = Image("GameImages\\background2.jpg",game)
logo = Image("GameImages\\logo2.png",game)
bk1.resizeTo(game.width,game.height)
bk1.draw()
#coin.draw()
logo.resizeBy(20)
logo.moveTo(logo.x,logo.y-120)
logo.draw()
drDoomIntro.moveTo(140,280)
drDoomIntro.draw()
hero.resizeBy(200)
hero.moveTo(1470,370)
hero.draw()
hulks.resizeBy(150)
hulks.moveTo(320,280)
villain.resizeBy(-70)
villain.moveTo(hulks.x+100, hulks.y+120)
villain.draw()
villain.moveTo(hulks.x+180, hulks.y+120)
villain.draw()
villain.moveTo(hulks.x+260, hulks.y+120)
villain.draw()
villain.moveTo(hulks.x+340, hulks.y+120)
villain.draw()
villain.stop()
game.drawText("Press SPACE to Continue",700,450)
game.update(1)
game.wait(K_SPACE)

hero.moveTo(1400,450)

h.health = 1000 #hulk HP
h2.health = 1500#hulk2 hp
d.health = 2000#DR DOOM HP

hulkIntro = Image("GameImages\\hulkIntro.png",game)
hulkStrike = Animation("GameImages\\HulkStrike.png",4,game,502/2,440/2)
hulkStrike.resizeBy(40)
hulkStrike.visible = True
hulkStrike2 = Animation("GameImages\\HulkStrike.png",4,game,502/2,440/2)
hulkStrike2.resizeBy(40)
hulkStrike2.visible = True

#drDoom = Animation("GameImages\\DrdoomSpriteWalk.png",10,game,510/2,1030/5) ####DRDOOM
#drDoom.resizeBy(40)
drDoomIntro1 = Image("GameImages\\drDoomIntro.png",game)
drDoomIntro1.resizeBy(40)
hulkIntro.resizeBy(40)
NextSlide2 = 10
while not game.over: #splash screen 2
    game.processInput()
    bk3 = Image("GameImages\\background4.jpg",game)
    bk3.resizeTo(game.width,game.height)
    bk3.draw()
    game.drawText("STAGE 1", 125,30)
    game.drawText(" x 1 (1000HP) ", 250,185)
    hulkIntro.moveTo(145,185)
    hulkIntro.draw()
    game.drawText(" 5 Clones ",185,400)
    villain.moveTo(140,400)
    villain.draw()
    game.drawText("STAGE 2", 730,30)
    game.drawText(" x 1  (1500HP) ", 855,185)
    hulkIntro.moveTo(750,185)
    hulkIntro.draw()
    game.drawText(" 10 Clones ",805,400)
    villain.moveTo(750,400)
    villain.draw()
    drDoomIntro1.moveTo(1250,185)
    game.drawText(" Final Stage ", 1235,30)
    game.drawText(" x 1 (2000HP) ", 1400,185)
    villain.moveTo(1250,400)
    villain.draw()
    game.drawText(" 15 Clones ", 1300, 400)
    drDoomIntro1.draw()
    #blankaIntro.moveTo(1300,185)###############################
    #blankaIntro.draw()##################################
    
    game.drawText("NEXT SLIDE IN : " + str(NextSlide2),750,480)
    game.drawText("Hold [1] to fast forward!", 730,455)

    if keys.Pressed[K_1]:
        break

    NextSlide2 -=1
    
    if NextSlide2 == 0:
        break

    game.update(1)
game.update()

NextSlide = 30
countDown = Sound("GameImages\\countdown3-0.wav",1)
while not game.over: #splash screen 3
    game.processInput()
    bk2 = Image("GameImages\\background3.jpg",game)
    bk2.resizeTo(game.width,game.height)           
    bk2.draw()
    NextSlide -=1
    game.drawText("GAME STARTS IN : " + str  (NextSlide) + ("    Get Ready!"),700,460)
    game.drawText(" You've Entered The Demons' Castle!", 650,30)
    game.drawText("             They Will Not Let You Out Alive! The Only Way Out Is To Kill All Demons", 480,60)
    game.drawText(" Instructions ", 20, 150)
    game.drawText(" - Press F To Shoot Fireballs",70,180)
    game.drawText(" - Press R To Use Hero's Ability",70,210)
    game.drawText(" - Press RIGHT Button To Move Right ",70,240)
    game.drawText(" - Press LEFT Button To Move Left",70,270)
    game.drawText(" - Press UP Button To JUMP",70,300)
    game.drawText(" How To Win/Lose ", 390,150)
    game.drawText(" - Kill All The Boss To Win!", 440, 180)
    game.drawText(" - If The Time Hits 4000, The Game Ends And You Lose!", 440,210)
    game.drawText(" - If The Hero's Health Goes Below 0 You Lose! ", 440, 240)
    game.drawText(" - Tips And Tricks ", 900, 150)
    game.drawText(" - There Are Only 1 actual Demon In Each Wave, The others Are All Clones!", 950, 180)
    game.drawText(" Find the Actual One To Kill The Rest!", 950, 210)
    game.drawText(" - Jump To Collect Coins To Gain Extra EXP and Energy", 950,240)
    game.drawText(" - It Costs 100 Energy To Use FireBall And 3 Stamina To Use Hero's Attack Ability", 950, 270)
    game.drawText(" - First Boss Appears When Time Reaches 200 and The Others Will", 950,300)
    game.drawText(" Follow With Their Own Troops When The Previous One Dies ", 950,330)
    game.drawText(" -If Both The Little Demons And The Boss Goes Off The Screen It Will Reappear", 950,360)
    game.drawText(" From The Left Of The Screen Until You Kill Them", 950, 390)

    game.drawText("Hold [2] to fast forward!", 700,430)

    if keys.Pressed[K_2]:
        NextSlide = 2
        
    if NextSlide <=2 and not keys.Pressed[K_2]:
        countDown.play()
        
    if NextSlide == 0:
        break
    
    game.update(1)#game takes about 30 seconds to start 
game.update()
vdmg = 0
vdmg2 = 0
vdmg3 = 0
lastStage = 0
################### Sounds #####################
#themeSound = Sound("GameImages\\themeSound.wav",1)
fireballSound = Sound("GameImages\\fireballSound.wav",2)
boom1 = Sound("GameImages\\boom1.wav",6) #main boom
boom2 = Sound("GameImages\\boom2.wav",6)
heroWalking = Sound("GameImages\\walking.wav",3)
hulkWalk = Sound("GameImages\\walking2.wav",4)
swordSlash = Sound("GameImages\\swordSlash1.wav",5)
coinSound = Sound("GameImages\\coinSound.wav",2)
drDoomWalk = Sound("GameImages\\drDoomFootstep.wav",4)
zap = Sound("GameImages\\drDoomZap.wav",4)
heroJump = Sound("GameImages\\heroJump.wav",7)
#bloodEffect = Sound("GameImages\\bloodEffect2.mp3",2)

hero.health = 500
stage1Intro = Animation("GameImages\\stage1Sprite.png",2,game,32/1,64/2)
stage1Intro.resizeBy(500)
gameover = Image("GameImages\\gameover.png",game)
energy = 0
gameText1 = 0
gameText2 = 0
gameoverText = 0
#stage1 = False
#stage2 = False
#x = 0
jumping = False #Used to check to see if you are jumping
landed = False #Used to check to see if you have landed on the ground
factor = 1 #Used for a slowing effect of the jumping
#heroMove.resizeBy(40)
while not game.over:
    game.processInput()
    bk.move()
    #themeSound.play()
    #stage1Intro.moveTo(800,90)
    #stage1Intro.move()
    #hulkStrike.visible = True
    #hulkStrike.move()
    hero.move()
    hero.resizeTo(100,75)
    fireball.resizeTo(100,50)
    heroAttack.resizeTo(200,150)
    fireball.move()
    slash.moveTo(10000,10000)
    blood.moveTo(10000,10000)
    hero.move()
    #z = 50*x
    #heroMove.moveTo(10000,10000)
    #hulk.move()
    exp+=1
    Time +=1
    c.move()
    #hero.angleTo(h)

    for c in coin:
        c.move()
        if hero.collidedWith(c)or heroAttack.collidedWith(c):
            coinSound.play()
            x = randint(-800,-500)
            y = randint(300,370)
            c.moveTo(x,y)
            exp += 100
            energy +=50

        if c.isOffScreen("right"):
            x = randint(-800,-500)
            y = randint(300,370)
            c.moveTo(x,y)
    
    if hero.y < 450:
        landed = False
        if hero.collidedWith(bk,"rectangle"):
            landed = False
        #450 is the floor.  Decision can be replaced with a more complex condition based on game
    else:
        landed = True
        
    if jumping:
        hero.y -= 70 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .90
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .8:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True
            heroJump.play()
            
    if not landed:
        hero.y += 15

    
    for v in villains:
        v.move()
        if v.collidedWith(heroAttack):
            blood1.moveTo(v.x,v.y)
            blood1.visible = True
            blood1.move()
        if v.collidedWith(hero):
            blood.moveTo(hero.x,hero.y)
            blood.visible = True
            slash.moveTo(hero.x-10,hero.y)
            slash.visible = True
        if v.collidedWith(heroAttack) and energy > 0:
            #bloodEffect.play()
            vdmg+=1
        if v.collidedWith(fireball):
            boom1.play()
            v.visible = False
            game.score +=1
            v.moveTo(-1000000000,1000)
            fireball.moveTo(5000,1000)

        if v.isOffScreen("right"):
            x = randint(-1000,-200)
            v.moveTo(x,450)

        #if v.x >= hero.x-60 <= hero.x:
        if v.collidedWith(hero):
            v.setSpeed(0,270)

        if v.x >= hero.x or v.x <= hero.x-60:
            s = randint(2,11)
            v.setSpeed(s,270)

        #if v.x is not hero.x:
            #s = randint(3,5)
            #v.setSpeed(s,270)
    
        if vdmg >=200:
            v.visible = False
            #v.moveTo(-10000,10000)

    #if not v.collidedWith(hero):

    if keys.Pressed[K_r]:
        swordSlash.play()
        energy -=3
        heroAttack.move()
        heroAttack.moveTo(hero.x-20,hero.y-40)
        hero.visible = False
        
    #if keys.Pressed[K_e]:
        #heroLimitAtk.move()
        #heroLimitAtk.moveTo(hero.x,hero.y-50)
        #hero.visible = False

    #if v.collidedWith(heroLimitAtk):
            #game.score+=1

    if keys.Pressed[K_LEFT]:
        heroWalking.play()
        hero.nextFrame()
        hero.moveX(-20)
        #hero.visible = False
        #heroMove.moveTo(hero.x,hero.y+5)
        
    elif keys.Pressed[K_RIGHT]:
        heroWalking.play()
        hero.prevFrame()
        hero.moveX(20)
        #hero.visible = False
        #heroMove.moveTo(hero.x,hero.y+5)
        
    if not keys.Pressed[K_r]:
        heroAttack.moveTo(40000,40000)
        energy +=1
        hero.visible = True
        
    if keys.Pressed[K_f] and exp >= 100:
        fireball.visible = True
        fireballSound.play()
        fireball.moveTo(hero.x-50,hero.y-10)
        fireball.setSpeed(75, 90)
        exp -=100
        #x +=1

    #if fireball.collidedWith(h) or fireball.collidedWith(v):
        #x = 0
        
    if exp <= 0:
        fireball.moveTo(100000,100000)
        fireball.visible = False
        exp = 0
        game.drawText("Not Enough EXP To Use Fireball!", 200, 25)

    if exp <=100:
        game.drawText("Not Enough EXP To Use Fireball!", 200, 25)

    if energy <= 0:
        energy = 0
        game.drawText("Not Enough Energy!", 10,25)
        

    if fireball.collidedWith(h) or fireball.collidedWith(hulkStrike): #h = hulk
        boom2.play()
        h.health -= 100
        fireball.moveTo(5000,1000)

    if fireball.isOffScreen("left"):
        fireball.moveTo(5000,5000)
        fireball.visible = False

    #if v.x >= castle.x+100:
        #castle.health -=1
        #slash.moveTo(castle.x,castle.y)
        #slash.move()
        
    if hero.isOffScreen("right"):
        hero.moveTo(1600,450)

    if Time >= 3000:
        game.drawText("Time Is About To Run Out!", 700, 150)

    #if v.x 

    if h.isOffScreen("right"):
        h.moveTo(-500,390)

    if hero.health <=0:
        game.drawText("Press [SPACE] To Exit!",700,300)
        gameover.draw()
        #if keys.Pressed[K_SPACE]:
        game.over = True
        '''def gamee():
            return play_again()
        def play_again():
            while True:
                again = input("Would you like to play again? Type y for yes or type n for no-")
                if again not in {"y","n"}:
                    print("please enter valid input")
                elif again == "n":
                    return "Thanks for Playing, good bye!"
                elif again == "y":
                    return gamee()'''
        
    if Time >= 200:
        for h in hulk: ################# Hulk
            h.move()
            if h.health > 0 or h2.health > 0:
                hulkWalk.play()
            if h.health >0:
                game.drawText("BOSS INCOMING!", 950, 40)
                game.drawText("BOSS Health:" + str(h.health), 950,10)
            if heroAttack.collidedWith(h) and energy > 0:
                #bloodEffect.play()
                h.health-=2

            if heroAttack.collidedWith(hulkStrike) and energy > 0:
                h.health -=2
                
            if h.collidedWith(heroAttack):
                blood1.moveTo(h.x,h.y)
                blood1.visible = True

            if hulkStrike.collidedWith(heroAttack):
                blood1.moveTo(hulkStrike.x-25,hulkStrike.y+50)
                blood1.draw()
                blood1.visible = True

            #if hulkStrike.x >= hero.x:          
                
            #if h.collidedWith(hero):
            if h.x >= hero.x-100: #and h.x+100 <= hero.x:
                h.visible = False
                #h.visible = False
                hulkStrike.moveTo(h.x-25,h.y-51)
                hulkStrike.visible = True
                h.setSpeed(0,270)
                blood.visible = True
                if h.x >= hero.x-100 and hero.x >= h.x:
                    blood.moveTo(hero.x,hero.y)
                if hero.collidedWith(blood) and h.x <= hero.x or heroAttack.collidedWith(blood) and h.x <= hero.x:
                    hero.health -=1
                
            if h.x >= hero.x or h.x <= hero.x-100:
                h.setSpeed(2,270)
                h.visible = True
                hulkStrike.visible = False
                hulkStrike.moveTo(-10000,10000)
                blood.moveTo(10000,10000)
                
            if h.health <=0: ################# stage 2
                hulkStrike.moveTo(-10000,10000)
                h.moveTo(-10000,100000)
                gameText1 +=1
                if gameText1 <=50:
                    game.drawText("First Boss Is Dead, Second Boss Is Approaching With His Troops!",550,300)
                    
                if h2.health > 0:
                    game.drawText("BOSS 2 Health:" + str(h2.health), 950,10)
                    
                for h2 in hulk2:
                    h2.move()
                    if h2.isOffScreen("right"):
                        h2.moveTo(-500,390)
                    if h2.x >= hero.x-100: #and h.x+100 <= hero.x:
                        h2.visible = False
                        #h.visible = False
                        hulkStrike2.moveTo(h2.x-25,h2.y-51)
                        hulkStrike2.visible = True
                        h2.setSpeed(0,270)
                        blood.visible = True
                        if h2.x >= hero.x-100 and hero.x >= h2.x:
                            blood.moveTo(hero.x,hero.y)
                        if hero.collidedWith(blood) and h2.x <= hero.x or heroAttack.collidedWith(blood) and h2.x <= hero.x:
                            hero.health -=1

                    if heroAttack.collidedWith(h2) and energy > 0:
                        #bloodEffect.play()
                        h2.health-=2

                    if heroAttack.collidedWith(hulkStrike2) and energy > 0:
                        h2.health -=2
                        
                    if h2.collidedWith(heroAttack):
                        blood1.moveTo(h2.x,h2.y)
                        blood1.visible = True

                    if hulkStrike2.collidedWith(heroAttack):
                        blood1.moveTo(hulkStrike2.x-25,hulkStrike2.y+50)
                        blood1.draw()
                        blood1.visible = True
                
                    if h2.x >= hero.x or h2.x <= hero.x-100:
                        #hulkWalk.play()
                        h2.setSpeed(2,270)
                        h2.visible = True
                        hulkStrike2.visible = False
                        hulkStrike2.moveTo(-10000,10000)
                        blood.moveTo(10000,10000)

                    if fireball.collidedWith(h2) or fireball.collidedWith(hulkStrike2): #h = hulk
                        boom2.play()
                        h2.health -= 100
                        fireball.moveTo(5000,1000)

                    if h2.health <=0:
                        gameText2 +=1
                        if gameText2 < 70:
                            game.drawText("Second Boss Is Dead, Last Boss is Approaching!",600,300)  
                        h2.moveTo(-10000,10000)
                        hulkStrike2.moveTo(-10000,10000)
                        lastStage +=1
                        if lastStage > 70:
                            #themeSound.play()
                            for v3 in villains3:
                                v3.move()
                                
                                if v3.collidedWith(heroAttack):
                                    blood1.moveTo(v3.x,v3.y)
                                    blood1.visible = True
                                    blood1.move()

                                if v3.collidedWith(blood1) and energy > 0:
                                    vdmg3 +=1

                                if v3.collidedWith(hero):
                                    blood.moveTo(hero.x,hero.y)
                                    blood.visible = True
                                    slash.moveTo(hero.x-10,hero.y)
                                    slash.visible = True
                                #if v2.collidedWith(heroAttack):
                                    #bloodEffect.play()
                                    #vdmg+=1
                                if v3.collidedWith(fireball):
                                    boom1.play()
                                    v3.visible = False
                                #game.score +=1
                                    v3.moveTo(-10000000,1000)
                                    fireball.moveTo(5000,1000)

                                if v3.isOffScreen("right"):
                                    x = randint(-1000,-200)
                                    v3.moveTo(x,450)

                                #if v.x >= hero.x-60 <= hero.x:
                                if v3.collidedWith(hero):
                                    v3.setSpeed(0,270)

                                if v3.x >= hero.x or v3.x <= hero.x-60:
                                    s = randint(2,11)
                                    v3.setSpeed(s,270)

                                if vdmg3 > 350:
                                    v3.moveTo(-30000,10000)
                                
                            for d in drDoom:
                                d.move()
                                if d.health > 0:
                                    game.drawText("BOSS 3 Health:" + str(d.health), 950,10)
                                    
                                if d.x >= hero.x-100: #and h.x+100 <= hero.x:
                                    #zap.play()
                                    d.visible = False
                                    #h.visible = False
                                    drDoomStrike.moveTo(d.x-25,d.y+40)
                                    drDoomStrike.visible = True
                                    d.setSpeed(0,270)
                                    blood.visible = True
                                    
                                if d.x >= hero.x-100 and hero.x >= d.x:
                                    zap.play()
                                    blood.moveTo(hero.x,hero.y)
                                if hero.collidedWith(blood) and d.x <= hero.x or heroAttack.collidedWith(blood) and d.x <= hero.x:
                                    hero.health -=1
                
                                if d.x >= hero.x or d.x <= hero.x-100:
                                    drDoomWalk.play()
                                    d.setSpeed(2,270)
                                    d.visible = True
                                    drDoomStrike.visible = False
                                    drDoomStrike.moveTo(-10000,10000)
                                    blood.moveTo(10000,10000)
                                    
                                if fireball.collidedWith(d) or fireball.collidedWith(drDoomStrike): #h = hulk
                                    boom2.play()
                                    d.health -= 100
                                    fireball.moveTo(5000,1000)

                                if heroAttack.collidedWith(d) and energy > 0:
                                    #bloodEffect.play()
                                    d.health-=2

                                if heroAttack.collidedWith(drDoomStrike) and energy > 0:
                                    d.health -=2
                        
                                if d.collidedWith(heroAttack):
                                    blood1.moveTo(d.x,d.y)
                                    blood1.visible = True

                                if drDoomStrike.collidedWith(heroAttack):
                                    blood1.moveTo(drDoomStrike.x-25,drDoomStrike.y+50)
                                    blood1.draw()
                                    blood1.visible = True

                                if d.isOffScreen("right"):
                                    d.moveTo(-300,363)

                                if d.health <=0:
                                    gameover.draw()
                                    hero.moveTo(hero.x,10000)
                                    heroWin.moveTo(hero.x,420)
                                    heroWin.move()
                                    d.visible = False
                                    v3.visible = False
                                    game.drawText("You Win! Press [SPACE] To exit", gameover.x, gameover.y+45)
                                    gameoverText +=1
                                    if gameoverText > 33:
                                        game.over = True
                            
                for v2 in villains2:
                    v2.move()
                    if v2.collidedWith(heroAttack):
                        blood1.moveTo(v2.x,v2.y)
                        blood1.visible = True
                        blood1.move()

                    if v2.collidedWith(blood1) and energy > 0:
                        vdmg2 +=1

                    if v2.collidedWith(hero):
                        blood.moveTo(hero.x,hero.y)
                        blood.visible = True
                        slash.moveTo(hero.x-10,hero.y)
                        slash.visible = True
                    #if v2.collidedWith(heroAttack):
                        #bloodEffect.play()
                        #vdmg+=1
                    if v2.collidedWith(fireball):
                        boom1.play()
                        v2.visible = False
                        #game.score +=1
                        v2.moveTo(-10000000,1000)
                        fireball.moveTo(5000,1000)

                    if v2.isOffScreen("right"):
                        x = randint(-1000,-200)
                        v2.moveTo(x,450)

                        #if v.x >= hero.x-60 <= hero.x:
                    if v2.collidedWith(hero):
                        v2.setSpeed(0,270)

                    if v2.x >= hero.x or v2.x <= hero.x-60:
                        s = randint(2,11)
                        v2.setSpeed(s,270)

                    #if h2.x >= hero.x-100: #and h.x+100 <= hero.x:
                        #h2.visible = False
                        #h.visible = False
                        #hulkStrike.moveTo(h2.x-25,h2.y-51)
                        #hulkStrike.visible = True
                        #h2.setSpeed(0,270)
                        #blood.visible = True 

                    if vdmg2 >=275:
                        v2.moveTo(-2200,1000)

    if hero.collidedWith(slash) or hero.collidedWith(blood):
        hero.health-=1
                          
    if Time >=4000:
        game.drawText("Press [SPACE] To Exit",700,300)
        game.drawText("You Lost! Press [SPACE] To exit", gameover.x, gameover.y+45)
        gameover.draw()
        #if keys.Pressed[K_SPACE]:
        #game.stop()
        game.over = True
        #game.over = True

        

    #if Mouse.collidedWith(game.drawText) and mouse.Leftbutton:
        #game.over = True
    #if h.health >0:
    game.drawText("Hero's Energy:" + str(exp),200,5)
    
    game.drawText("Stamina:" + str(energy),10,5)

    game.drawText("Hero's Health:" + str(hero.health),1450,5)

    game.drawText("Time:" + str(Time),1450,30)
    

    #game.drawText("Fireball:" + str(x),1050,30)
    
    #game.drawText("Z:" + str(z),1050,60)
    
    #game.drawText("Castle Health:" + str(castle.health),1450,25)

    
    game.update(10)
game.update()

#while not game.over:
    #game.processInput()
    #bk3.draw() 
game.wait(K_SPACE)
game.quit()

