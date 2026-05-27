#!/usr/bin/env python
# coding: utf-8

# Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
# License: Apache License, Version 2.0

import psutil


def main():
    cpu_temp = get_cpu_temperature()
    cpu_usage = get_cpu_usage()
    print(f'{round(cpu_temp):2} °C | {round(cpu_usage):2} %')


def get_cpu_temperature():
    temps = psutil.sensors_temperatures()

    for name, entries in temps.items():
        if name in ['k10temp', 'coretemp']:
            cpu_temp = entries[0].current
            break

    return float(cpu_temp)


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1.0)
    return float(cpu_usage)


if __name__ == '__main__':
    main()
