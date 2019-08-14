# tiles2image

## About

This program takes a list of tiles and turns it into a black and white image, with white pixels where there were tiles in the list. This image can then be used with other image processing software to visualize the tile list.

## Usage

```
usage: tiles2image.py [-h] zoom filename

positional arguments:
  zoom        Zoom level of tiles
  filename    Name of PNG to write to

optional arguments:
  -h, --help  show this help message and exit
```

```
usage: image2tiles.py [-h] zoom filename

positional arguments:
  zoom        Zoom level of tiles
  filename    Name of PNG to read from

optional arguments:
  -h, --help  show this help message and exit
```

## Limitations
It doesn't georeference the image

## Examples

The OSMF publishes [tile request logs](https://planet.openstreetmap.org/tile_logs/). In these examples, `tiles-2019-08-11.txt` is from that site.

```sh
# Show zoom 12 tiles
cat tiles-2019-08-11.txt | cut -f1 -d' ' | grep '^12' | ./tiles2image.py 12 z12.png

# Compare a tile list and the image turned to a tile list. This is an empty diff

diff <(cat tiles-2019-08-11.txt | cut -f1 -d' ' | grep '^12' | sort) <(./image2tiles.py 12 z12.png | sort)
```
