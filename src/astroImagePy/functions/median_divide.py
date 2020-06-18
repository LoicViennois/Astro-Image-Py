import numpy as np

from astroImagePy.operators import multiply, divide, median_one


def median_divide(rgb: np.ndarray, flat: np.ndarray) -> np.ndarray:
    if flat is None:
        return rgb
    result = divide(multiply(rgb, median_one(flat)), flat)
    return result
