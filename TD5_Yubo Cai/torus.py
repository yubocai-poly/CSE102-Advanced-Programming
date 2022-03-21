"""
Yubo Cai
CSE102
Tutorial_5
"""
import random


def torus_volume_cuboid(R, r, N=100000):

    c = 0
    for _ in range(N):
        xr = random.uniform(-R - r, R + r)
        yr = random.uniform(-R - r, R + r)
        zr = random.uniform(-r, r)

        left = (((xr**2 + yr**2)**0.5) - R)**2 + zr**2
        right = r**2
        if left <= right:
            c += 1

    Ab = (2 * R + 2 * r) * (2 * R + 2 * r) * 2 * r

    return Ab * (c / N)


print(torus_volume_cuboid(10, 2))
""" 
这个就是用随机点估计法来求体积，一个圆环包裹在由相应的长宽高组成的方体，随机生成坐标点，
如果坐标点满足不等式关系说明点在圆环里面，然后大量的生成，看生成比例来估计
"""
