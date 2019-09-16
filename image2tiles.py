#!/usr/bin/env python3
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("zoom", type=int, help = "Zoom level of tiles")
parser.add_argument("filename", help = "Name of PNG to read from")
args = parser.parse_args()

with Image.open(args.filename) as img:
    pixels = img.load()
    for x in range(2**int(args.zoom)):
        for y in range(2**int(args.zoom)):
            if pixels[x,y] != 0:
                print("{}/{}/{}".format(args.zoom,str(x),str(y)))
