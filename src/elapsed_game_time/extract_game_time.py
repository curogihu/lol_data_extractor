import numpy as np
import cv2
import os
from glob import glob
from tqdm import tqdm
# 680, 50, 40, 15

def main():
    # pass

    img_file_paths = glob('../../images/base/*.jpg')

    for img_file_path in tqdm(img_file_paths):
        img = cv2.imread(img_file_path)
        # base_file_name = os.path.splitext(os.path.basename(img_file_path))[0]
        base_file_name = os.path.basename(img_file_path)

        # print('img: ', img)
        # print('base_file_name: ', base_file_name)

        extract_img = img[50:65, 680:720]

        cv2.imwrite(f'../../images/elapsed_game_time/{base_file_name}', extract_img)

        # exit()


if __name__ == '__main__':
    main()