import cv2, os
import argparse

from generate_multi_plate import MultiPlateGenerator


def parse_args():
    parser = argparse.ArgumentParser(description='中国车牌生成器')
    parser.add_argument('--double', default=False, type=bool, help='是否双层车牌')
    parser.add_argument('--bg-color', default='blue', help='车牌底板颜色')
    parser.add_argument('--plate-number', default='云999999', help='车牌号码')
    args = parser.parse_args()
    return args


def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

if __name__ == '__main__':
    args = parse_args()
    print(args)

    generator = MultiPlateGenerator('plate_model', 'font_model')
    img = generator.generate_plate_special(args.plate_number, args.bg_color, args.double)
    cv2.imwrite('{}.jpg'.format(args.plate_number), img)
