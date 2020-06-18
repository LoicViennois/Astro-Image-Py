import numpy as np


def substract(rgb1, rgb2) -> np.ndarray:
    if rgb2 is None:
        return rgb1.astype(int)
    subtraction = np.subtract(rgb1, rgb2)
    result = np.clip(subtraction, 0, 255)
    return result.astype(int)
