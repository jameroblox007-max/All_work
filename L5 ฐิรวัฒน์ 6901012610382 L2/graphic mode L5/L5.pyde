def setup():
    size(800, 300)
    rectMode(CENTER)  

def draw():
    background(200)
    
    count = 5
    spacing = 130
    start_x = 140
    y_pos = height / 2

    i = 0
    while i < count:
        x_pos = start_x + (i * spacing)

        d = dist(mouseX, mouseY, x_pos, y_pos)

        if d < 80:
            size_size = 35  
        else:
            size_size = 25  

        draw_positive(x_pos, y_pos, size_size)
        
        i += 1 

def draw_positive(x, y, s):
    fill(220)
    stroke(0)

    rect(x, y, s, s)

    rect(x, y - s, s, s)

    rect(x, y + s, s, s)

    rect(x - s, y, s, s)

    rect(x + s, y, s, s)
