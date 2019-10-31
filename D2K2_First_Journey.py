import pygame
import numpy
from random import *
import os

# print(help(pygame))
'''
https://www.pygame.org

pygame.image.load()
load new image from a file

pygame.image.save()
save an image to disk

pygame.image.get_extended()
test if extended image formats can be loaded

pygame.image.tostring()
transfer image to string buffer

pygame.image.fromstring()
create new Surface from a string buffer

pygame.image.frombuffer()
create a new Surface that shares data inside a string buffer
'''
pygame.init()


class Game:

    def __init__(self, height = 500, width = 500):
        self.height = height
        self.width = width
        self.Window = pygame.display.set_mode((self.width, self.height))

class Player(Game):

    def __init__(self, Window, x = 250, y = 250, height = 60, width = 40):

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.jumping = False
        self.attacking = False
        self.ranged_stance = False
        self.melee_stance = False
        self.fist_stance = False
        self.speed = 6
        self.walkCount = 0
        self.jumpCount = 10
        self.hp_max = 25
        self.hp = 25
        self.temp_hp = 0

        self.hp_box = pygame.draw.rect(Window, (0,0, 200), (15, 15, 50, 20))

        self.hp_gauge = pygame.draw.rect(Window, (200, 0, 0), (15, 15, 50, 20))

        self.hitbox = pygame.draw.rect(Window, (0,0,255), (self.x, self.y, height, width))

        self.avatar = pygame.image.load("/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/colors.jpeg")



    def Player_Update(self, Window):

        self.hp_box = pygame.draw.rect(Window, (0,0, 200), (15, 15, 50, 20))
        self.hp_gauge = pygame.draw.rect(Window, (200,0, 0), (15, 15, 50, 20)),

        self.hitbox = pygame.draw.rect(
            Window,
            (0, 140, 200),
            (self.x, self.y, self.width, self.height)
        )
        Window.blit(self.avatar, (self.x, self.y))





class Monster(Game):

    def __init__(self, x = 250, y = 250, height = 60, width = 40):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.jumping = False
        self.attacking = False
        self.ranged = False
        self.melee = False


class Projectile:

    def __init__(self, x = 50, y = 50, height = 60, width = 40):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False


def main():

    run = True

    game = Game()

    pc = Player(Window = game.Window)

    while run:
        print("run start")
        pygame.time.delay(33)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_LEFT] and pc.x > pc.speed):
            pc.x -= pc.speed
            pc.left = True
            pc.right = False
            pc.standing = False

        elif(keys[pygame.K_RIGHT] and pc.x < 500 - pc.width - pc.speed):
            pc.x += pc.speed
            pc.right = True
            pc.left = False
            pc.standing = False
        else:
            pc.standing = True
            pc.walkCount = 0

        if(keys[pygame.K_SPACE]):

            pc.jumping = True

            if(not pc.jumping):
                if keys[pygame.K_UP]:
                    pc.jumping = True
                    pc.right = False
                    pc.left = False
                    pc.walkCount = 0
            else:
                if(pc.jumpCount >= -10):
                    neg = 1
                    if pc.jumpCount < 0:
                        neg = -1
                    pc.y -= (pc.jumpCount ** 2) * 0.5 * neg
                    pc.jumpCount -= 1
                else:
                    pc.jumping = False
                    pc.jumpCount = 10

        game.Window.fill((0,0,0))

        pc.Player_Update(Window = game.Window)

        pygame.display.update()


    pygame.quit()


main()

'''
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Game")

walkRight = [pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R1.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R2.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R3.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R4.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R5.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R6.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R7.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R8.png'),
             pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R9.png')]
walkLeft = [pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L1.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L2.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L3.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L4.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L5.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L6.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L7.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L8.png'),
            pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L9.png')]
bg = pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/bg.jpg')
char = pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/standing.png')

clock = pygame.time.Clock()

# bulletSound = pygame.mixer.Sound('bullet.wav')
# hitSound = pygame.mixer.Sound('hit.wav')
#
# music = pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)

score = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkLeft = [pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L1E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L2E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L3E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L4E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L5E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L6E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L7E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L8E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L9E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L10E.png'),
                 pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/L11E.png')
                 ]
    walkRight = [pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R1E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R2E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R3E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R4E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R5E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R6E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R7E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R8E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R9E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R10E.png'),
                pygame.image.load('/Users/michaelduffy/Library/Preferences/PyCharmCE2019.1/scratches/Game/R11E.png')
                ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                # hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        # bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
'''