WIDTH = 400
HEIGHT = 400
SPEED = 1

alien = Actor("alien")
alien.bottomright = 0, 0

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.angle += 1
    if alien.left >= WIDTH:
        alien.right = 0
    if alien.top >= HEIGHT:
        alien.bottom = 0
    alien.left += SPEED
    alien.bottom += SPEED

