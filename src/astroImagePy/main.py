import glob
import os
import shutil
import sys

from astroImagePy.functions import median_divide
from astroImagePy.operators import median, mean, substract
from astroImagePy.reader import read
from astroImagePy.writer import write


def main(working_folder: str):
    # Prepare folders
    master_folder = os.path.join(working_folder, 'master')
    if os.path.exists(master_folder):
        shutil.rmtree(master_folder)
    os.makedirs(master_folder)
    output_path = os.path.join(working_folder, 'output.png')
    if os.path.exists(output_path):
        os.remove(output_path)

    # Get paths
    offsets_path = glob.glob(os.path.join(working_folder, 'offset', '*.png'))
    darks_path = glob.glob(os.path.join(working_folder, 'dark', '*.png'))
    flats_path = glob.glob(os.path.join(working_folder, 'flat', '*.png'))
    images_path = glob.glob(os.path.join(working_folder, 'image', '*.png'))

    # Build master offset
    print('==== BUILDING MASTER OFFSET ====')
    if len(offsets_path) > 0:
        offsets = read(offsets_path)
        master_offset = median(offsets)
        write(master_offset, os.path.join(master_folder, 'master_offset.png'))
        del offsets
    else:
        print('No offset found, ignoring master offset\n')
        master_offset = None

    # Build master dark
    print('==== BUILDING MASTER DARK ====')
    if len(darks_path) > 0:
        darks = read(darks_path)
        master_dark = substract(median(darks), master_offset)
        write(master_dark, os.path.join(master_folder, 'master_dark.png'))
        del darks
    else:
        print('No dark found, ignoring master dark\n')
        master_dark = None

    # Build master flat
    print('==== BUILDING MASTER FLAT ====')
    if len(flats_path) > 0:
        flats = read(flats_path)
        master_flat = substract(median(flats), master_offset)
        write(master_flat, os.path.join(master_folder, 'master_flat.png'))
        del flats
    else:
        print('No flat found, ignoring master flat\n')
        master_flat = None

    # Build master image
    print('==== BUILDING MASTER IMAGE ====')
    images = read(images_path)
    master_image = substract(mean(images), master_offset)
    write(master_image, os.path.join(master_folder, 'master_image.png'))
    del images

    # Build final image
    print('==== BUILDING FINAL IMAGE ====')
    final_image = median_divide(substract(master_image, master_dark), master_flat)
    write(final_image, output_path)

    print('DONE')


if __name__ == '__main__':
    main(sys.argv[1])
