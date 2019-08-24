import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

# 控制怪物速度

COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8

# 怪物的类型
TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3


class Monster(Sprite):
    def __init__(self, view_manager, tp=TYPE_BOMB):
        super().__init__()
