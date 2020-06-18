import numpy as np


def divide(rgb1: np.ndarray, rgb2: np.ndarray) -> np.ndarray:
    division = np.divide(rgb1, rgb2)
    result = np.clip(division, 0, 255)
    return result.astype(int)
