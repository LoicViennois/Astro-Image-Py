from typing import List

import numpy as np


def median_one(rgb: np.ndarray) -> np.ndarray:
    median_pixel = np.median(rgb, axis=(0, 1))
    zeros = np.zeros(rgb.shape)
    result = zeros + median_pixel
    return result.astype(int)


def median(rgbs: List[np.ndarray]) -> np.ndarray:
    concat = np.array(rgbs)
    result = np.median(concat, axis=0)
    return result.astype(int)
