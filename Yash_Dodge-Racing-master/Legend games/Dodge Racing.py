#Yash Patel
#Game Name: Dodge Racing
#Game Company:Legend Games

from gamelib import *

game = Game(400,700,"Dodge racing")

road = Image("road.png",game)
road.resizeTo(400,800)
game.setBackground(road)
game.drawBackground()


car = Image("car.png",game)
car.resizeBy(-95)
car.moveTo(200,550)

police = Image("police.png",game)
police.resizeBy(-88)
x = randint(20,380)
y = game.height - randint(500,2000)
s = randint(5,15)
police.moveTo(x,y)
police.setSpeed(s,180)

car2 = Image("car2.png",game)
car2.resizeBy(-95)
x = randint(20,380)
y = game.height - randint(500,2500)
s = randint(10,15)
car2.moveTo(x,y)
car2.setSpeed(s,180)

wood = Image("wood.png",game)
wood.resizeBy(-78)
x = randint(20,380)
y = game.height - randint(500,3000)
s = randint(10,15)
wood.moveTo(x,y)
wood.setSpeed(s,180)

cone = Image("cone.png",game)
cone.resizeBy(-80)
x = randint(20,380)
y = game.height - randint(500,3000)
s = randint(10,15)
cone.moveTo(x,y)
cone.setSpeed(s,180)

blocker = Image("blocker.png",game)
blocker.resizeBy(-70)
x = randint(20,380)
y = game.height - randint(500,2500)
s = randint(10,15)
blocker.moveTo(x,y)
blocker.setSpeed(s,180)

mileStone = Image("mileStone.png",game)
mileStone.resizeBy(-70)
x = randint(20,380)
y = game.height - randint(500,3200)
s = randint(10,15)
mileStone.moveTo(x,y)
mileStone.setSpeed(s,180)

diamond = Image("diamond.png",game)
diamond.resizeBy(-82)
x = randint(20,380)
y = game.height - randint(500,4000)
s = randint(10,15)
diamond.moveTo(x,y)
diamond.setSpeed(s,180)

sock = Image("sock.png",game)
sock.resizeBy(-82)
x = randint(20,380)
y = game.height - randint(500,4000)
s = randint(10,15)
sock.moveTo(x,y)
sock.setSpeed(s,180)

tank = Image("tank.png",game)
tank.resizeBy(-88)
x = randint(20,380)
y = game.height - randint(1000,4200)
s = randint(8,15)
tank.moveTo(x,y)
tank.setSpeed(s,180)

cars4 = Image("4cars.png",game)
cars4.resizeBy(-80)
x = randint(20,380)
y = game.height - randint(2500,5000)
s = randint(8,15)
cars4.moveTo(x,y)
cars4.setSpeed(s,180)

cautions = Image("cautions.png",game)
cautions.resizeBy(-80)
x = randint(20,380)
y = game.height - randint(1500,3000)
s = randint(8,15)
cautions.moveTo(x,y)
cautions.setSpeed(s,180)

gems = Image("gems.png",game)
gems.resizeBy(-80)
x = randint(20,380)
y = game.height - randint(2000,3200)
s = randint(8,15)
gems.moveTo(x,y)
gems.setSpeed(s,180)

trap = Image("trap.png",game)
trap.resizeBy(-80)
x = randint(20,380)
y = game.height - randint(1700,3000)
s = randint(8,15)
trap.moveTo(x,y)
trap.setSpeed(s,180)

game.drawText("Dodge Racing",game.width/5-65,game.height/4-50,Font(blue,80,red))
game.drawText("By: LEGEND GAMES",game.width/5+30,game.height/4+10,Font(red,30,black))
game.drawText("Press [SPACE] to begin",game.width/5-45,game.height/4+250,Font(green,40,blue))
game.drawText("Shoot the cars and collect the diamond",game.width/5-70,game.height/4+50,Font(blue,30))
game.drawText("Dodge the cautions",game.width/5+20,game.height/4+80,Font(red,30))
game.drawText("Arrow keys to move",game.width/5+20,game.height/4+120,Font(blue,30))
game.drawText("[SPACE] to shoot",game.width/5+20,game.height/4+140,Font(blue,30))

game.update()
game.wait(K_SPACE)

fireball = Image("fireball.png",game)
fireball.resizeBy(-93)
fireball.visible = False

ruin = Image("ruin.png",game)

while not game.over:
    game.processInput()
    game.scrollBackground("down",10)
    car.move()
    police.move()
    car2.move()
    wood.move()
    cone.move()
    blocker.move()
    mileStone.move()
    diamond.move()
    sock.move()
    tank.move()
    cars4.move()
    cautions.move()
    gems.move()
    trap.move()
    fireball.move()
            
    if keys.Pressed[K_LEFT]:
        car.rotateBy(5,"left")
        
    if keys.Pressed[K_RIGHT]:
        car.rotateBy(5,"right")

    if keys.Pressed[K_UP]:
        car.forward(5)

    if keys.Pressed[K_DOWN]:
        car.moveY(+15)

    if keys.Pressed[K_SPACE]:
        fireball.visible = True
        fireball.moveTo(car.x,car.y)
        fireball.setSpeed(40,car.getAngle())

    if fireball.collidedWith(police):
        police.visible = False
        ruin.move()
        game.score+=1

    if car.collidedWith(police):
        car.health-=10

    if fireball.collidedWith(car2):
        car2.visible = False
        ruin.move()
        game.score+=1


    if car.collidedWith(car2):
        car.health-=10

    if car.collidedWith(wood):
        car.health-=10
        
    if car.collidedWith(cone):
        car.health-=10

    if car.collidedWith(blocker):
        car.health-=10

    if car.collidedWith(mileStone):
        car.health-=10

    if car.collidedWith(diamond):
        diamond.visible = False
        ruin.visible = True
        game.score+=5

    if car.collidedWith(sock):
        car.health-=10

    if fireball.collidedWith(tank):
        tank.visible = False
        ruin.visible = True
        game.score+=5

    if fireball.collidedWith(cars4):
        cars4.visible = False
        ruin.visible = True
        game.score+=7

    if car.collidedWith(cautions):
        car.health-=10

    if car.collidedWith(cars4):
        car.health-=10

    if car.collidedWith(gems):
        gems.visible = False
        game.score+=10

    if car.collidedWith(trap):
        car.health-=10

    if car.health<=0:
        game.over = True

    if game.score>=20:
        game.over = True
        game.drawText("You WIN",game.width/3-40,game.height/3,Font(red,90,black))
        game.drawText("Press [ESC] to Exit",game.width/3-40,game.height-80,Font(blue,40,black))
        game.update()
        game.wait(K_ESCAPE)
        game.quit()
        
    game.drawText("Health: " + str(car.health),5,5)
    game.drawText("Score: " + str (game.score),300,5)

    game.update(8)

game.drawText("The End",game.width/3-40,game.height/3,Font(red,90,black))
game.drawText("Press [ESC] to Exit",game.width/3-40,game.height-80,Font(blue,40,black))
game.update()
game.wait(K_ESCAPE)
game.quit()


game.quit()


