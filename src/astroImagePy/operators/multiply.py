import numpy as np


def multiply(rgb1: np.ndarray, rgb2: np.ndarray, limit=False) -> np.ndarray:
    result = np.multiply(rgb1, rgb2)
    if limit:
        result = np.clip(result, 0, 255)
    return result.astype(int)
