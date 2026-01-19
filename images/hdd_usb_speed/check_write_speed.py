#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: Apache License, Version 2.0

import argparse
import shutil
import time


def main():
    parser = argparse.ArgumentParser(
        description='Check write speed')
    parser.add_argument(
            'directory', metavar='D', nargs='+',
            help='specify a directory')
    args = parser.parse_args()

    dir_place = args.directory[0]
    interval = 2
    dir_size_prev = -1

    while True:
        # ディレクトリのサイズを確認し、bytes を MB に変換
        dir_size = shutil.disk_usage(dir_place).used / (1024 ** 2)
        dir_size = int(dir_size)

        if dir_size_prev == -1:
            dir_size_prev = dir_size
            time.sleep(interval)
            continue

        if dir_size - dir_size_prev <= 0:
            print('0 MB/s write')
            time.sleep(interval)
            continue

        # ディレクトリの増加サイズを interval で割って速度を計算
        write_speed = (dir_size - dir_size_prev) / interval
        write_speed = round(write_speed, 2)

        # 1 TBの書き込みに何時間かかるか計算
        time_to_1tb = (1024 ** 2) / (write_speed * (60 ** 2))
        time_to_1tb = round(time_to_1tb, 2)

        print(
            f'{write_speed} MB/s write, ' +
            f'{time_to_1tb} hrs to write 1 TB')

        dir_size_prev = dir_size
        time.sleep(interval)


if __name__ == '__main__':
    main()
