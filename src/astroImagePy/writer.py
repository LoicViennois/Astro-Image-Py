import imageio
import numpy as np


def write(rgb: np.ndarray, path: str):
    rgb8 = rgb.astype('uint8')
    imageio.imsave(path, rgb8)
    print('[OUT] Image written to ' + path + '\n')
