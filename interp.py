import numpy as np
import matplotlib.pyplot as plt


def lin_interp_lists(x_, x, y):
    q = []
    for z in x_:
        xL = max([m for m in x if m <= z])
        xR = min([m for m in x if m > z])
        yL = y[x.index(xL)]
        yR = y[x.index(xR)]
        q.append((yR - yL) * (z - xL) / (xR - xL) + yL)
    return q


def lin_interp(x_, x, y):
    ix = ((x_[None, :] - x[:-1, None]) * (x_[None, :] - x[1:, None])).argmin(axis=0)
    return (y[ix+1] - y[ix])/(x[ix+1] - x[ix]) * (x_ - x[ix]) + y[ix]


if __name__ == '__main__':
    x = np.asarray([1, 2, 4, 7, 8, 10])
    y = np.asarray([_**2 for _ in x])
    x_ = np.arange(2, 10)

    y_ = lin_interp(x_, x, y)

    fig, ax = plt.subplots()
    ax.plot(x_, y_, 'o', label='interpolated')
    ax.plot(x_, x_ ** 2, label='function')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel(r'$y=x^2$')
    plt.show(block=True)