def setup():
    size(700, 250)
    background(155,0,0)

    i = 0

    while i < 5:
        x = 110 + i * 115
        draw_positive(x, 125)
        i += 1


def draw_positive(x, y):
    stroke(0)
    strokeWeight(5)
    noFill()

    rect(x - 15, y - 60, 30, 120)

    rect(x - 45, y - 30, 90, 30)
