# -*- coding: utf-8 -*-
import os
import shutil


def split_dataset(abs_dirname, N):
    """Move files into subdirectories. N files per subdirectory"""
    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]
    i = 0
    for f in files:
        # create new subdirectory if necessary
        if i % N == 0:
            sub_dir = os.path.join(abs_dirname, '{0:03d}'.format((i // N) + 1))
            os.mkdir(sub_dir)
        # move file to the current subdirectory
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(sub_dir, f_base))
        i += 1
