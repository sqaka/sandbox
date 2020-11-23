#!.venv/bin/python3

import cv2
import glob
import numpy as np
import re

import click


TMP_FOLDER_PATH = "./tmp/"
MTX_PATH = TMP_FOLDER_PATH + "mtx.csv"
DIST_PATH = TMP_FOLDER_PATH + "dist.csv"
SAVE_FOLDER_PATH = "./undist_image"


def calibrateImage(imdir):
    '''make undistortion'''
    mtx, dist = loadCalibrationFile(MTX_PATH, DIST_PATH)

    for fname in glob.glob("{}/*".format(imdir)):
        img = cv2.imread(fname)
        # let undistortion using params
        resultImg = cv2.undistort(img, mtx, dist, None)
        saveImg(SAVE_FOLDER_PATH, fname, imdir, resultImg)


def loadCalibrationFile(mtx_path, dist_path):
    '''read csv_params'''
    try:
        mtx = np.loadtxt(mtx_path, delimiter=',')
        dist = np.loadtxt(dist_path, delimiter=',')
    except Exception as e:
        raise e
    return mtx, dist


def saveImg(dirPath, fname, imdir, img):
    '''save images using same name'''
    fname = re.sub('{}'.format(imdir), '', fname)
    fname = re.sub('/', '/undist_', fname)
    path = dirPath + fname
    cv2.imwrite(path, img)
    print("saved: ", path)


@click.command()
@click.option('--imdir', type=str, default='calib_image')
def main(imdir):
    calibrateImage(imdir)


if __name__ == '__main__':
    main()
