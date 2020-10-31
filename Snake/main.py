import pygame, math, random

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption('Snake')

score = 0

x, y = 320,320
dx,dy = 32,32
running = True
dirUp, dirDown = False, False
dirLeft, dirRight = False, True
body = [(x,y)]
pos = []

squares = [i for i in range(640) if i % 32 == 0]
food = pygame.image.load('/Users/mikolajszczerbetka/Desktop/Python_projects/Snake/fruit.png')
food = pygame.transform.scale(food, (32,32))
foodx,foody = random.choice(squares), random.choice(squares)

def isCollision(obsX, obsY, x, y):
    return math.sqrt(math.pow(obsX - x, 2) + math.pow(obsY - y, 2)) <= 0

def show_text():
    score_font = pygame.font.Font('freesansbold.ttf',32)
    score_text = score_font.render('Score: {}'.format(score), True, (255,255,255))
    screen.blit(score_text, (0,0))

def move(x, y):
    if dirUp:
        y -= dy
    elif dirDown:
        y += dy
    elif dirRight:
        x += dx
    elif dirLeft:
        x -= dx
    return x, y

clock = pygame.time.Clock()

while running:
    clock.tick(10)
    screen.fill((0,128,0))

    if body[0][0] > 608 or body[0][0] < 0:
        running = False
    elif body[0][1] > 608 or body[0][1] < 0:
        running = False

    snakeImg = [pygame.transform.scale(pygame.image.load('/Users/mikolajszczerbetka/Desktop/Python_projects/Snake/snakeblock.png'), (32,32)) for i in range(len(body))]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not dirDown:
                dirUp = True
                dirLeft = dirDown = dirRight = False
            if event.key == pygame.K_DOWN and not dirUp:
                dirDown = True
                dirUp = dirLeft = dirRight = False
            if event.key == pygame.K_RIGHT and not dirLeft:
                dirRight = True
                dirUp = dirDown = dirLeft = False
            if event.key == pygame.K_LEFT and not dirRight:
                dirLeft = True
                dirUp = dirDown = dirRight = False
    for i in reversed(range(len(body))):
        if isCollision(foodx,foody,body[i][0],body[i][1]):
            foodx, foody = random.choice(squares), random.choice(squares)
            score += 1
            body.insert(0, move(body[i][0], body[i][1]))
        elif i == 0:

            body[i] = move(body[i][0], body[i][1])
        else:

            body[i] = body[i - 1]

        screen.blit(food, (foodx, foody))
        screen.blit(snakeImg[i], (body[i][0], body[i][1]))

    for i in range(len(body)):
        if body[0] in body[1:]:
            running = False

    show_text()
    pygame.display.update()
pygame.quit()
