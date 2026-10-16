def setup():
    size(1280,720)
    rectMode(CENTER)
    noFill()
    strokeWeight(2)

def draw():
    background(0)

    if mousePressed:

        if mouseX < width / 2:
            stroke(255, 0, 0)   
        else:
            stroke(0, 0, 255)  
    else:
        stroke(255)           

    draw_positive(mouseX, mouseY, 15)

def draw_square(x, y, size):
    rect(x, y, size, size)

def draw_positive(x, y, size):
    draw_square(x, y, size)          
    draw_square(x, y - size, size)   
    draw_square(x, y + size, size)   
    draw_square(x - size, y, size)   
    draw_square(x + size, y, size)  
