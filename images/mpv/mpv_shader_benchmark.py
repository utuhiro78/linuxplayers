#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: BSD-3-Clause

import subprocess
import sys
import time
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print('Usage: python mpv_shader_benchmark.py <movie>')
        sys.exit()

    movie_file = sys.argv[1]
    results = {}

    shader_file = ""
    result = run_mpv(shader_file, movie_file)
    results['lanczos'] = result[1]

    shader_dir = Path("~/.config/mpv/shaders").expanduser()
    shader_files = list(shader_dir.glob("*"))

    for shader_file in shader_files:
        shader_name, elapsed_time = run_mpv(shader_file, movie_file)
        results[shader_name] = elapsed_time

    # Sort by elapsed_time
    results = sorted(results.items(), key=lambda x: x[1])

    print('Upscaler | Time (sec)')
    print('-- | --')

    for result in results:
        shader_name, elapsed_time = result
        print(f'{shader_name} | {elapsed_time}')


def run_mpv(shader_file, movie_file):
    start_time = time.time()

    mpv_options = '--no-config --load-scripts=no --no-osc ' + \
        '--window-scale=2.0 --audio=no --untimed=yes ' + \
        '--video-sync=display-desync --vulkan-swap-mode=immediate ' + \
        '--opengl-swapinterval=0 --wayland-internal-vsync=no'

    mpv_options = mpv_options.split()

    subprocess.run(
        ['mpv', *mpv_options, f'--glsl-shaders={shader_file}',
            movie_file],
        check=True)

    end_time = time.time()

    elapsed_time = round(end_time - start_time, 2)
    shader_name = Path(shader_file).stem

    return (shader_name, elapsed_time)


if __name__ == '__main__':
    main()
