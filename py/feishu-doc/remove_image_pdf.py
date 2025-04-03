#!/usr/bin/env python

import glob
import os

source_files = glob.glob("token_pdf/token_*.pdf")
os.makedirs("token_pdf_noimg", exist_ok=True)

bad_files = set(["token_pdf_noimg/token_YJdVdZRTaoPP0uxCekhcwwlvnkf.pdf"])


def remove_image(file_path, output_path):
    cmd = "gs -o %s -sDEVICE=pdfwrite -dFILTERIMAGE %s" % (output_path, file_path)
    os.system(cmd)


for f in source_files:
    if f in bad_files:
        continue
    basename = os.path.basename(f)
    output_path = "token_pdf_noimg/" + basename
    if os.path.exists(output_path):
        print("Already processed:", f)
        continue
    remove_image(f, output_path)
