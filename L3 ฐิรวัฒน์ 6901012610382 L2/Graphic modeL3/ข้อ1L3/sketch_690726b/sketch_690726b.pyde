x = 200

def setup():
    size(400, 400) 

def draw():
    background(255) 
    draw_balloon(x, 200, 50)

    d = cal_distance(x, 200, mouseX, mouseY)

    if mouseX > x:
        line(x, 200, x + d, 200)
    else:
        line(x, 200, x - d, 200)

def draw_balloon(bx, by, r):
    fill(255, 100, 100)
    circle(bx, by, r) 

def cal_distance(x1, y1, x2, y2):
    return dist(x1, y1, x2, y2) 
