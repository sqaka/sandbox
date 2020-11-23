#!.venv/bin/python3

import cv2
import glob
import numpy as np
import re

import click

TMP_FOLDER_PATH = "./tmp/"
MTX_PATH = TMP_FOLDER_PATH + "mtx.csv"
DIST_PATH = TMP_FOLDER_PATH + "dist.csv"


def calcCamera(square_size, pattern_size, imdir):
    '''calculate undistortion param'''
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size
    # arrays to store object points and image points from all the images
    img_points = []
    obj_points = []
 
    # read images
    for fname in glob.glob("{}/*".format(imdir)):
        im = cv2.imread(fname, 0)
        print("loading..." + fname)
        # detect corners of chessboard
        found, corner = cv2.findChessboardCorners(im, pattern_size)
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            corners = cv2.cornerSubPix(im, corner, (5, 5), (-1, -1), term)
            # save marking images
            img = cv2.drawChessboardCorners(im, pattern_size, corners, found)
            saveImg(TMP_FOLDER_PATH, fname, imdir, img)
            # sleep(0.5)
        # skip failure image
        if not found:
            print('chessboard not found')
            continue
        # append params in 2D & 3D lists
        img_points.append(corner.reshape(-1, 2))
        obj_points.append(pattern_points)
 
    # calculate undistortion param
    rms, K, d, r, t = cv2.calibrateCamera(obj_points, img_points, (im.shape[1], im.shape[0]), None, None)

    return rms, K, d


def saveImg(dirPath, fname, imdir, img):
    '''save images using same name'''
    fname = re.sub('{}'.format(imdir), '', fname)
    path = dirPath + fname
    cv2.imwrite(path, img)
    print("saved: ", path)


def outputParams(rms, K, d):
    # output undistortion param in console
    print("RMS = ", rms)
    print("K = \n", K)
    print("d = ", d.ravel())


def saveCalibrationFile(mtx, dist, mtx_path, dist_path):
    '''undistortion param -> csv_file'''
    # camera param
    np.savetxt(mtx_path, mtx, delimiter=',', fmt="%0.14f")
    # undistortion param
    np.savetxt(dist_path, dist, delimiter=',', fmt="%0.14f")


@click.command()
@click.option('--square_size', type=float, default=20.0)
@click.option('--pattern_size', type=tuple, default=(10, 7))
@click.option('--imdir', type=str, default='chart_image')
def main(square_size, pattern_size, imdir):
    rms, K, d = calcCamera(square_size, pattern_size, imdir)
    outputParams(rms, K, d)
    saveCalibrationFile(K, d, MTX_PATH, DIST_PATH)


if __name__ == '__main__':
    main()
