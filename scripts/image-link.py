#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Haoyang <me@peterchen.xyz>
#
# Distributed under terms of the MIT license.

"""
remove github markdown image resize syntax
"""

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import os
import shutil
regex = r"\ \=\d{1,}x{1}\d{1,}\)$"
subst = ")"

output_dir = 'docs'
ftype = '.md'
rtype = ('.png', '.jpeg', '.jpg')
for path, _, files in os.walk('raw'):
    for fname in files:
        sub_dir = output_dir + "/" + path.split("/")[1]
        # print(sub_dir)
        if not os.path.exists(sub_dir):
             os.makedirs(sub_dir)
        if fname.endswith(rtype):
            resouces_dir = sub_dir + '/resources/'
            if not os.path.exists(resouces_dir):
                os.makedirs(resouces_dir)
            shutil.copy(path + "/" + fname, resouces_dir)
        if not fname.endswith(ftype):
            continue
        with open(os.path.join(sub_dir, fname), 'w') as o:
            with open(os.path.join(path, fname), 'r') as f:
                for line in f:
                    o.write(re.sub(regex, subst, line, 0, re.MULTILINE))

# You can manually specify the number of replacements by changing the 4th argument

