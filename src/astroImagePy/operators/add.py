from typing import List

import numpy as np


def add(rgbs: List[np.ndarray], limit=False) -> np.ndarray:
    result = np.add.reduce(rgbs)
    if limit:
        result = np.clip(result, 0, 255)
    return result.astype(int)
