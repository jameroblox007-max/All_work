balloons = [
    [100, 450, 30, 255, 100, 100, 2.0],
    [180, 500, 40, 100, 200, 255, 1.5],
    [250, 420, 25, 255, 200, 100, 2.5],
    [320, 480, 35, 150, 255, 150, 1.8],
    [390, 520, 45, 200, 100, 255, 1.2]
]

def setup():
    size(500, 500)

def draw():
    background(230, 240, 255)  
    for b in balloons:
        draw_balloon(b[0], b[1], b[2], color(b[3], b[4], b[5]))
        
        b[1] -= b[6]

        if b[1] < -b[2] * 2:
            b[1] = height + b[2] * 2

def draw_balloon(x, y, r, c):
    stroke(100)
    strokeWeight(2)
    line(x, y + r, x, y + r + 40)
    
    noStroke()
    fill(c)
    ellipse(x, y, r * 2, r * 2.4)
    
    triangle(x - 5, y + r + 2, x + 5, y + r + 2, x, y + r - 3)

    fill(255, 255, 255, 150)
    ellipse(x - r * 0.3, y - r * 0.3, r * 0.4, r * 0.5)
