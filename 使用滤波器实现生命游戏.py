import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

random_board = np.random.randint(0, 2, size=(100, 100))

def frash(values):
    center = values[len(values) // 2]
    neighbors = np.sum(values) - center
    if neighbors == 3 or (center and neighbors == 2):
        return 1.
    else:
        return 0.

def update(frames, img, board):
    newBoard = ndi.generic_filter(board, frash, size=3, mode='wrap')
    img.set_data(newBoard)
    board[:] = newBoard[:]
    return img

fig, ax = plt.subplots()
img = ax.imshow(random_board)
ani = FuncAnimation(fig, update, fargs=(img, random_board), interval=5, save_count=50)
plt.show()