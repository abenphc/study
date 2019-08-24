from enum import Enum
import random

BLOCKWIDTH = 36
BLOCKHEIGHT = 30
MINE_COUNT = 99


class BlockStatus(Enum):
    normal = 1  # 未点击
    opened = 2  # 已点击
    mine = 3  # 地雷
    flag = 4  # 标记为地雷
    ask = 5  # 标记为问号
    bomb = 6  # 踩中地雷
    hint = 7  # 被双击的周围
    double = 8  # 正在被双击


class Mine:
    def __init__(self, x, y, value=0):
        self._x = x
        self._y = y
        self._value = 0  # 0:非地雷; 1:地雷
        self._around_mine_count = -1
        self._status = BlockStatus.normal
        self.set_value(value)

    def __repr__(self):
        return self._value

    def set_value(self, value):
        pass

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    y = property(fget=get_y, fset=set_y)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value:
            self.value = 1
        else:
            self.value = 0

    @property
    def around_mine_count(self):
        return self._around_mine_count

    @around_mine_count.setter
    def around_mine_count(self, around_mine_count):
        self._around_mine_count = around_mine_count

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


'''布雷'''


class MineBlock:
    def __init__(self):
        # 创建所有方块构成列表
        self._block = [[(Mine(i, j) for i in range(BLOCKWIDTH))] for j in range(BLOCKHEIGHT)]
        # 布雷
        for i in random.sample(range(BLOCKWIDTH * BLOCKHEIGHT), MINE_COUNT):
            self._block[i // BLOCKWIDTH][i % BLOCKHEIGHT].value = 1

    def openMine(self, x, y):
        # hit mine
        if self._block[y][x].value:
            self._block[y][x].status = BlockStatus.bomb
            return False

        self._block.status[y][x] = BlockStatus.opened

        around = _get_around(x, y)

        _sum = 0
        for i, j in around:
            if self._block[j][i].value:
                _sum += 1

        self._block[y, x].around_mine_count = _sum

        if _sum == 0:
            for i,j in around:
                if self._block[j][i].around_mine_count == -1:
                    self.openMine(i,j)

        return True


def _get_around(x, y):
    return [(i, j) for i in range(max(0, x - 1), min(BLOCKWIDTH - 1, x + 1) + 1)
            for j in range(max(0, y - 1), min(BLOCKHEIGHT - 1, y + 1) + 1) if i != x and j != y]

