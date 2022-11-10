import random
import numpy as np
from PIL import Image

# numpyで色の配列をつくる H:色相、S:彩度、V:明度の三次元
# randomで数値を取得
# 配列から画像を生成


def random_color_make():
    value = random.randint(0, 255)
    line_data = np.full(256, value)

    hue = np.tile(
        line_data, (256, 1)
    )  # 255x255の2次元配列を生成 [0,1..,254,255],[0,1..,254,255]
    sat = np.transpose(hue)  # hueの配列の行と列を入れ替え [0 0],[1,1],[254,254],[255,255]
    val = np.full_like(
        hue, 255
    )  # hueと同じ構造とデータ型を生成 [255,255],[255,255]..,[255,255],[255,255]

    mat = np.stack([hue, sat, val], 2)  # 3つの2次元配列を結合して3次元配列にする axisで結合の階層を指定
    images = Image.fromarray(np.uint8(mat), "HSV")  # HSVのデータを読み込む
    images_rgb = images.convert("RGB")  # HSVからRGBに変換

    images_rgb.show()
    return images_rgb.save("images/random_color.png")
