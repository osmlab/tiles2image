#!/usr/bin/env python3
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("zoom", type=int, help = "Zoom level of tiles")
parser.add_argument("filename", help = "Name of PNG to write to")
args = parser.parse_args()

img = Image.new('1', (2**args.zoom, 2**args.zoom), "black")
pixels = img.load()

for line in sys.stdin.readlines():
    # Standard z/x/y format
    splitline=line.split('/',4)
    if (splitline[0] != str(args.zoom)):
        raise ValueError("Line {} does not have zoom {}".format(line, args.zoom))
    x = int(splitline[1])
    y = int(splitline[2])
    pixels[x,y] = 1

img.save(args.filename)