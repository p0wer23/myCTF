from secret import config
import math
from py_mini_racer import py_mini_racer

class LCG:
    lcg_m = config.m
    lcg_c = config.c
    lcg_n = config.n

    def __init__(self, lcg_s):
        self.state = lcg_s

    def next(self):
        self.state = (self.state * self.lcg_m + self.lcg_c) % self.lcg_n
        return self.state


def v8random():
    ctx = py_mini_racer.MiniRacer()
    result = ctx.execute('Array.from(Array(6), Math.random)')
    return result