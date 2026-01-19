#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: BSD-3-Clause

import os
import subprocess
import sys
import time
from urllib.request import urlretrieve


def main():
    if len(sys.argv) == 1 or \
            sys.argv[1][-4:] == 'help' or \
            sys.argv[1] == '-h':
        print('Usage: python mpv_shader_benchmark.py <shaders>')
        sys.exit()

    # "Aerial view of a boat sailing in the sea" by Burak Evlivan
    # https://www.pexels.com/video/aerial-view-of-a-boat-sailing-in-the-sea-28478483/
    # "12393381_3840_2160_60fps_480.mp4" is resized to 854:480.
    if os.path.exists('12393381_3840_2160_60fps_480.mp4') is False:
        download_file(
            'http://linuxplayers.g1.xrea.com/images/mpv/' +
            '12393381_3840_2160_60fps_480.mp4',
            '12393381_3840_2160_60fps_480.mp4')

    results = {}
    result = run_mpv('')
    results['Lanczos'] = result[1]

    shaders = sys.argv[1:]

    for shader in shaders:
        result = run_mpv(shader)
        results[result[0]] = result[1]

    # Convert to list sorted by value
    results = sorted(results.items(), key=lambda x: x[1])

    print('| Upscaler | Time (sec) |')
    print('| --- | --- |')

    for result in results:
        print(f'| {result[0]} | {result[1]} |')


def run_mpv(shader):
    start_time = time.time()

    subprocess.run(
        ['mpv', '--audio=no', '--untimed=yes',
            '--video-sync=display-desync', '--vulkan-swap-mode=immediate',
            '--opengl-swapinterval=0', '--scale=lanczos',
            f'--glsl-shaders={shader}', '--fs',
            '12393381_3840_2160_60fps_480.mp4'],
        check=True)

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    shader = shader.split('/')[-1]
    shader = '.'.join(shader.split('.')[:-1])

    return (shader, elapsed_time)


def download_file(url, save_path):
    try:
        urlretrieve(url, save_path)
        print(f"File downloaded successfully to {save_path}")
    except Exception as exception:
        print(f"Error downloading file: {exception}")
        sys.exit()


if __name__ == '__main__':
    main()
