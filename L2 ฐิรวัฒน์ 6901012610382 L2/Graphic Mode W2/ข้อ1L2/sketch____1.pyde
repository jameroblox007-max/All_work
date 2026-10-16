balloon_x = 200
balloon_y = 500

def setup():
    size(400, 600)

def draw():
    global balloon_y
    background(135, 206, 235)

    draw_balloon(balloon_x, balloon_y)

    balloon_y = update_balloon_position(balloon_y)

def draw_balloon(x, y):

    stroke(0)
    line(x, y + 10, x, y + 100)

    noStroke()
    fill(255, 50, 50)
    ellipse(x, y, 60, 70)

def update_balloon_position(y):

    y -= 2

    if y < -50:
        y = height + 50
    return y
