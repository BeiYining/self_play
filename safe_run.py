import sys
import os
import time
import shutil
from multiprocessing import Process

try:
    import pygame as pg
    from random import randrange
    from fruit import create_fruit
    from game import GameBoard
    import pymunk
except ImportError:
    os.system('pip3 install pygame pymunk -i https://mirrors.aliyun.com/pypi/simple/')
    import pygame as pg
    from random import randrange
    from fruit import create_fruit
    from game import GameBoard
    import pymunk

os.system('python -u ./main.py')