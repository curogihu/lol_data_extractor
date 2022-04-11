from glob import glob
import os


def main():
    file_paths = glob('../../images/elapsed_game_time/*.jpg')

    print(len(file_paths))

    for file_path in file_paths:
        print('file_path:', os.path.basename(file_path), ', elapsed_date: 00:00')


if __name__ == '__main__':
    main()