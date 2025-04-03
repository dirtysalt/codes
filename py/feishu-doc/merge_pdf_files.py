#!/usr/bin/env python

import glob
import os
import shutil

source_files = glob.glob("token_pdf_noimg/token_*.pdf")

CUT_SIZE = 25 * (1 << 20)
buf_files = []
buf_size = 0
buf_idx = 0

DIR = "token_pdf_merged"

shutil.rmtree(DIR, ignore_errors=True)
os.makedirs(DIR, exist_ok=True)


def merge_files(files, output):
    if files:
        cmd = "pdftk %s cat output %s" % (" ".join(files), output)
        print(cmd)
        os.system(cmd)


large_files = []

for f in source_files:
    # get file size
    size = os.path.getsize(f)
    if size * 2 > CUT_SIZE:
        large_files.append(f)
        continue
    buf_files.append(f)
    buf_size += size
    if buf_size > CUT_SIZE:
        merge_files(buf_files, DIR + "/aa_merged_%02d" % buf_idx + ".pdf")
        buf_files = []
        buf_size = 0
        buf_idx += 1

merge_files(buf_files, DIR + "/aa_merged_%02d" % buf_idx + ".pdf")
buf_idx += 1

for f in large_files:
    shutil.copy(f, DIR + "/" + os.path.basename(f))
