import numpy as np
import matplotlib.pyplot as plt
from interp import lin_iterp
from scipy.signal import convolve


def b(x):
    """bandwidth as a function of frequency
    """
    return 1.25  - np.exp(np.mod(x/10, 1))
    

def cbw(f, b, h):
    """transform f such that the bandwidth is constant in the transformed domain
    f (np.ndarray) : the original frequencies
    b (callable) : the bandwidth function
    h (np.ndarray) : the amplitude of the spectrum
    """
    c = np.cumsum(b(f))
    c = (c - c.min()) / (c.max() - c.min())
    # interpolate in the original domain
    return c, lin_interp(c, f, h)


def conv(h):
    g = np.asarray([np.exp(-u ** 2/2) / np.sqrt(np.pi) for u in np.arange(-5, 6)]) # kernel here
    return convolve(h, g)

def inv_cbw(f, c, h):
    """inverse transform the frequencies to their original domain
    f  : the target frequencies
    c  : the transform
    """
    return lin_interp(c, f, h)


x = np.linspace(0, 25, 2501)
h = np.random.exponential(size=x.shape)

fig, ax = plt.subplots(1, 2, sharey=True, squeeze=True)
ax[0].plot(x, h)
ax[0].set_xlabel('frequency')
ax[0].set_ylabel('bandwidth')

