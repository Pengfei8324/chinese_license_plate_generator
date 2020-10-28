"""
generate plate numbers
"""

import numpy as np
import cv2, os
from glob import glob

# 省份
provinces = ["京", "津", "冀", "晋", "蒙", "辽", "吉", "黑", "沪",
             "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘",
             "粤", "桂", "琼", "渝", "川", "贵", "云", "藏", "陕",
             "甘", "青", "宁", "新"]

# "港", "澳", "使", "领", "学", "警", "挂"]
digits = ['{}'.format(x + 1) for x in range(9)] + ['0']

# 英文，没有I、O两个字符
letters = [chr(x + ord('A')) for x in range(26) if not chr(x + ord('A')) in ['I', 'O']]
# print('letters', digits + letters)

# 随机选取
def random_select(data):
    return data[np.random.randint(len(data))]

# 蓝牌
def generate_plate_number_blue(length=7):
    plate = random_select(provinces)
    for i in range(length - 1):
        plate += random_select(digits + letters)
    return plate

# 黄色挂车
def generate_plate_number_yellow_gua():
    plate = generate_plate_number_blue()
    return plate[:6] + '挂'

# 教练车
def generate_plate_number_yellow_xue():
    plate = generate_plate_number_blue()
    return plate[:6] + '学'

# 白色警车、军车
def generate_plate_number_white():
    plate = generate_plate_number_blue()

    if np.random.random(1) > 0.5:
        return plate[:6] + '警'
    else:
        first_letter = random_select(letters)
        return first_letter + plate[1:]


def generate_plate_number_black_gangao():
    plate = generate_plate_number_blue()
    return '粤' + plate[1:6] + random_select(["港", "澳"])


def generate_plate_number_black_ling():
    plate = generate_plate_number_blue()
    return plate[:6] + '领'


def generate_plate_number_black_shi():
    plate = generate_plate_number_blue()
    return '使' + plate[1:]


def board_bbox(polys):
    x1, y1 = np.min(polys, axis=0)
    x2, y2 = np.max(polys, axis=0)

    return [x1, y1, x2, y2]

if __name__ == '__main__':
    pass