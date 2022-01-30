import math
import random
import numpy as np
from numba import jit

pi = 3.1415927


# 通过迭代生成h mtd=0
@jit(nopython=True)
def get_h_set0(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set1(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(i * x * coslist[i] + i * y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set2(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + i * np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set3(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i] + i)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set4(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + i / 8
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set5(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + 2 * np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set6(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q + 0.5)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set7(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set8(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + 1
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set9(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i] + 0.5) + 1
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set10(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set11(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
        sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set12(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
        sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set13(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.abs(i * np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set14(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.sin(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set15(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.tan(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set16(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + 1 / np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set17(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set18(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.sin(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set19(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.tan(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set20(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set21(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.tan(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set22(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * sinlist[i] + y * coslist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set23(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x / coslist[i] + y / sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set24(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set25(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            cosx = np.cos(x)
            siny = np.sin(y)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(cosx * coslist[i] + siny * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set26(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            tanx = np.tan(x)
            if 0 == y:
                y = 1
            rtany = 1 / np.tan(y)  # 除数可能为0，偏移量须设为非0
            # rtany = 1
            h = 0
            for i in range(1, Q):
                h = h + np.cos(tanx * coslist[i] + rtany * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set27(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.abs(np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set28(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(np.abs(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set29(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            cosx = np.cos(x)
            siny = np.sin(y)
            for i in range(1, Q):
                h = h + np.tan(cosx * coslist[i] + siny * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set30(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            cosx = np.cos(x)
            siny = np.sin(y)
            for i in range(1, Q):
                h = h + np.abs(cosx * coslist[i] + siny * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set31(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            cosx = np.cos(x)
            siny = np.sin(y)
            for i in range(1, Q):
                h = h + np.cos(np.tan(cosx * coslist[i]) + np.tan(siny * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set32(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set33(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set34(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 15)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set35(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set36(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set37(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set38(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.sqrt(np.abs(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set39(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set40(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 3)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 3)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set41(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 15)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 15)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set42(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.sqrt(np.abs(np.cos(2 * pi * i / q)))
        sinlist[i] = np.sqrt(np.abs(np.sin(2 * pi * i / q)))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set43(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sqrt(np.abs(x))
            Y = np.sqrt(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set44(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.power(np.abs(x), 0.75)
            Y = np.power(np.abs(y), 0.75)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set45(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.power(np.abs(x), 1.25)
            Y = np.power(np.abs(y), 1.25)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set46(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sin(np.sqrt(np.abs(x)))
            Y = np.cos(np.sqrt(np.abs(y)))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set47(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set48(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sqrt(np.abs(x))
            Y = np.sqrt(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set49(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sqrt(np.abs(x))
            Y = np.sqrt(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set50(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sin(np.sqrt(np.abs(x)))
            Y = np.cos(np.sqrt(np.abs(y)))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set51(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
        sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.sqrt(np.abs(x))
            Y = np.sqrt(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set52(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set53(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set54(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.exp(np.cos(2 * pi * i / q))
        sinlist[i] = np.exp(np.sin(2 * pi * i / q))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set55(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.exp(np.sqrt(np.abs(np.cos(2 * pi * i / q))))
        sinlist[i] = np.exp(np.sqrt(np.abs(np.sin(2 * pi * i / q))))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set56(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.exp(np.cos(2 * pi * i / q))
        sinlist[i] = np.exp(np.sin(2 * pi * i / q))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set57(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.exp(np.cos(2 * pi * i / q))
        sinlist[i] = np.exp(np.sin(2 * pi * i / q))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i]))))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set58(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set59(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set60(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set61(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
        sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set62(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.log(np.abs(x))
            Y = np.log(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set63(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.cos(np.log(np.abs(x)))
            Y = np.log(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set64(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
        sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set65(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
        sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.log(np.abs(x))
            Y = np.log(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(X * coslist[i] + Y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set66(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
        sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = np.log(np.abs(x))
            Y = np.log(np.abs(y))
            h = 0
            for i in range(1, Q):
                h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set67(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = (np.sin(x) + np.cos(y)) / 5
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set68(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = np.cos(np.sin(x) + y) / 5
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set69(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = (x + y) / 25
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set70(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = (x * x + y * y) / 200
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set71(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.cos(temp) + np.power(np.sin(temp), 2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set72(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                temp2 = np.cos(temp)
                h = h + temp2 + np.power(np.sin(temp), 2) + np.power(temp2, 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set73(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.tan(temp) + np.power(np.cos(temp), 2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set74(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                temp2 = np.cos(temp)
                h = h + temp2 + np.power(temp2, 100) + np.power(temp2, 101)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set75(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                temp2 = np.cos(temp)
                for t in range(1, 6):
                    h = h + np.power(temp2, t)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set76(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                temp2 = np.sin(temp)
                for t in range(1, 6):
                    h = h + np.abs(temp2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set77(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = np.exp(np.cos(x) + np.sin(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set78(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = np.log(x * x + y * y) / 5
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set79(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            add = np.log(np.abs(np.sin(x) + np.cos(y))) / 5
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set80(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.abs(np.cos(temp)) + np.power(np.sin(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set81(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.abs(np.cos(temp) + np.power(np.sin(temp), 2))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set82(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.cos(np.cos(temp)) + np.power(np.sin(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set83(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.sin(temp) + np.power(np.cos(np.cos(temp)), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set84(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.tan(np.sin(temp)) + np.power(np.cos(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set85(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.exp(np.cos(temp)) + np.power(np.cos(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set86(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.exp(np.sin(temp)) + np.power(np.cos(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set87(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.log(np.abs(np.cos(temp))) + np.power(np.cos(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set88(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 3)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set89(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 100)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set90(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.abs(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set91(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.sin(np.cos(temp)) + np.log(np.abs(np.sin(temp)))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set92(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.exp(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set93(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                temp = x * coslist[i] + y * sinlist[i]
                h = h + np.sqrt(np.exp(np.sin(temp))) + np.log(np.abs(np.cos(temp)))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set94(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            p = np.cos(x) * np.cos(y)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set95(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            p = np.sin(x) * np.cos(y)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set96(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            p = np.sin(x - y) * np.cos(x + y)
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set97(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            p = np.exp(np.sin(x)) * np.exp(np.cos(y))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set98(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            p = np.exp(np.sin(x)) * np.exp(np.cos(y)) * np.exp(np.sin(y)) * np.exp(np.cos(x))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set99(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            sinx = np.sin(x)
            cosy = np.cos(y)
            p = np.exp(sinx) * np.exp(cosy) * np.log(np.abs(sinx * cosy))
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set100(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.cos(x * np.sin(coslist[i]) + y * np.sin(sinlist[i]))) \
                    + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set101(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.power(np.tan(np.sin(x * coslist[i] + y * sinlist[i]) *
                                        np.power(np.sin(y * sinlist[i] + x * coslist[i]), 3)), 4)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set102(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), q))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set103(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), i))
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set104(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h - np.cos(x * coslist[i] + y * sinlist[i]) * coslist[i] * sinlist[i]
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set105(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            temp1 = np.cos(x * coslist[i] + y * sinlist[i])
            temp2 = np.sin(x * coslist[i] + y * sinlist[i])
            for i in range(1, Q):
                h = h - (np.exp(temp1) * temp1 + 2 * temp2) * coslist[i] * sinlist[i]
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set106(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            pwq2 = int(q) * int(q)
            X = 2 * x * pi
            Y = 2 * y * pi
            for i in range(1, Q):
                h = h - np.sin(x * coslist[i] + y * sinlist[i]) * \
                    (X * i / pwq2 * sinlist[i] - Y * i / pwq2 * coslist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set107(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            pwq2 = int(q) * int(q)
            h = 0
            for i in range(1, Q):
                cxcys = np.cos(x * coslist[i] + y * sinlist[i])
                sxcys = np.sin(x * coslist[i] + y * sinlist[i])
                temp = 2 * x * pi * i / pwq2 * sinlist[i] - 2 * y * pi * i / pwq2 * coslist[i]
                h = h + np.exp(sxcys) * cxcys * temp - 3 * cxcys * cxcys * temp
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set108(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h - np.sin(x * coslist[i] + y * sinlist[i]) * \
                    (2 * x * pi / q * sinlist[i] - 2 * y * pi / q * coslist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set109(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            X = 2 * x * pi / q
            Y = 2 * y * pi / q
            h = 0
            for i in range(1, Q):
                xsyc = x * sinlist[i] + y * coslist[i]
                sxsyc = np.sin(xsyc)
                cxsyc = np.cos(xsyc)
                temp = X * coslist[i] - Y * sinlist[i]
                h = h + np.exp(sxsyc) * cxsyc * temp + 4 * cxsyc * cxsyc * cxsyc * temp
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set110(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = 2 * pi * i / q
                t2 = t * t
                t4 = t2 * t2
                t10 = t2 * t4 * t4
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 720 + (t4 * t4) / 40320 - t10 / 3628800 \
                     + (t2 * t10) / 3628800 / 11 / 12 - (t4 * t10) / 3628800 / 11 / 12 / 13 / 14
                a2 = t - (t * t2) / 6 + (t * t4) / 120 - (t * t2 * t4) / 5040 + (t * t4 * t4) / 362880 - \
                     (t * t10) / 3628800 / 11 + (t * t2 * t10) / 3628800 / 11 / 12 / 13 - \
                     (t * t4 * t10) / 3628800 / 11 / 12 / 13 / 14 / 15
                h = h + np.cos(x * a1 + y * a2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set111(q, s, w, xmin, ymin, mag=10):
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = 2 * pi * i / q
                t2 = t * t
                t4 = t2 * t2
                t10 = t2 * t4 * t4
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 720 + (t4 * t4) / 40320 - t10 / 3628800 \
                     + (t2 * t10) / 3628800 / 11 / 12
                a2 = t - (t * t2) / 6 + (t * t4) / 120 - (t * t2 * t4) / 5040 + (t * t4 * t4) / 362880 - \
                     (t * t10) / 3628800 / 11 + (t * t2 * t10) / 3628800 / 11 / 12 / 13
                h = h + np.cos(x * a1 + y * a2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set112(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = 2 * pi * i / q
                t2 = t * t
                t4 = t2 * t2
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 720 + (t4 * t4) / 40320
                a2 = t - (t * t2) / 6 + (t * t4) / 120 - (t * t2 * t4) / 5040 + (t * t4 * t4) / 362880
                h = h + np.cos(x * a1 + y * a2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set113(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = x * coslist[i] + y * sinlist[i]
                t2 = t * t
                t4 = t2 * t2
                t10 = t2 * t4 * t4
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 720 + (t4 * t4) / 40320 - t10 / 3628800 \
                     + (t2 * t10) / 3628800 / 11 / 12 - (t4 * t10) / 3628800 / 11 / 12 / 13 / 14
                h = h + a1
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set114(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = 2 * pi * i / q
                t2 = t * t
                t4 = t2 * t2
                t10 = t2 * t4 * t4
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 720 + (t4 * t4) / 40320 - t10 / 3628800 \
                     + (t2 * t10) / 3628800 / 11 / 12 - (t * t2 * t10) / 3628800 / 11 / 12 / 13 / 14
                a2 = t - (t * t2) / 6 + (t * t4) / 120 - (t * t2 * t4) / 5040 + (t * t4 * t4) / 362880 - \
                     (t * t10) / 3628800 / 11 + (t * t2 * t10) / 3628800 / 11 / 12 / 13 - \
                     (t4 * t10) / 3628800 / 11 / 12 / 13 / 14 / 15
                h = h + np.cos(x * a1 + y * a2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set115(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = 2 * pi * i / q
                t2 = t * t
                t4 = t2 * t2
                t10 = t2 * t4 * t4
                a1 = 1 - t2 / 2 + t4 / 24 - (t2 * t4) / 710 + (t4 * t4) / 40320 - t10 / 3628800 \
                     + (t2 * t10) / 3628800 / 11 / 12 - (t * t2 * t10) / 3628800 / 11 / 12 / 13 / 14
                a2 = t - (t * t2) / 6 + (t * t4) / 121 - (t * t2 * t4) / 5040 + (t * t4 * t4) / 362880 - \
                     (t * t10) / 3628800 / 11 + (t * t2 * t10) / 3628800 / 11 / 12 / 13 - \
                     (t4 * t10) / 3628800 / 11 / 12 / 13 / 14 / 15
                h = h + np.cos(x * a1 + y * a2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


@jit(nopython=True)
def get_h_set116(q, s, w, xmin, ymin, mag=10):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                t = i / q
                b1 = np.sin(2 * pi * pi) / (2 * pi * pi)
                b2 = 2 * np.sin(2 * pi * pi) / pi
                pwpi2 = pi * pi
                f1 = -4 * pi * np.cos(t) / (4 * pwpi2 - 1) + 4 * pi * np.cos(2 * t) / (4 * pwpi2 - 4) - \
                     4 * pi * np.cos(3 * t) / (4 * pwpi2 - 9) + 4 * pi * np.cos(4 * t) / (4 * pwpi2 - 16) - \
                     4 * pi * np.cos(5 * t) / (4 * pwpi2 - 25) + 4 * pi * np.cos(6 * t) / (4 * pwpi2 - 36) - \
                     4 * pi * np.cos(7 * t) / (4 * pwpi2 - 49)
                f2 = -np.sin(t) / (4 * pwpi2 - 1) + 2 * np.sin(2 * t) / (4 * pwpi2 - 4) - \
                     3 * np.sin(3 * t) / (4 * pwpi2 - 9) + 4 * np.sin(4 * t) / (4 * pwpi2 - 16) - \
                     5 * np.sin(5 * t) / (4 * pwpi2 - 25) + 4 * np.sin(6 * t) / (4 * pwpi2 - 36) - \
                     5 * np.sin(7 * t) / (4 * pwpi2 - 49)
                h = h + np.cos(x * (b1 + b1 * f1) + y * b2 * f2)
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set


# 对h变换后直接得到k mtd=1
@jit(nopython=True)
def get_k_set0(q, s, w, xmin, ymin, tp=0):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    k_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + 5 * np.cos(x * coslist[i] + y * sinlist[i])
            k = abs(h)
            k = np.divmod(k, 16)[1]
            k_set[ny][nx] = k

    return k_set


@jit(nopython=True)
def get_k_set1(q, s, w, xmin, ymin, tp=0):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    k_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            if h < 0:
                h1 = np.abs(h)
            elif h >= 0:
                h1 = h + h1
            k = np.divmod(h1, 16)[1]
            k_set[ny][nx] = k

    return k_set


# 直接生成color_set mtd=2
@jit(nopython=True)
def get_color_set0(q, s, w, xmin, ymin):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * np.pi
    ymax = ymin + s * np.pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    color_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)
    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    kn = 0.05
    pw2kn = np.power(2, kn)

    Se1 = int(random.random() * 255 + 1)
    Se2 = int(random.random() * 255 + 1)
    Se3 = int(random.random() * 255 + 1)

    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
            t = np.log(np.abs(100 * h + 1e-6)) * pw2kn
            R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * t), 512)[1] - 256))
            G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * t), 512)[1] - 256))
            B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * t), 512)[1] - 256))
            if R > 255:
                R = 255
            if G > 255:
                G = 255
            if B > 255:
                B = 255

            color_set[ny][nx] = B * 1e6 + G * 1e3 + R

    return color_set


@jit(nopython=True)
def get_color_set1(q, s, w, xmin, ymin):
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * np.pi
    ymax = ymin + s * np.pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    color_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)
    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    kn = 0.05
    pw2kn = np.power(2, kn)

    Se1 = int(random.random() * 255 + 1)
    Se2 = int(random.random() * 255 + 1)
    Se3 = int(random.random() * 255 + 1)

    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
            Sinh = np.sin(h)
            Cosh = np.cos(h)
            R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * np.exp(2 * Sinh + 1e-6) * kn), 512)[1]
                                 - 256))
            G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * np.exp(3 * Cosh + 1e-6) * kn), 512)[1]
                                 - 256))
            B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * np.exp(4 * Sinh + 1e-6) * kn), 512)[1]
                                 - 256))
            if R > 255:
                R = 255
            if G > 255:
                G = 255
            if B > 255:
                B = 255

            color_set[ny][nx] = B * 1e6 + G * 1e3 + R

    return color_set


# 函数索引数组
list_of_get_h_set = [get_h_set0, get_h_set1, get_h_set2, get_h_set3, get_h_set4, get_h_set5, get_h_set6, get_h_set7,
                     get_h_set8, get_h_set9, get_h_set10, get_h_set11, get_h_set12, get_h_set13, get_h_set14,
                     get_h_set15, get_h_set16, get_h_set17, get_h_set18, get_h_set19, get_h_set20, get_h_set21,
                     get_h_set22, get_h_set23, get_h_set24, get_h_set25, get_h_set26, get_h_set27, get_h_set28,
                     get_h_set29, get_h_set30, get_h_set31, get_h_set32, get_h_set33, get_h_set34, get_h_set35,
                     get_h_set36, get_h_set37, get_h_set38, get_h_set39, get_h_set40, get_h_set41, get_h_set42,
                     get_h_set43, get_h_set44, get_h_set45, get_h_set46, get_h_set47, get_h_set48, get_h_set49,
                     get_h_set50, get_h_set51, get_h_set52, get_h_set53, get_h_set54, get_h_set55, get_h_set56,
                     get_h_set57, get_h_set58, get_h_set59, get_h_set60, get_h_set61, get_h_set62, get_h_set63,
                     get_h_set64, get_h_set65, get_h_set66, get_h_set67, get_h_set68, get_h_set69, get_h_set70,
                     get_h_set71, get_h_set72, get_h_set73, get_h_set74, get_h_set75, get_h_set76, get_h_set77,
                     get_h_set78, get_h_set79, get_h_set80, get_h_set81, get_h_set82, get_h_set83, get_h_set84,
                     get_h_set85, get_h_set86, get_h_set87, get_h_set88, get_h_set89, get_h_set90, get_h_set91,
                     get_h_set92, get_h_set93, get_h_set94, get_h_set95, get_h_set96, get_h_set97, get_h_set98,
                     get_h_set99, get_h_set100, get_h_set101, get_h_set102, get_h_set103, get_h_set104, get_h_set105,
                     get_h_set106, get_h_set107, get_h_set108, get_h_set109, get_h_set110, get_h_set111, get_h_set112,
                     get_h_set113, get_h_set114, get_h_set115, get_h_set116]

list_of_get_color_set = [get_color_set0, get_color_set1]

list_of_get_k_set = [get_k_set0, get_k_set1]
