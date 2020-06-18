from typing import List

import imageio
import numpy as np


def read_one(path) -> np.ndarray:
    rgb = imageio.imread(path)
    return rgb.astype(int)


def read(images: List[str]) -> List[np.ndarray]:
    rgbs = []
    for k, img_path in enumerate(images):
        rgbs.append(read_one(img_path))
        print('[IN] %d/%d Image read from %s' % (k + 1, len(images), img_path))

    return rgbs
