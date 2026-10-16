rocketX = 400
rocketY = 400

speed = 0

flying = False

def setup():
    size(800, 600)
    frameRate(60)


def draw():
    global rocketY, speed, flying

    background(10, 10, 40)

    draw_stars()

    draw_rocket(rocketX, rocketY)

    if flying:
        rocketY -= speed
        speed += 0.05

    if rocketY < -100:
        rocketY = 400
        speed = 0
        flying = False

def draw_rocket(x, y):

    fill(220)
    stroke(255)
    strokeWeight(2)
    ellipse(x, y, 70, 120)

    fill(50, 150, 255)
    ellipse(x, y - 20, 25, 25)

    fill(200, 50, 50)
    line(x - 30, y + 30, x - 50, y + 60)
    line(x - 50, y + 60, x - 25, y + 50)

    line(x + 30, y + 30, x + 50, y + 60)
    line(x + 50, y + 60, x + 25, y + 50)

    draw_fire(x, y + 65)


def draw_fire(x, y):

    fill(255, 150, 0)
    stroke(255, 200, 0)

    ellipse(x, y, 25, 45)

    fill(255, 230, 50)
    ellipse(x, y + 5, 12, 30)

def draw_stars():

    fill(255)
    stroke(255)

    ellipse(80, 100, 5, 5)
    ellipse(180, 200, 5, 5)
    ellipse(300, 80, 5, 5)
    ellipse(500, 150, 5, 5)
    ellipse(700, 100, 5, 5)

    ellipse(120, 400, 5, 5)
    ellipse(250, 500, 5, 5)
    ellipse(550, 400, 5, 5)
    ellipse(680, 500, 5, 5)

def mousePressed():

    global flying, speed

    flying = True
    speed = 3
