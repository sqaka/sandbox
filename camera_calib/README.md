## notice
the following helpful articles : \
https://rikoubou.hatenablog.com/entry/2019/03/26/143556 \
https://qiita.com/ReoNagai/items/5da95dea149c66ddbbdd \
https://qiita.com/nonbiri15/items/5e59dea66d7733d6d6a3


## readme
- first, please take some images using chessboard and put into `/chart_image`
- if you have images to make undistortion, please put into `/calib_image`

### setup
- please run `bash setup.sh` first
- then `source .venv/bin/activate` to make enviroments

### make undistortion param
- run `python3 make_undistortion_param.py`
- option `--square_size`, type=`float`, default=`20.0`
- option `--pattern_size`, type=`tuple`, default=`(10, 7)`
- option `--imdir`, type=`str`, default=`chart_image/`


### calibrate image
- run `python3 calibrate_images.py`
- option `--imdir`, type=`str`, default=`calib_image/`

## directry
```
camera_calib
|
├── setup.sh
|── requirements.txt
├── .venv
|── make_undistortion_param.py
|── calibrate_images.py
|
|── chart_image/
|   └── (please put images using chessboard)
|
|── calib_image/
|   └── (please put images to make undistortion)
|
|── tmp/
|   |── mtx.csv
|   |── dist.csv
|   └── (generated chessboard images drawing corners)
|
└── undist_image/
    └── (generated undistotion images here)
```
