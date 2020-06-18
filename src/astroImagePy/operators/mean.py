from typing import List

import numpy as np


def mean(rgbs: List[np.ndarray]) -> np.ndarray:
    result = np.add.reduce(rgbs) / len(rgbs)
    return result.astype(int)
