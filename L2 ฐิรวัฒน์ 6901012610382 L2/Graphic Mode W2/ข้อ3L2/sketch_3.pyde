x = 0  

def setup():
    size(600, 300)

def draw():
    global x
    background(255) 

    stroke(0) 
    noFill()  

    line(x, 150, x + 200, 150)   
    line(x, 200, x + 200, 200)    
    line(x, 150, x, 200)         
    line(x + 200, 150, x + 200, 200) 

    line(x + 60, 100, x + 140, 100) 
    line(x + 60, 100, x + 60, 150)
    line(x + 140, 100, x + 160, 150)

    ellipse(x + 50, 200, 40, 40) 
    ellipse(x + 150, 200, 40, 40)

    x = x + 2

    if x > width:
        x = -210
