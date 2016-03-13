from graphics import*
from button import Button
from math import*
from time import*
import winsound
from random import*
class Ball:
    def __init__(self, wVal, xVal, yVal):
        self.w = wVal # window object
        self.x = xVal # (x,y) the centre of the card
        self.y = yVal
        self.f = Image(Point(xVal,yVal),"ball.gif")
    def undraw(self):
        self.f.undraw()
    def draw(self):
        self.f.draw(self.w)
    def move2Ball(self,a,b):
        dx=a-self.x
        dy=b-self.y
        self.f.move(dx,dy)
def setBackground(bac):
    Image(Point(600,450),"ground.gif").draw(bac)
    Image(Point(1100,600),"loops.gif").draw(bac)
    Image(Point(700,250),"audience.gif").draw(bac)
    Image(Point(150,300),"shoot.gif").draw(bac)
def setCircle(cir):
    c=Circle(Point(300,500),140)
    c.setOutline('red')
    c.setWidth(40)
    c.draw(cir)
    b=Circle(Point(300,500),100)
    b.setOutline('yellow')
    b.setWidth(40)
    b.draw(cir)
    a=Circle(Point(300,500),60)
    a.setOutline('blue')
    a.setWidth(40)
    a.draw(cir)
def setLine(lin):
    line1=Line(Point(300,500),Point(300,660))
    line1.setFill('grey')
    line1.setWidth(5)
    line1.setArrow("last")
    line1.draw(lin)
    line2=Line(Point(300,500),Point(460,500))
    line2.setFill('grey')
    line2.setWidth(5)
    line2.setArrow("last")
    line2.draw(lin)
def effect1(tex1):
    o=Text(Point(600,600),"NICE SHOOT!!!")
    o.setSize(30)
    o.setFill("purple")
    o.draw(tex1)
    soundfile="344.wav"
    winsound.PlaySound(soundfile,winsound.SND_FILENAME) #add music effects
    o.undraw()
def effect2(tex2):
    p=Text(Point(600,600),"FAIL...")
    p.setSize(30)
    p.setFill("green")
    p.draw(tex2)
    soundfile="2.wav"
    winsound.PlaySound(soundfile,winsound.SND_FILENAME) #add music effects
    p.undraw()

def main():
    win=GraphWin("Basketball",1200,900)
    win.setCoords(1200,0,0,900)
    setBackground(win)  #set background
    setCircle(win)      #set circle
    setLine(win)        #set line
    rButton = Button(win,Point(900,850),140,60,"Restart")
    qButton = Button(win,Point(400,850),140,60,"Quit")
    rButton.activate()
    qButton.activate()
 
    ball0=Ball(win,300,500)
    ball0.draw()
    ball_list=[0,0,0,0]
    for j in range(4):
        ball_list[j] = Ball(win,100,(850-j*100))
        ball_list[j].draw()
    i=-1
    score=0 
    while True:
        q=win.getMouse()
        if qButton.clicked(q):
            break
        if rButton.clicked(q):
            ball0=Ball(win,300,500)
            ball0.draw()
            ball_list=[0,0,0,0]
            for j in range(4):
                ball_list[j] = Ball(win,100,(850-j*100))
                ball_list[j].draw()
                i=-1
                score=0
        
        x=float(q.getX())
        y=float(q.getY())
        if 300.0<x<500.0 and 500.0<y<700.0 and 0<((x-300)*(x-300)+(y-500)*(y-500))<=25600:
            w=(x-300)*(x-300)+(y-500)*(y-500)
            bsin=float(y-500)/sqrt(w)
            bcos=float(x-300)/sqrt(w)
            t=0
            if 14400<((x-300)*(x-300)+(y-500)*(y-500))<=25600:
                v0=uniform(95,105)
            if 6400<((x-300)*(x-300)+(y-500)*(y-500))<=14400:
                v0=uniform(85,95)
            if 0<((x-300)*(x-300)+(y-500)*(y-500))<=6400:
                v0=uniform(75,85)
            if i==-1:
                while ball0.x<=1030 and ball0.y>=500:
                    t=t+1
                    a=300+v0*bcos*t
                    b=500+v0*bsin*t-5.0*t*t
                    ball0.f.move(v0*bcos*1,(v0*bsin-10.0*t+5.0))
                    ball0.x=a
                    ball0.y=b
                    sleep(0.1)
                if 1020<a<1100 and 500<b<650:
                    score=score+3
                    effect1(win)
                else:
                    score=score+0
                    effect2(win)
                ball0.undraw()
                i=i+1
                ball_list[i].move2Ball(300,500)
                continue
            if i>=0 and i<=3:
                a=ball_list[i].x
                b=ball_list[i].y
                while a<=1030 and b>=500:
                    t=t+1
                    a=300+v0*bcos*t
                    b=500+v0*bsin*t-5.0*t*t
                    ball_list[i].f.move(v0*bcos*1,(v0*bsin-10.0*t+5.0))
                    sleep(0.1)
                if 1020<a<1100 and 500<b<650:
                    score=score+3
                    effect1(win)
                else:
                    score=score+0
                    effect2(win)
                ball_list[i].undraw()
                if i<3:
                    i=i+1
                    ball_list[i].move2Ball(300,500)
                    continue
                else:
                    q=Text(Point(600,600),"Your final score is %-4d"%(score))
                    q.setFill("white")
                    q.setSize(35)
                    q.draw(win)
                    sleep(1.5)
                    q.undraw()
                    print "your final score is",score
                    continue
                
            
    win.close()
main()

    
