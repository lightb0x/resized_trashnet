import os
import constants
import numpy as np
from PIL import Image, ExifTags


def fileWalk(directory, destPath):
    try:
        os.makedirs(destPath)
    except OSError:
        if not os.path.isdir(destPath):
            raise

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if len(file) <= 4 or file[-4:] != '.jpg':
                continue

            pic = Image.open(os.path.join(subdir, file))
            # direction = pic.getexif()[orientation]

            w, h = pic.size
            if h > w:
                off = (h - w) / 2
                pic = pic.crop((0, off, w, w + off))
            else:
                off = (w - h) / 2
                pic = pic.crop((off, 0, h + off, h))

            if not constants.RGB:
                pic = pic.convert("L")

            pic = pic.resize((constants.DIM, constants.DIM),
                             resample=Image.ANTIALIAS)

            filename = os.path.splitext(file)[0]
            pic.save(os.path.join(destPath, filename + '.png'))


def main():
    prepath = os.path.join(os.getcwd(), 'dataset-original')
    glassDir = os.path.join(prepath, 'glass')
    paperDir = os.path.join(prepath, 'paper')
    cardboardDir = os.path.join(prepath, 'cardboard')
    plasticDir = os.path.join(prepath, 'plastic')
    metalDir = os.path.join(prepath, 'metal')
    trashDir = os.path.join(prepath, 'trash')

    color = ''
    if constants.RGB:
        color = 'rgb'
    else:
        color = 'grayscale'

    # destination folder name
    destPath = os.path.join(os.getcwd(), color + str(constants.DIM))
    try:
        os.makedirs(destPath)
    except OSError:
        if not os.path.isdir(destPath):
            raise

    # GLASS
    fileWalk(glassDir, os.path.join(destPath, 'glass'))

    # PAPER
    fileWalk(paperDir, os.path.join(destPath, 'paper'))

    # CARDBOARD
    fileWalk(cardboardDir, os.path.join(destPath, 'cardboard'))

    # PLASTIC
    fileWalk(plasticDir, os.path.join(destPath, 'plastic'))

    # METAL
    fileWalk(metalDir, os.path.join(destPath, 'metal'))

    # TRASH
    fileWalk(trashDir, os.path.join(destPath, 'trash'))


if __name__ == '__main__':
    main()
