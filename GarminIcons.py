from pathlib import Path

from ImageReducer import image_reduce

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Usage: %s 1024_SIZE_FILE.png GARMIN_ICON_PIXEL_SIZE' % sys.argv[0])
        exit(0)

    pic_1024 = sys.argv[1]
    pic_1024_path = Path(pic_1024)
    suffix = pic_1024_path.suffix
    if suffix != '.png':
        print('Only png images are supported')
        exit(0)

    size = 0
    if sys.argv[2].isdigit():
        size = int(sys.argv[2])
    else:
        print('GARMIN_ICON_PIXEL_SIZE must be an integer')
        exit(0)

    scale = size / 1024

    filename = pic_1024_path.stem
    if filename.startswith("1024_"):
        filename = filename[5:]
    if filename.endswith("_1024"):
        filename = filename[:-5]

    filename_garmin_icon = filename + "_" + str(size) + suffix
    image_reduce(pic_1024, filename_garmin_icon, scale)
