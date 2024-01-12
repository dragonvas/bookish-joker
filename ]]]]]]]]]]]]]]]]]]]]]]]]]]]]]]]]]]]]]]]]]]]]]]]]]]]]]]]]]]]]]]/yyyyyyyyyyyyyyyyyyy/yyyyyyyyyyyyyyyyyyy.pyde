popa=70
def setup():
    size(1000,1000)
def draw():
    global popa
    ellipse(500,500,popa,popa)
    if keyPressed:
        background(123,234,0)
        if key == 'a' or key == 'A':
            popa=popa+1
            ellipse(500,500,popa,popa)
        if key == 'q' or key == 'Q':
            popa=popa-1
            ellipse(500,500,popa,popa)
