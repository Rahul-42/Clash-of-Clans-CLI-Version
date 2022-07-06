#from troops import Troop
from src.hut import Can
from src.hut import Wizard
from src.hut import Hut
import time
from src.hut import Th
from src.hut import Walls
from src.input import input_to
from src.King import King
from src.King import Queen
from colorama import Fore, Back, Style
from operator import imod
level = 1
ec = 1

fp = open('replays/replay.txt', 'wt')
fp.write('')
fp.close()

fp = open('replays/replay.txt', 'at')

t0 = time.time()


def initial(level, ec):
    m = 41
    n = 82

    #from turtle import distance
    #from pyrsistent import b
    cannon = []
    wizard = []
    timekeep = []

    if(level == 1):
        defense_count = 2
        cannon.append(Can(13, 7, 400, 25))
        cannon.append(Can(67, 37, 400, 25))
        wizard.append(Wizard(41, 23, 400, 25))
        wizard.append(Wizard(53, 11, 400, 25))
    elif(level == 2):
        defense_count = 3
        cannon.append(Can(13, 7, 400, 25))
        cannon.append(Can(67, 37, 400, 25))
        cannon.append(Can(31, 19, 400, 25))
        wizard.append(Wizard(41, 23, 400, 25))
        wizard.append(Wizard(53, 11, 400, 25))
        wizard.append(Wizard(25, 33, 400, 25))
    elif(level == 3):
        defense_count = 4
        cannon.append(Can(13, 7, 400, 25))
        cannon.append(Can(67, 37, 400, 25))
        cannon.append(Can(31, 19, 400, 25))
        cannon.append(Can(49, 19, 400, 25))
        wizard.append(Wizard(41, 15, 400, 25))
        wizard.append(Wizard(41, 23, 400, 25))
        wizard.append(Wizard(53, 11, 400, 25))
        wizard.append(Wizard(25, 33, 400, 25))

    Barb1 = 0
    Barb2 = 0
    Barb3 = 0
    Arch1 = 0
    Arch2 = 0
    Arch3 = 0
    Ball1 = 0
    Ball2 = 0
    Ball3 = 0

    k = King(3, 1, 400, 30, 2)
    q = Queen(3, 10, 300, 30, 2)

    rows, cols = (41, 82)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    # print(arr)

    barbarian_count = 0
    archer_count = 0
    balloon_count = 0

    class Troop:
        def __init__(self, x, y, health, damage, speed):
            self.x = x
            self.y = y
            self.health = health
            self.damage = damage
            self.speed = speed

        def barbdistance1(self):
            # print("barb[0]: ",self.x,self.y)
            min1 = distance(self.x, self.y, h1.x, h1.y)
            c = [h1.x, h1.y]
            a = h1
            townhall_check = 0
            if(distance(self.x, self.y, h2.x, h2.y) < min1):
                min1 = distance(self.x, self.y, h2.x, h2.y)
                c = [h2.x, h2.y]
                a = h2
            if(distance(self.x, self.y, h3.x, h3.y) < min1):
                min1 = distance(self.x, self.y, h3.x, h3.y)
                c = [h3.x, h3.y]
                a = h3
            if(distance(self.x, self.y, h4.x, h4.y) < min1):
                min1 = distance(self.x, self.y, h4.x, h4.y)
                c = [h4.x, h4.y]
                a = h4
            if(distance(self.x, self.y, h5.x, h5.y) < min1):
                min1 = distance(self.x, self.y, h5.x, h5.y)
                c = [h5.x, h5.y]
                a = h5
            for cannon_index in cannon:
                if(distance(self.x, self.y, cannon_index.x, cannon_index.y) < min1):
                    min1 = distance(
                        self.x, self.y, cannon_index.x, cannon_index.y)
                    c = [cannon_index.x, cannon_index.y]
                    a = cannon_index
            for cannon_index in wizard:
                if(distance(self.x, self.y, cannon_index.x, cannon_index.y) < min1):
                    min1 = distance(
                        self.x, self.y, cannon_index.x, cannon_index.y)
                    c = [cannon_index.x, cannon_index.y]
                    a = cannon_index
            if(distance(self.x, self.y, th1.x, th1.y) < min1):
                min1 = distance(self.x, self.y, th1.x, th1.y)
                c = [th1.x, th1.y]
                a = th1
                townhall_check = 1
            # print(c)
            if(c[0] < self.x and c[1] < self.y):
                if(self.x - c[0] > 2 and self.y - c[1] > 1):
                    if(arr[self.y - self.speed][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - self.speed == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.x-c[0] > 2):
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.y-c[1] > 1):
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] > self.x and c[1] < self.y):
                if(c[0]-self.x > 2 and self.y - c[1] > 1):
                    if(arr[self.y - self.speed][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - self.speed == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(c[0]-self.x > 2):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.y-c[1] > 1):
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] < self.x and c[1] > self.y):
                if(self.x-c[0] > 2 and c[1]-self.y > 1):
                    if(arr[self.y + self.speed][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + self.speed == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.x-c[0] > 2):
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(c[1]-self.y > 1):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] > self.x and c[1] > self.y):
                if(c[0]-self.x > 2 and c[1]-self.y > 1):
                    if(arr[self.y + self.speed][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + self.speed == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(c[0]-self.x > 2):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(c[1]-self.y > 1):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] == self.x):
                if(c[1] > self.y):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                else:
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[1] == self.y):
                if(c[0] > self.x):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                else:
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
            if(townhall_check):
                if(abs(c[0]-self.x) <= 5 and abs(c[1]-self.y) <= 3):
                    a.health = a.health - self.damage
                    townhall_check = 0
            elif(abs(c[0]-self.x) <= 2 and abs(c[1]-self.y) <= 1):
                a.health = a.health - self.damage
            return

    class Archer:
        def __init__(self, x, y, health, damage, speed, range):
            self.x = x
            self.y = y
            self.health = health
            self.damage = damage
            self.speed = speed
            self.range = range

        def archerdistance(self):
            # print("barb[0]: ",self.x,self.y)
            min1 = distance(self.x, self.y, h1.x, h1.y)
            c = [h1.x, h1.y]
            a = h1
            if(distance(self.x, self.y, h2.x, h2.y) < min1):
                min1 = distance(self.x, self.y, h2.x, h2.y)
                c = [h2.x, h2.y]
                a = h2
            if(distance(self.x, self.y, h3.x, h3.y) < min1):
                min1 = distance(self.x, self.y, h3.x, h3.y)
                c = [h3.x, h3.y]
                a = h3
            if(distance(self.x, self.y, h4.x, h4.y) < min1):
                min1 = distance(self.x, self.y, h4.x, h4.y)
                c = [h4.x, h4.y]
                a = h4
            if(distance(self.x, self.y, h5.x, h5.y) < min1):
                min1 = distance(self.x, self.y, h5.x, h5.y)
                c = [h5.x, h5.y]
                a = h5
            for cannon_index in cannon:
                if(distance(self.x, self.y, cannon_index.x, cannon_index.y) < min1):
                    min1 = distance(
                        self.x, self.y, cannon_index.x, cannon_index.y)
                    c = [cannon_index.x, cannon_index.y]
                    a = cannon_index
            for cannon_index in wizard:
                if(distance(self.x, self.y, cannon_index.x, cannon_index.y) < min1):
                    min1 = distance(
                        self.x, self.y, cannon_index.x, cannon_index.y)
                    c = [cannon_index.x, cannon_index.y]
                    a = cannon_index
            if(distance(self.x, self.y, th1.x, th1.y) < min1):
                min1 = distance(self.x, self.y, th1.x, th1.y)
                c = [th1.x, th1.y]
                a = th1
            # print(c)
            if(c[0] < self.x and c[1] < self.y):
                if(self.x - c[0] > 2*self.range and self.y - c[1] > self.range):
                    if(arr[self.y - self.speed][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - 1 == wall_index.y and self.x - 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y - self.speed == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.x-c[0] > 2*self.range):
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.y-c[1] > self.range):
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] > self.x and c[1] < self.y):
                if(c[0]-self.x > 2*self.range and self.y - c[1] > self.range):
                    if(arr[self.y - self.speed][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - 1 == wall_index.y and self.x + 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y - self.speed == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                            # print(wall_index.health)

                elif(c[0]-self.x > 2*self.range):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.y-c[1] > self.range):
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] < self.x and c[1] > self.y):
                if(self.x-c[0] > 2*self.range and c[1]-self.y > self.range):
                    if(arr[self.y + self.speed][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + 1 == wall_index.y and self.x - 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y + self.speed == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.x-c[0] > 2*self.range):
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(c[1]-self.y > self.range):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[0] > self.x and c[1] > self.y):
                if(c[0]-self.x > 2*self.range and c[1]-self.y > self.range):
                    if(arr[self.y + self.speed][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + 1 == wall_index.y and self.x + 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y + self.speed == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage

                elif(c[0]-self.x > 2*self.range):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                            # print(wall_index.health)
                elif(c[1]-self.y > self.range):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                            # print(wall_index.health)
            elif(c[0] == self.x):
                if(c[1] - self.y > self.range):
                    if(arr[self.y + self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y += self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y + 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y + self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.y - c[1] > self.range):
                    if(arr[self.y - self.speed][self.x] == 0):
                        arr[self.y][self.x] = 0
                        self.y -= self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y - 1 == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    # w.pop(wall_index)
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                            elif(self.y - self.speed == wall_index.y and self.x == wall_index.x):
                                wall_index.health -= self.damage
            elif(c[1] == self.y):
                if(c[0] - self.x > 2*self.range):
                    if(arr[self.y][self.x + 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x += 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x + 2 == wall_index.x):
                                wall_index.health -= self.damage
                                # print(wall_index.health)
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y == wall_index.y and self.x + 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
                elif(self.x - c[0] > 2*self.range):
                    if(arr[self.y][self.x - 2*self.speed] == 0):
                        arr[self.y][self.x] = 0
                        self.x -= 2*self.speed
                        arr[self.y][self.x] = 1
                    else:
                        for wall_index in w:
                            if(self.y == wall_index.y and self.x - 2 == wall_index.x):
                                wall_index.health -= self.damage
                                if(wall_index.health <= 0):
                                    arr[self.y][self.x] = 0
                                    arr[wall_index.y][wall_index.x] = 1
                                    self.y = wall_index.y
                                    self.x = wall_index.x
                                    w.pop(wall_index)
                            elif(self.y == wall_index.y and self.x - 2*self.speed == wall_index.x):
                                wall_index.health -= self.damage
            if(abs(c[0]-self.x) <= 2*self.range and abs(c[1]-self.y) <= self.range):
                a.health = a.health - self.damage
            return

    class Balloon:
        def __init__(self, x, y, health, damage, speed):
            self.x = x
            self.y = y
            self.health = health
            self.damage = damage
            self.speed = speed
            #self.range = range

        def move(self):
            cannon_healthcheck = 1
            wizard_healthcheck = 1
            for cannon_index in cannon:
                if(cannon_index.health <= 0):
                    cannon_healthcheck = 1
                else:
                    cannon_healthcheck = 0
                    req_cannon = cannon_index
                    break
            for cannon_index in wizard:
                if(cannon_index.health <= 0):
                    wizard_healthcheck = 1
                else:
                    wizard_healthcheck = 0
                    req_wizard = cannon_index
                    break
            if(cannon_healthcheck == 1 and wizard_healthcheck == 1):
                min1 = distance(self.x, self.y, h1.x, h1.y)
                c = [h1.x, h1.y]
                a = h1
                if(distance(self.x, self.y, h2.x, h2.y) < min1):
                    min1 = distance(self.x, self.y, h2.x, h2.y)
                    c = [h2.x, h2.y]
                    a = h2
                if(distance(self.x, self.y, h3.x, h3.y) < min1):
                    min1 = distance(self.x, self.y, h3.x, h3.y)
                    c = [h3.x, h3.y]
                    a = h3
                if(distance(self.x, self.y, h4.x, h4.y) < min1):
                    min1 = distance(self.x, self.y, h4.x, h4.y)
                    c = [h4.x, h4.y]
                    a = h4
                if(distance(self.x, self.y, h5.x, h5.y) < min1):
                    min1 = distance(self.x, self.y, h5.x, h5.y)
                    c = [h5.x, h5.y]
                    a = h5
                if(distance(self.x, self.y, th1.x, th1.y) < min1):
                    min1 = distance(self.x, self.y, th1.x, th1.y)
                    c = [th1.x, th1.y]
                    a = th1
                #call(c, a)
            elif(wizard_healthcheck == 1):
                min = distance(self.x, self.y, req_cannon.x, req_cannon.y)
                for i in cannon:
                    if(i.health > 0 and distance(self.x, self.y, i.x, i.y) <= min):
                        c = [i.x, i.y]
                        a = i
            elif(cannon_healthcheck == 1):
                min = distance(self.x, self.y, req_wizard.x, req_wizard.y)
                for i in wizard:
                    if(i.health > 0 and distance(self.x, self.y, i.x, i.y) <= min):
                        c = [i.x, i.y]
                        a = i
            else:
                min = distance(self.x, self.y, req_cannon.x, req_cannon.y)
                for i in cannon:
                    if(i.health > 0 and distance(self.x, self.y, i.x, i.y) <= min):
                        c = [i.x, i.y]
                        a = i
                for i in wizard:
                    if(i.health > 0 and distance(self.x, self.y, i.x, i.y) <= min):
                        c = [i.x, i.y]
                        a = i
                #call(c, a)
            if(c[0] < self.x and c[1] < self.y):
                if(self.x - c[0] > 2*self.speed and self.y - c[1] > self.speed):
                    self.x -= 2*self.speed
                    self.y -= self.speed

                elif(self.x - c[0] > 2*self.speed):
                    self.x -= 2*self.speed

                elif(self.y-c[1] > self.speed):

                    self.y -= self.speed

            elif(c[0] > self.x and c[1] < self.y):
                if(c[0]-self.x > 2*self.speed and self.y - c[1] > self.speed):
                    self.x += 2*self.speed
                    self.y -= self.speed

                elif(c[0]-self.x > 2*self.speed):
                    self.x += 2*self.speed

                elif(self.y-c[1] > self.speed):

                    self.y -= self.speed

            elif(c[0] < self.x and c[1] > self.y):
                if(self.x-c[0] > 2*self.speed and c[1]-self.y > self.speed):
                    self.x -= 2*self.speed
                    self.y += self.speed

                elif(self.x-c[0] > 2*self.speed):

                    self.x -= 2*self.speed

                elif(c[1]-self.y > self.speed):

                    self.y += self.speed

            elif(c[0] > self.x and c[1] > self.y):
                if(c[0]-self.x > 2*self.speed and c[1]-self.y > self.speed):

                    self.x += 2*self.speed
                    self.y += self.speed

                elif(c[0]-self.x > 2*self.speed):

                    self.x += 2*self.speed

                elif(c[1]-self.y > self.speed):

                    self.y += self.speed

            elif(c[0] == self.x):
                if(c[1] > self.y):

                    self.y += self.speed

                else:

                    self.y -= self.speed

            elif(c[1] == self.y):
                if(c[0] > self.x):

                    self.x += 2*self.speed

                else:

                    self.x -= 2*self.speed

            if(abs(c[0]-self.x) <= 2*self.speed and abs(c[1]-self.y) <= self.speed):
                a.health = a.health - self.damage
            return

    hut1 = [7, 3]
    hut2 = [9, 3]
    hut3 = [73, 3]
    hut4 = [7, 37]
    hut5 = [73, 37]
    h1 = Hut(7, 3, 100)
    h2 = Hut(9, 3, 100)
    h3 = Hut(73, 3, 100)
    h4 = Hut(7, 37, 100)
    h5 = Hut(73, 37, 100)
    th1 = Th(40, 20, 500)
    #b1 = Troop(3, 39, 200, 20, 1)
    #b2 = Troop(65, 33, 200, 20, 1)
    #b3 = Troop(39, 3, 200, 20, 1)
    b = []
    w = []
    archer = []
    balloon = []
    j = 35
    while j < 46:
        w.append(Walls(j, 17, 300))
        w.append(Walls(j, 21, 300))
        j += 2
    i = 18
    while i < 21:
        w.append(Walls(35, i, 300))
        w.append(Walls(45, i, 300))
        i += 1

    wall_health = 0

    # b.append(b1)
    # b.append(b2)
    # b.append(b3)

    def attack():
        if(k.health > 0):
            if((abs(k.x - th1.x) <= 13) and (abs(k.y - th1.y) <= 6) and (th1.health > 0)):
                th1.health -= k.damage
            for i in cannon:
                if(abs(i.x - k.x) <= 10 and abs(k.y - i.y) <= 5 and (i.health > 0)):
                    i.health -= k.damage
            for i in wizard:
                if(abs(i.x - k.x) <= 10 and abs(k.y - i.y) <= 5 and (i.health > 0)):
                    i.health -= k.damage
            if(abs(h1.x - k.x) <= 10 and abs(k.y - h1.y) <= 5 and (h1.health > 0)):
                h1.health = h1.health - k.damage
            if(abs(h2.x - k.x) <= 10 and abs(k.y - h2.y) <= 5 and (h2.health > 0)):
                h2.health = h2.health - k.damage
            if(abs(h3.x - k.x) <= 10 and abs(k.y - h3.y) <= 5 and (h3.health > 0)):
                h3.health = h3.health - k.damage
            if(abs(h4.x - k.x) <= 10 and abs(k.y - h4.y) <= 5 and (h4.health > 0)):
                h4.health = h4.health - k.damage
            if(abs(h5.x - k.x) <= 10 and abs(k.y - h5.y) <= 5 and (h5.health > 0)):
                h5.health = h5.health - k.damage
            for i in w:
                if(abs(i.x - k.x) <= 10 and abs(k.y - i.y) <= 5 and (i.health > 0)):
                    i.health = i.health - k.damage

    def attack_queen():
        fx = 0
        fy = 0
        if(q.health > 0):
            if(latest[-1] == "w"):
                if(q.y >= 8):
                    fy = q.y - 8
                    fx = q.x
                else:
                    fy = 0
                    fx = q.x
            elif(latest[-1] == "s"):
                if(q.y <= 31):
                    fy = q.y + 8
                    fx = q.x
                else:
                    fy = 39
                    fx = q.x
            elif(latest[-1] == "a"):
                if(q.x >= 16):
                    fx = q.x - 16
                    fy = q.y
                else:
                    fx = 0
                    fy = q.y
            elif(latest[-1] == "d"):
                if(q.x <= 71):
                    fx = q.x + 16
                    fy = q.y
                else:
                    fx = 79
                    fy = q.y
            if((abs(fx - th1.x) <= 4) and (abs(fy - th1.y) <= 2) and (th1.health > 0)):
                th1.health -= q.damage
            for i in cannon:
                if(abs(i.x - fx) <= 4 and abs(fy - i.y) <= 2 and (i.health > 0)):
                    i.health -= q.damage
            for i in wizard:
                if(abs(i.x - fx) <= 4 and abs(fy - i.y) <= 2 and (i.health > 0)):
                    i.health -= q.damage
            if(abs(h1.x - fx) <= 4 and abs(fy - h1.y) <= 2 and (h1.health > 0)):
                h1.health = h1.health - q.damage
            if(abs(h2.x - fx) <= 4 and abs(fy - h2.y) <= 2 and (h2.health > 0)):
                h2.health = h2.health - q.damage
            if(abs(h3.x - fx) <= 4 and abs(fy - h3.y) <= 2 and (h3.health > 0)):
                h3.health = h3.health - q.damage
            if(abs(h4.x - fx) <= 4 and abs(fy - h4.y) <= 2 and (h4.health > 0)):
                h4.health = h4.health - q.damage
            if(abs(h5.x - fx) <= 4 and abs(fy - h5.y) <= 2 and (h5.health > 0)):
                h5.health = h5.health - q.damage
            for i in w:
                if(abs(i.x - fx) <= 4 and abs(fy - i.y) <= 2 and (i.health > 0)):
                    i.health = i.health - q.damage

    def specialattack():
        fx = 0
        fy = 0
        if(q.health > 0):
            if(latest[-1] == "w"):
                if(q.y >= 16):
                    fy = q.y - 16
                    fx = q.x
                else:
                    fy = 0
                    fx = q.x
            elif(latest[-1] == "s"):
                if(q.y <= 23):
                    fy = q.y + 16
                    fx = q.x
                else:
                    fy = 39
                    fx = q.x
            elif(latest[-1] == "a"):
                if(q.x >= 32):
                    fx = q.x - 32
                    fy = q.y
                else:
                    fx = 0
                    fy = q.y
            elif(latest[-1] == "d"):
                if(q.x <= 63):
                    fx = q.x + 32
                    fy = q.y
                else:
                    fx = 79
                    fy = q.y
            if((abs(fx - th1.x) <= 8) and (abs(fy - th1.y) <= 4) and (th1.health > 0)):
                th1.health -= q.damage
            for i in cannon:
                if(abs(i.x - fx) <= 8 and abs(fy - i.y) <= 4 and (i.health > 0)):
                    i.health -= q.damage
            for i in wizard:
                if(abs(i.x - fx) <= 8 and abs(fy - i.y) <= 4 and (i.health > 0)):
                    i.health -= q.damage
            if(abs(h1.x - fx) <= 8 and abs(fy - h1.y) <= 4 and (h1.health > 0)):
                h1.health = h1.health - q.damage
            if(abs(h2.x - fx) <= 8 and abs(fy - h2.y) <= 4 and (h2.health > 0)):
                h2.health = h2.health - q.damage
            if(abs(h3.x - fx) <= 8 and abs(fy - h3.y) <= 4 and (h3.health > 0)):
                h3.health = h3.health - q.damage
            if(abs(h4.x - fx) <= 8 and abs(fy - h4.y) <= 4 and (h4.health > 0)):
                h4.health = h4.health - q.damage
            if(abs(h5.x - fx) <= 8 and abs(fy - h5.y) <= 4 and (h5.health > 0)):
                h5.health = h5.health - q.damage
            for i in w:
                if(abs(i.x - fx) <= 8 and abs(fy - i.y) <= 4 and (i.health > 0)):
                    i.health = i.health - q.damage

    def defense():
        cannon_check = 0
        wizard_check = 0
        use = k
        for i in cannon:
            if(choice == "k"):
                if((abs(k.x - i.x) <= 10) and (abs(k.y - i.y) <= 5) and (k.health > 0)):
                    k.health = k.health - i.damage
                    cannon_check = 1
            elif(choice == "q"):
                if((abs(q.x - i.x) <= 10) and (abs(q.y - i.y) <= 5) and (q.health > 0)):
                    q.health = q.health - i.damage
                    cannon_check = 1
        for i in wizard:
            if(choice == "k"):
                use = k
            elif(choice == "q"):
                use = q
            if((abs(use.x - i.x) <= 10) and (abs(use.y - i.y) <= 5) and (use.health > 0)):
                use.health = use.health - i.damage
                wizard_check = 1
                for j in b:
                    if(abs(j.x - use.x) <= 2 and abs(j.y - use.y) <= 1 and (j.health > 0)):
                        j.health = j.health - i.damage
                for j in archer:
                    if(abs(j.x - use.x) <= 2 and abs(j.y - use.y) <= 1 and (j.health > 0)):
                        j.health = j.health - i.damage
                for j in balloon:
                    if(abs(j.x - use.x) <= 2 and abs(j.y - use.y) <= 1 and (j.health > 0)):
                        j.health = j.health - i.damage
        if(cannon_check == 0):
            barbarian_index = 0
            cannon_zeroes = [0]*len(cannon)
            for barbarian_index in range(barbarian_count):
                for index in range(len(cannon)):
                    if((abs(b[barbarian_index].x - cannon[index].x) <= 10) and (abs(b[barbarian_index].y - cannon[index].y) <= 5) and (b[barbarian_index].health > 0) and (cannon_zeroes[index] == 0)):
                        b[barbarian_index].health = b[barbarian_index].health - \
                            cannon[index].damage
                        cannon_zeroes[index] = 1
            for barbarian_index in archer:
                for index in range(len(cannon)):
                    if((abs(barbarian_index.x - cannon[index].x) <= 10) and (abs(barbarian_index.y - cannon[index].y) <= 5) and (barbarian_index.health > 0) and (cannon_zeroes[index] == 0)):
                        barbarian_index.health = barbarian_index.health - \
                            cannon[index].damage
                        cannon_zeroes[index] = 1
        if(wizard_check == 0):
            barbarian_index = 0
            wizard_zeroes = [0]*len(wizard)
            for barbarian_index in range(barbarian_count):
                for index in range(len(wizard)):
                    if((abs(b[barbarian_index].x - wizard[index].x) <= 10) and (abs(b[barbarian_index].y - wizard[index].y) <= 5) and (b[barbarian_index].health > 0) and (wizard_zeroes[index] == 0)):
                        b[barbarian_index].health = b[barbarian_index].health - \
                            wizard[index].damage
                        wizard_zeroes[index] = 1
                        for j in b:
                            if(abs(j.x - b[barbarian_index].x) <= 2 and abs(j.y - b[barbarian_index].y) <= 1 and (j.health > 0) and j != b[barbarian_index]):
                                j.health = j.health - i.damage
                        for j in archer:
                            if(abs(j.x - b[barbarian_index].x) <= 2 and abs(j.y - b[barbarian_index].y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        for j in balloon:
                            if(abs(j.x - b[barbarian_index].x) <= 2 and abs(j.y - b[barbarian_index].y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        if(abs(use.x - b[barbarian_index].x) <= 2 and abs(use.y - b[barbarian_index].y) <= 1 and (use.health > 0)):
                            use.health = use.health - i.damage
            for barbarian_index in archer:
                for index in range(len(wizard)):
                    if((abs(barbarian_index.x - wizard[index].x) <= 10) and (abs(barbarian_index.y - wizard[index].y) <= 5) and (barbarian_index.health > 0) and (wizard_zeroes[index] == 0)):
                        barbarian_index.health = barbarian_index.health - \
                            wizard[index].damage
                        wizard_zeroes[index] = 1
                        for j in b:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        for j in archer:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0) and j != barbarian_index):
                                j.health = j.health - i.damage
                        for j in balloon:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        if(abs(use.x - barbarian_index.x) <= 2 and abs(use.y - barbarian_index.y) <= 1 and (use.health > 0)):
                            use.health = use.health - i.damage
            for barbarian_index in balloon:
                for index in range(len(wizard)):
                    if((abs(barbarian_index.x - wizard[index].x) <= 10) and (abs(barbarian_index.y - wizard[index].y) <= 5) and (barbarian_index.health > 0) and (wizard_zeroes[index] == 0)):
                        barbarian_index.health = barbarian_index.health - \
                            wizard[index].damage
                        wizard_zeroes[index] = 1
                        for j in b:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        for j in archer:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0) and j != barbarian_index):
                                j.health = j.health - i.damage
                        for j in balloon:
                            if(abs(j.x - barbarian_index.x) <= 2 and abs(j.y - barbarian_index.y) <= 1 and (j.health > 0)):
                                j.health = j.health - i.damage
                        if(abs(use.x - barbarian_index.x) <= 2 and abs(use.y - barbarian_index.y) <= 1 and (use.health > 0)):
                            use.health = use.health - i.damage

    def distance(x1, y1, x2, y2):
        return ((((x2 - x1)**2) + ((y2-y1)**2))**0.5)

    latest = []
    queen_specialcount = 0

    print("Do you want to operate the king or the queen?:")
    while(1):
        choice = input_to()
        if(choice == "k"):
            fp.write("k %s\n" % (time.time() - t0))
            break
        elif(choice == "q"):
            fp.write("q %s\n" % (time.time() - t0))
            break

    while(True):
        # os.system("clear")
        p = input_to()
        win_check = 1
        lose_check = 1
    # time.sleep(0.1)
    # print("King Health: ",end="")
        # for i in range(k.health):
        #   print(Back.GREEN,end="")
        # print(Style.RESET_ALL)
        while(queen_specialcount > 0):
            for i in range(len(timekeep)):
                if(time.time() - timekeep[i] >= 1):
                    timekeep.pop(i)
                    queen_specialcount -= 1
                    specialattack()
        if(h1.health <= 0 and h2.health <= 0 and h3.health <= 0 and h4.health <= 0 and h5.health <= 0 and th1.health <= 0):
            for i in cannon:
                if(i.health > 0):
                    win_check = 0
            for i in wizard:
                if(i.health > 0):
                    win_check = 0
            if(win_check == 1):
                print("You have won the game")
                level += 1
                print("Do you wish to play next level ?")
                while(1):
                    choice1 = input_to()
                    if(choice1 == "y"):
                        fp.write("y %s\n" % (time.time() - t0))
                        return 738
                    elif(choice1 == "n"):
                        fp.write("n %s\n" % (time.time() - t0))
                        return
        else:
            for i in b:
                if(i.health > 0):
                    lose_check = 0
            for i in archer:
                if(i.health > 0):
                    lose_check = 0
            for i in balloon:
                if(i.health > 0):
                    lose_check = 0
            if(choice == "k"):
                if(k.health > 0):
                    lose_check = 0
            elif(choice == "q"):
                if(q.health > 0):
                    lose_check = 0
            if(lose_check == 1):
                print("You have lost the game")
                print("Do you wish to play again ?")
                while(1):
                    choice2 = input_to()
                    if(choice2 == "y"):
                        fp.write("y %s\n" % (time.time() - t0))
                        return
                    elif(choice2 == "n"):
                        fp.write("n %s\n" % (time.time() - t0))
                        return -1
        if(choice == "k"):
            if(p == "w" and k.y - 1 >= 0 and arr[k.y - 1][k.x] == 0):
                fp.write("w %s\n" % (time.time() - t0))
                for i in range(k.speed):
                    if(k.y - 1 >= 0 and arr[k.y - 1][k.x] == 0):
                        k.y = k.y - 1
                        arr[k.y][k.x] = 1
                        arr[k.y + 1][k.x] = 0
            elif(p == "s" and k.y + 1 >= 0 and arr[k.y + 1][k.x] == 0):
                fp.write("s %s\n" % (time.time() - t0))
                latest.append(p)
                for i in range(k.speed):
                    if(k.y + 1 <= m-1 and arr[k.y + 1][k.x] == 0):
                        k.y = k.y + 1
                        arr[k.y][k.x] = 1
                        arr[k.y - 1][k.x] = 0
            elif(p == "a" and k.x - 2 >= 0 and arr[k.y][k.x - 2] == 0):
                fp.write("a %s\n" % (time.time() - t0))
                latest.append(p)
                for i in range(k.speed):
                    if(k.x - 2 >= 0 and arr[k.y][k.x - 2] == 0):
                        k.x = k.x - 2
                        arr[k.y][k.x] = 1
                        arr[k.y][k.x + 2] = 0
            elif(p == "d" and k.x + 2 >= 0 and arr[k.y][k.x + 2] == 0):
                fp.write("d %s\n" % (time.time() - t0))
                latest.append(p)
                for i in range(k.speed):
                    if(k.x + 2 <= n-1 and arr[k.y][k.x + 2] == 0):
                        k.x = k.x + 2
                        arr[k.y][k.x] = 1
                        arr[k.y][k.x - 2] = 0
        if(choice == "q"):
            if(p == "w" and q.y - 1 >= 0 and arr[q.y - 1][q.x] == 0):
                fp.write("w %s\n" % (time.time() - t0))
                upq = 0
                for i in range(q.speed):
                    if(q.y - 1 >= 0 and arr[q.y - 1][q.x] == 0):
                        q.y = q.y - 1
                        arr[q.y][q.x] = 1
                        arr[q.y + 1][q.x] = 0
                        upq = 1
                if(upq == 1):
                    latest.append(p)
                    upq = 0
            elif(p == "s" and q.y + 1 >= 0 and arr[q.y + 1][q.x] == 0):
                fp.write("s %s\n" % (time.time() - t0))
                dq = 0
                for i in range(q.speed):
                    if(q.y + 1 <= m-1 and arr[q.y + 1][q.x] == 0):
                        q.y = q.y + 1
                        arr[q.y][q.x] = 1
                        arr[q.y - 1][q.x] = 0
                        dq = 1
                if(dq == 1):
                    latest.append(p)
                    dq = 0
            elif(p == "a" and q.x - 2 >= 0 and arr[q.y][q.x - 2] == 0):
                fp.write("a %s\n" % (time.time() - t0))
                lq = 0
                for i in range(q.speed):
                    if(k.x - 2 >= 0 and arr[q.y][q.x - 2] == 0):
                        q.x = q.x - 2
                        arr[q.y][q.x] = 1
                        arr[q.y][q.x + 2] = 0
                        lq = 1
                if(lq == 1):
                    latest.append(p)
                    lq = 0
            elif(p == "d" and q.x + 2 >= 0 and arr[q.y][q.x + 2] == 0):
                fp.write("d %s\n" % (time.time() - t0))
                rq = 0
                for i in range(q.speed):
                    if(q.x + 2 <= n-1 and arr[q.y][q.x + 2] == 0):
                        q.x = q.x + 2
                        arr[q.y][q.x] = 1
                        arr[q.y][q.x - 2] = 0
                        rq = 1
                if(rq == 1):
                    latest.append(p)
                    rq = 0
        if(p == "h"):  # heal spell
            fp.write("h %s\n" % (time.time() - t0))
            if(1.5*(k.health) < 400):
                k.health = 1.5*k.health
            else:
                k.health = 400
            if(1.5*(q.health) < 400):
                q.health = 1.5*q.health
            else:
                q.health = 400
            barbarian_index = 0
            for barbarian_index in range(barbarian_count):
                if(1.5*(b[barbarian_index].health) < 200):
                    b[barbarian_index].health = 1.5*b[barbarian_index].health
                else:
                    b[barbarian_index].health = 200
            for barbarian_index in range(archer_count):
                if(1.5*(archer[barbarian_index].health) < 100):
                    archer[barbarian_index].health = 1.5 * \
                        archer[barbarian_index].health
                else:
                    archer[barbarian_index].health = 100
            for barbarian_index in range(balloon_count):
                if(1.5*(balloon[barbarian_index].health) < 200):
                    balloon[barbarian_index].health = 1.5 * \
                        balloon[barbarian_index].health
                else:
                    balloon[barbarian_index].health = 200
        elif(p == "r"):  # rage spell
            fp.write("r %s\n" % (time.time() - t0))
            if(k.health > 0):
                k.speed = 2*k.speed
                k.damage = 2*k.damage
            if(q.health > 0):
                q.speed = 2*q.speed
                q.damage = 2*q.damage
            barbarian_index = 0
            for barbarian_index in range(barbarian_count):
                if(b[barbarian_index].health > 0):
                    b[barbarian_index].speed = 2*b[barbarian_index].speed
                    b[barbarian_index].damage = 2*b[barbarian_index].damage
            for barbarian_index in range(archer_count):
                if(archer[barbarian_index].health > 0):
                    archer[barbarian_index].speed = 2 * \
                        archer[barbarian_index].speed
                    archer[barbarian_index].damage = 2 * \
                        archer[barbarian_index].damage
        elif(p == "b"):
            fp.write("b %s\n" % (time.time() - t0))
        # b[0] = Troop(3,39,200,20,1)
            if(Barb1 + Barb2 + Barb3 < 6):
                Barb1 += 1
                barbarian_count += 1
                b.append(Troop(3, 39, 200, 20, 1))
        elif(p == "2"):
            fp.write("2 %s\n" % (time.time() - t0))
        # b[1] = Troop(65,33,200,20,1)
            if(Barb1 + Barb2 + Barb3 < 6):
                Barb2 += 1
                barbarian_count += 1
                b.append(Troop(65, 33, 200, 20, 1))
        elif(p == "3"):
            fp.write("3 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Barb1 + Barb2 + Barb3 < 6):
                Barb3 += 1
                barbarian_count += 1
                b.append(Troop(39, 3, 200, 20, 1))
        elif(p == "4"):
            fp.write("4 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Arch1 + Arch2 + Arch3 < 6):
                Arch1 += 1
                archer_count += 1
                archer.append(Archer(3, 27, 100, 10, 2, 4))
        elif(p == "5"):
            fp.write("5 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Arch1 + Arch2 + Arch3 < 6):
                Arch2 += 1
                archer_count += 1
                archer.append(Archer(65, 23, 100, 10, 2, 4))
        elif(p == "6"):
            fp.write("6 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Arch1 + Arch2 + Arch3 < 6):
                Arch3 += 1
                archer_count += 1
                archer.append(Archer(39, 38, 100, 10, 2, 4))
        elif(p == "7"):
            fp.write("7 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Ball1 + Ball2 + Ball3 < 3):
                Ball1 += 1
                balloon_count += 1
                balloon.append(Balloon(57, 35, 200, 40, 2))
        elif(p == "8"):
            fp.write("8 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Ball1 + Ball2 + Ball3 < 3):
                Ball2 += 1
                balloon_count += 1
                balloon.append(Balloon(45, 25, 200, 40, 2))
        elif(p == "9"):
            fp.write("9 %s\n" % (time.time() - t0))
        # b[2] = Troop(39,3,200,20,1)
            if(Ball1 + Ball2 + Ball3 < 3):
                Ball3 += 1
                balloon_count += 1
                balloon.append(Balloon(3, 5, 200, 40, 2))
        elif(p == " "):
            fp.write("  %s\n" % (time.time() - t0))
            if(choice == "k"):
                attack()
            else:
                if(latest[-1] != " "):
                    attack_queen()
        elif(p == "v"):
            timekeep.append(time.time())
            fp.write("v %s\n" % (time.time() - t0))
            queen_specialcount += 1
        elif(p == "q"):
            fp.write("q %s\n" % (time.time() - t0))
            ec = 0
            return -1
            # break
        print(chr(27) + "[2J")
        for i in range(m-1):
            print(" ___", end="")
        print("")
        defense()
        if(Barb1+Barb2+Barb3 <= 6 and Barb1+Barb2+Barb3 > 0):
            for barbarian_index in range(barbarian_count):
                if(b[barbarian_index].health > 0):
                    b[barbarian_index].barbdistance1()
        if(Arch1+Arch2+Arch3 <= 6 and Arch1+Arch2+Arch3 > 0):
            for barbarian_index in range(archer_count):
                if(archer[barbarian_index].health > 0):
                    archer[barbarian_index].archerdistance()
        if(Ball1+Ball2+Ball3 <= 3 and Ball1+Ball2+Ball3 > 0):
            for barbarian_index in range(balloon_count):
                if(balloon[barbarian_index].health > 0):
                    balloon[barbarian_index].move()
        # if(Barb2):
        #   b[1].barbdistance1()
        # if(Barb3):
        #   b[2].barbdistance1()
        for i in range(m):
            for j in range(n):
                l = int((j-1)/2)
                barbarian_bool = 0
                archer_bool = 0
                balloon_bool = 0
                check = 0
                cannon_check = 0
                wizard_check = 0
                for wall_i in w:
                    if(i == wall_i.y and j == wall_i.x):
                        wall_health = wall_i.health
                        check = 1
                        break
                if(check == 0):
                    wall_health = 0
                for wall_i in cannon:
                    if(i == wall_i.y and j == wall_i.x):
                        cannon_health = wall_i.health
                        cannon_check = 1
                        cannon_break = wall_i
                        break
                if(cannon_check == 0):
                    cannon_health = 0
                for wall_i in wizard:
                    if(i == wall_i.y and j == wall_i.x):
                        wizard_health = wall_i.health
                        wizard_check = 1
                        wizard_break = wall_i
                        break
                if(wizard_check == 0):
                    wizard_health = 0
                if(i == k.y and j == k.x):  # king spawn
                    if(k.health > 0):
                        print(Fore.RED + "_K_", end="")
                        print(Style.RESET_ALL, end="")
                        arr[i][j] = 1
                    else:
                        if(j % 2 == 0):
                            print("|", end="")
                            arr[i][j] = 0
                        else:
                            print("___", end="")
                            arr[i][j] = 0
                elif(i == q.y and j == q.x):  # queen spawn
                    if(q.health > 0):
                        print(Fore.RED + "_Q_", end="")
                        print(Style.RESET_ALL, end="")
                        arr[i][j] = 1
                    else:
                        if(j % 2 == 0):
                            print("|", end="")
                            arr[i][j] = 0
                        else:
                            print("___", end="")
                            arr[i][j] = 0
                #    strings[(i+1)*(l)] = "_K_"
                # elif(Barb[0]==1):
                else:
                    # barbarian_index=0
                    for barbarian_index in range(barbarian_count):
                        # barb[0] spawn
                        if(i == b[barbarian_index].y and j == b[barbarian_index].x and barbarian_bool == 0):
                            if(b[barbarian_index].health > 125):
                                print(Fore.GREEN + "_B_", end="")
                                print(Style.RESET_ALL, end="")
                                arr[i][j] = 1
                            elif(b[barbarian_index].health > 50):
                                print(Fore.YELLOW + "_B_", end="")
                                print(Style.RESET_ALL, end="")
                                arr[i][j] = 1
                            elif(b[barbarian_index].health > 0 and b[barbarian_index].health <= 50):
                                print(Fore.RED + "_B_", end="")
                                print(Style.RESET_ALL, end="")
                                arr[i][j] = 1
                            else:
                                print("___", end="")
                                arr[i][j] = 0
                                b[barbarian_index].x = -100
                                b[barbarian_index].y = -100
                            barbarian_bool = 1
                    if barbarian_bool == 0:
                        for archer_index in range(archer_count):
                            if(i == archer[archer_index].y and j == archer[archer_index].x and archer_bool == 0):
                                if(archer[archer_index].health > 75):
                                    print(Fore.GREEN + "_A_", end="")
                                    print(Style.RESET_ALL, end="")
                                    arr[i][j] = 1
                                elif(archer[archer_index].health > 35):
                                    print(Fore.YELLOW + "_A_", end="")
                                    print(Style.RESET_ALL, end="")
                                    arr[i][j] = 1
                                elif(archer[archer_index].health > 0 and archer[archer_index].health <= 35):
                                    print(Fore.RED + "_A_", end="")
                                    print(Style.RESET_ALL, end="")
                                    arr[i][j] = 1
                                else:
                                    print("___", end="")
                                    arr[i][j] = 0
                                    archer[archer_index].x = -100
                                    archer[archer_index].y = -100
                                archer_bool = 1
                        if archer_bool == 0:
                            for balloon_index in range(balloon_count):
                                if(i == balloon[balloon_index].y and j == balloon[balloon_index].x and balloon_bool == 0):
                                    if(balloon[balloon_index].health > 150):
                                        print(Fore.GREEN + "_O_", end="")
                                        print(Style.RESET_ALL, end="")
                                        #arr[i][j] = 1
                                    elif(balloon[balloon_index].health > 75):
                                        print(Fore.YELLOW + "_O_", end="")
                                        print(Style.RESET_ALL, end="")
                                        #arr[i][j] = 1
                                    elif(balloon[balloon_index].health > 0 and balloon[balloon_index].health <= 75):
                                        print(Fore.RED + "_O_", end="")
                                        print(Style.RESET_ALL, end="")
                                        #arr[i][j] = 1
                                    else:
                                        print("___", end="")
                                        arr[i][j] = 0
                                        balloon[balloon_index].x = -100
                                        balloon[balloon_index].y = -100
                                    balloon_bool = 1
                            if balloon_bool == 0:
                                if(cannon_check == 1):  # canons
                                    if(cannon_health > 200):
                                        print(Fore.GREEN + "Can", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    elif(cannon_health > 50):
                                        print(Fore.YELLOW + "Can", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    elif(cannon_health > 0 and cannon_health <= 50):
                                        print(Fore.RED + "Can", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    else:
                                        print("___", end="")
                                        arr[i][j] = 0
                                        cannon_break.x = -100
                                        cannon_break.y = -100
                                elif(wizard_check == 1):  # canons
                                    if(wizard_health > 200):
                                        print(Fore.GREEN + "WIZ", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    elif(wizard_health > 50):
                                        print(Fore.YELLOW + "WIZ", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    elif(wizard_health > 0 and wizard_health <= 50):
                                        print(Fore.RED + "WIZ", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                    else:
                                        print("___", end="")
                                        arr[i][j] = 0
                                        wizard_break.x = -100
                                        wizard_break.y = -100
                                elif(i < 21 and i > 17):
                                    if(j > 36 and j < 44):
                                        if(th1.health > 400):
                                            if(j % 2 == 0):
                                                print("|", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 0
                                            else:
                                                print(Back.BLUE +
                                                      "___", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            #   strings[(i+1)*(l)] = "___"
                                        elif(th1.health > 250):
                                            if(j % 2 == 0):
                                                print("|", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 0
                                            else:
                                                print(Back.GREEN +
                                                      "___", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                        elif(th1.health > 100):
                                            if(j % 2 == 0):
                                                print("|", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 0
                                            else:
                                                print(Back.YELLOW +
                                                      "___", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                        elif(th1.health > 0):
                                            if(j % 2 == 0):
                                                print("|", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 0
                                            else:
                                                print(Back.RED + "___", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                        else:
                                            if(j % 2 == 0):
                                                print("|", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 0
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                th1.x = -100
                                                th1.y = -100
                                            #   strings[(i+1)*(l)] = "___"
                                    elif(j == 34 or j == 44):
                                        print("|", end="")
                                        print(Style.RESET_ALL, end="")
                                    elif((j == 35 or j == 45) and wall_health > 0):
                                        print("Wal", end="")
                                        print(Style.RESET_ALL, end="")
                                        arr[i][j] = 1
                                        #w.append(Walls(i, j,300))
                                    #  strings[(i+1)*(l)] = "Wal"
                                    elif(j != 81):
                                        if (j % 2 == 0):
                                            print("|", end="")
                                        else:
                                            print("___", end="")
                                        arr[i][j] = 0
                                        #  strings[(i+1)*(l)] = "___"
                                    else:
                                        print("")
                                elif(i == 21 or i == 17):
                                    if(j > 34 and j < 46):
                                        if(j % 2 == 0):
                                            print("|", end="")
                                            print(Style.RESET_ALL, end="")
                                        elif(wall_health > 0):
                                            print("Wal", end="")
                                            print(Style.RESET_ALL, end="")
                                            arr[i][j] = 1
                                            #w.append(Walls(i, j,300))
                                    #     strings[(i+1)*(l)] = "Wal"
                                        else:
                                            print("___", end="")
                                            arr[i][j] = 0
                                    elif(j != 81):
                                        if (j % 2 == 0):
                                            print("|", end="")
                                        else:
                                            print("___", end="")
                                        arr[i][j] = 0
                                    #     strings[(i+1)*(l)] = "___"
                                    else:
                                        print("")

                                # upper huts
                                elif((j == 7 or j == 8 or j == 9 or j == 10 or j == 73 or j == 74) and i == 3):
                                    if(j % 2 == 0):
                                        print("|", end="")
                                        print(Style.RESET_ALL, end="")
                                    else:
                                        if(j == 7 and i == 3):
                                            if(h1.health > 50):
                                                print(Fore.GREEN +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h1.health > 20):
                                                print(Fore.YELLOW +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h1.health > 0 and h1.health <= 20):
                                                print(Fore.RED + "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                h1.x = -100
                                                h1.y = -100
                                        if(j == 9 and i == 3):
                                            if(h2.health > 50):
                                                print(Fore.GREEN +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h2.health > 20):
                                                print(Fore.YELLOW +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h2.health > 0 and h2.health <= 20):
                                                print(Fore.RED + "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                h2.x = -100
                                                h2.y = -100
                                        if(j == 73 and i == 3):
                                            if(h3.health > 50):
                                                print(Fore.GREEN +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h3.health > 20):
                                                print(Fore.YELLOW +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h3.health > 0 and h3.health <= 20):
                                                print(Fore.RED + "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                h3.x = -100
                                                h3.y = -100
                                    # strings[(i+1)*(l)] = "Hut"
                                elif((j == 7 or j == 8 or j == 73 or j == 74) and i == 37):  # lower huts
                                    if(j % 2 == 0):
                                        print("|", end="")
                                        print(Style.RESET_ALL, end="")
                                    else:
                                        if(j == 7 and i == 37):
                                            if(h4.health > 50):
                                                print(Fore.GREEN +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h4.health > 20):
                                                print(Fore.YELLOW +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h4.health > 0 and h4.health <= 20):
                                                print(Fore.RED + "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                h4.x = -100
                                                h4.y = -100

                                        if(j == 73 and i == 37):
                                            if(h5.health > 50):
                                                print(Fore.GREEN +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h5.health > 20):
                                                print(Fore.YELLOW +
                                                      "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            elif(h5.health > 0 and h5.health <= 20):
                                                print(Fore.RED + "Hut", end="")
                                                print(Style.RESET_ALL, end="")
                                                arr[i][j] = 1
                                            else:
                                                print("___", end="")
                                                arr[i][j] = 0
                                                h5.x = -100
                                                h5.y = -100
                                    # strings[(i+1)*(l)] = "Hut"
                                elif(j != 81):
                                    if (j % 2 == 0):
                                        print("|", end="")
                                    else:
                                        print("___", end="")
                                    arr[i][j] = 0
                                    # strings[(i+1)*(l-1)] = "___"
                                else:
                                    print("")
        if(choice == "k"):
            print("King's Health: ")
            for i in range(100):
                if(i <= (k.health/400)*100):
                    print(Back.GREEN + " ", end='')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end="")
        elif(choice == "q"):
            print("Queen's Health: ")
            for i in range(100):
                if(i <= (q.health/400)*100):
                    print(Back.GREEN + " ", end='')
                    print(Style.RESET_ALL, end="")
                else:
                    print(" ", end="")
        print('', end="")
        print("|")
        for x in w:
            # print(w[x].health)
            if(x.health <= 0):
                x.x = -100
                x.y = -100
                w.pop(w.index(x))
        # for i in range(m-1):
        #    print(strings[i])

    # print(k.x,k.y,k.health,k.damage,k.speed)
ret = 1
while ret != -1:
    if(ret == 738):
        level += 1
    ret = initial(level, ec)
