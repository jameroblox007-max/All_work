letterWidth = 40
letterHeight = 80
gap = 20
strokeW = 4

def setup():
    size(800, 800)
    background(255)
    strokeWeight(strokeW)
    stroke(0)
    
    drawWord("LINE", 50, 50, letterWidth, letterHeight, gap)
    drawWord("INN", 50, 150, letterWidth, letterHeight, gap)
    drawWord("NILE", 50, 250, letterWidth, letterHeight, gap)
    drawWord("EIN", 50, 350, letterWidth, letterHeight, gap)
    drawWord("LININ", 50, 450, letterWidth, letterHeight, gap)
    drawWord("NEIL", 50, 550, letterWidth, letterHeight, gap)
    
def draw_L(x, y, w, h):
    line(x, y, x, y + h)
    line(x, y + h, x + w, y + h)


def draw_I(x, y, w, h):
    midX = x + w/2
    line(x, y, x + w, y)
    line(midX, y, midX, y + h)
    line(x, y + h, x + w, y + h)


def draw_N(x, y, w, h):
    line(x, y, x, y + h)
    line(x, y, x + w, y + h)
    line(x + w, y, x + w, y + h)


def draw_E(x, y, w, h):
    midY = y + h/2
    line(x, y, x, y + h)
    line(x, y, x + w, y)
    line(x, midY, x + w * 0.8, midY)
    line(x, y + h, x + w, y + h)


def drawWord(word, startX, startY, w, h, g):
    currentX = startX
    for ch in word:
        if ch == 'L':
            draw_L(currentX, startY, w, h)
        elif ch == 'I':
            draw_I(currentX, startY, w, h)
        elif ch == 'N':
            draw_N(currentX, startY, w, h)
        elif ch == 'E':
            draw_E(currentX, startY, w, h)
        currentX += w + g
