import matplotlib.pyplot as plt
import matplotlib.animation as anim
from random import random

def noise(w, h):
    return [[random() < 0.5 for _ in range(w)] for _ in range(h)]

def new_state(i, j, pre):
    n_neighbors = \
            pre[(i-1)%h][(j-1)%w] + pre[(i-1)%h][j] + pre[(i-1)%h][(j+1)%w] \
            + pre[i][(j-1)%w] + pre[i][(j+1)%w] \
            + pre[(i+1)%h][(j-1)%w] + pre[(i+1)%h][j] + pre[(i+1)%h][(j+1)%w]
        
    if pre[i][j]:
        return n_neighbors == 2 or n_neighbors == 3
    else:
        return n_neighbors == 3

w, h = 100, 100
pre = noise(w, h)
fut = [[False for _ in range(w)] for _ in range(h)]

fig, ax = plt.subplots()
grid = ax.imshow(pre, cmap="gray")
plt.xticks([])
plt.yticks([])

def update(frame):
    global pre, fut
    for i in range(h):
        for j in range(w):
            fut[i][j] = new_state(i, j, pre)
    
    pre, fut = fut, pre
    grid.set_data(pre)
    return (grid)
    
ani = anim.FuncAnimation(fig=fig, func=update, frames=300, interval=10)
anim.Animation.save(ani, "./conway.gif")
# plt.show()