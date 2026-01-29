#!/usr/bin/python
# -*- coding:utf-8 -*-

import glob
import os
import subprocess
import time


def main():
    files = glob.glob('*.md')
    files_mtime = {}

    for file in files:
        # {file: mtime} の dictionary を作成
        files_mtime[file] = os.path.getmtime(file)

    # 最新の3個を起動時にアップデート
    # list を作成して key でソート
    files_latest = sorted(files_mtime.items(), key=lambda x: x[1])
    files_latest = files_latest[0:]

    # files_latest の例
    #     [('mpv_01.md', 1732313157.6537077),
    #     ('arch_linux_01.md', 1732358436.509328)]
    for file in files_latest:
        update_html(file[0])

    while True:
        for file in files:
            mtime = os.path.getmtime(file)

            if files_mtime[file] == mtime:
                continue

            print(f'Update {file.replace('.md', '.html')}')
            files_mtime[file] = mtime
            update_html(file)

        time.sleep(1)


def update_html(file):
    subprocess.run(
        ['./pandoc',
            '-s',
            '--template', 'pandoc_template.html',
            '-f', 'markdown+hard_line_breaks',
            '-c', 'github.css',
            '--toc', '--toc-depth=3',
            file,
            '-o', file.replace('.md', '.html')])


if __name__ == '__main__':
    main()
