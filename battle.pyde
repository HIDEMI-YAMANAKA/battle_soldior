import math
import random
from time import sleep

SOL_N = 900
BATTLE_D =[]
SOLS = []
TURN = 0

def makesol():
    global SOL_N
    global SOLS
    for i in range(0,SOL_N):
        sol = [i,int(130+40*randomGaussian()),1+2*int(i%sqrt(SOL_N)),1+2*int(i/sqrt(SOL_N))]
        SOLS.append(sol)

def movesol(pos):
    global SOL_N
    pos[2] = pos[2] + random.randint(-1,1)
    pos[3] = pos[3] + random.randint(-1,1)
    for i in range(2,4):
        if pos[i] < 0:
            pos[i] = 0
        if pos[i] > 2*int(sqrt(SOL_N)):
            pos[i] = 2*int(sqrt(SOL_N))
    return(pos)

def checkstuck(pos):
    global SOLS
    for sol in SOLS:
        if sol[1] < 1:
            continue
        if pos[0] == sol[0]:
            continue
        if (pos[2] == sol[2]) and (pos[3] == sol[3]):
            (pos,sol) = battle(pos,sol)
            break
    return(pos)

def battle(sol_o,sol_d):
    bp = sol_o[1] - sol_d[1]
    cp  = random.randint(-240,240)
    if cp <= bp:
        sol_d[1] = sol_d[1] - 10
    else:
        sol_o[1] = sol_o[1] - 10
    return(sol_o,sol_d)

def chart(bd):
    for i in range(1,4):
        fill(200)
        rect(0,height-160*i,width,160)
        fill(255)
        rect(5,height-160*i+5,width-10,150)
    for cbd in bd:
        if cbd[0] < 600:
            stroke(255,0,0)
            line(5+cbd[0],height-5,5+cbd[0],height-5-int((cbd[1]+cbd[2]+cbd[3])/6))
            stroke(0,0,255)
            line(5+cbd[0],height-5,5+cbd[0],height-5-int((cbd[2]+cbd[3])/6))
            stroke(0)
            line(5+cbd[0],height-5,5+cbd[0],height-5-int((cbd[3])/6))
            continue
        if cbd[0] < 1200:
            stroke(255,0,0)
            line(5+cbd[0]-600,height-5-160,5+cbd[0]-600,height-5-160-int((cbd[1]+cbd[2]+cbd[3])/6))
            stroke(0,0,255)
            line(5+cbd[0]-600,height-5-160,5+cbd[0]-600,height-5-160-int((cbd[2]+cbd[3])/6))
            stroke(0)
            line(5+cbd[0]-600,height-5-160,5+cbd[0]-600,height-5-160-int((cbd[3])/6))
            continue
        else:
            stroke(255,0,0)
            line(5+cbd[0]-1200,height-5-320,5+cbd[0]-1200,height-5-320-int((cbd[1]+cbd[2]+cbd[3])/6))
            stroke(0,0,255)
            line(5+cbd[0]-1200,height-5-320,5+cbd[0]-1200,height-5-320-int((cbd[2]+cbd[3])/6))
            stroke(0)
            line(5+cbd[0]-1200,height-5-320,5+cbd[0]-1200,height-5-320-int((cbd[3])/6))
    fill(0,255,0)
    textSize(18)
    for i in range(0,3):
        text(150+600*i,5+150,height-5-160*i)
        text(300+600*i,5+300,height-5-160*i)
        text(450+600*i,5+450,height-5-160*i)
        text("300",5,height-5-50-160*i)
        text("600",5,height-5-100-160*i)
        text("900",5,height-5-150-160*i)

def mousePressed():
    if mouseButton == RIGHT:
        loop()

def setup():
    global SOL_N
    size(int(10*(2*sqrt(SOL_N)+2)),int(10*(2*sqrt(SOL_N)+2)))
    
makesol()

def draw():
    global SOL_N
    global SOLS
    global TURN
    #Draw field and sols
    background(100)
    for i in range(0,int(2*sqrt(SOL_N)+2)):
        line(5,5+i*10,10*(2*sqrt(SOL_N)+2)-5,5+i*10)
        line(5+i*10,5,5+i*10,10*(2*sqrt(SOL_N)+2)-5)
    for sol in SOLS:
        if sol[1] < 1:
            continue
        fill(sol[1],0,0)
        rect(5+10*sol[2],5+10*sol[3],10,10)
    #move and check sols
    for sol in SOLS:
        if sol[1] < 1:
            continue
        sol = movesol(sol)
        sol = checkstuck(sol)
    #Display sols in console
    sols = []
    sn = 0
    for sol in SOLS:
        if sol[1] < 1:
            continue
        sols.append(sol)
        sn = sn + 1
    print("TURN:%d"%TURN)
    print(sols)
    #Resize field
    if sn <= 2:
        SOL_N = 25
    elif sn <= 8:
        SOL_N = 100
    elif sn <= 32:
        SOL_N = 400
    # make battle data
    if TURN < 1800:
        hsn = 0
        msn = 0
        lsn = 0
        for sol in SOLS:
            if sol[1] < 1:
                continue
            if sol[1] > 150:
                hsn = hsn + 1
                continue
            if sol[1] > 50:
                msn = msn + 1
                continue
            else:
                lsn = lsn + 1
        bd = [TURN,hsn,msn,lsn]
        BATTLE_D.append(bd)
    #Draw END
    if sn == 1:
        chart(BATTLE_D)
        fill(200)
        rect(width/2-170,height/2+20,340,60)
        fill(255)
        rect(width/2-165,height/2+25,330,50)
        fill(0)
        textSize(36)
        textAlign(CENTER,CENTER)
        text("TURN END:%d"%TURN,width/2,height/2+50)
        noLoop()
    #Draw turn and number of sols when mouse pressed
    if mousePressed and (mouseButton == LEFT):
        fill(200)
        rect(mouseX+15,mouseY-15,185,60)
        fill(255)
        rect(mouseX+20,mouseY-10,175,50)
        fill(0)
        textSize(24)
        text("TURN:%d"%TURN,mouseX+30,mouseY+12)
        text("SOLS = %d"%sn,mouseX+30,mouseY+37)
        noLoop()

    TURN = TURN + 1
