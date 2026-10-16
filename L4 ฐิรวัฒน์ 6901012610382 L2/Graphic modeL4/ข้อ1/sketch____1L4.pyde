def setup():
    size(600, 400)

def draw_balloon(x, y, r):
    fill(255, 100, 100)
    ellipse(x, y, r, r * 1.2)
    stroke(0)
    line(x, y + r * 0.6, x, y + r * 0.6 + 40)

def cal_distance(x1, y1, x2, y2):
    diffx = abs(x1 - x2)
    diffy = abs(y1 - y2)
    result = sqrt(diffx * diffx + diffy * diffy)
    return result

def draw():
    background(255)
    x = 300
    y = 200 + sin(frameCount * 0.05) * 20  # ลอยขึ้นลงเล่นๆ

    draw_balloon(x, y, 50)
    d = cal_distance(x, y, mouseX, mouseY)

    stroke(0, 150, 255)
    if mouseX > x:
        line(x, y, x + d, y)
    else:
        line(x, y, x - d, y)

    fill(0)
    noStroke()
    text("distance: " + str(int(d)), 10, 20)
