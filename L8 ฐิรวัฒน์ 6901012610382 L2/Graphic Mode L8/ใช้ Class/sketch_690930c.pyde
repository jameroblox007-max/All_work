class Balloon:
    def __init__(self, x, y, r, c, speed):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.speed = speed

    def show(self):
        stroke(100)
        strokeWeight(2)
        line(self.x, self.y + self.r, self.x, self.y + self.r + 40)

        noStroke()
        fill(self.c)
        ellipse(self.x, self.y, self.r * 2, self.r * 2.4)

        triangle(self.x - 5, self.y + self.r + 2, self.x + 5, self.y + self.r + 2, self.x, self.y + self.r - 3)

        fill(255, 255, 255, 150)
        ellipse(self.x - self.r * 0.3, self.y - self.r * 0.3, self.r * 0.4, self.r * 0.5)

    def update(self):

        self.y -= self.speed

        if self.y < -self.r * 2:
            self.y = height + self.r * 2

balloons = []

def setup():
    size(500, 500)

    balloons.append(Balloon(100, 450, 30, color(255, 100, 100), 2.0))
    balloons.append(Balloon(180, 500, 40, color(100, 200, 255), 1.5))
    balloons.append(Balloon(250, 420, 25, color(255, 200, 100), 2.5))
    balloons.append(Balloon(320, 480, 35, color(150, 255, 150), 1.8))
    balloons.append(Balloon(390, 520, 45, color(200, 100, 255), 1.2))

def draw():
    background(230, 240, 255)  
    

    for b in balloons:
        b.show()
        b.update()
