from pathlib import Path

from PIL import Image


def image_reduce(in_file, out_file, target_scale):
    image = Image.open(in_file)
    x, y = image.size
    new_x, new_y = int(target_scale * x), int(target_scale * y)
    new_image = image.resize((new_x, new_y))
    new_image.save(out_file)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: %s 1024_size_file.png' % sys.argv[0])
        exit(0)

    pic_1024 = sys.argv[1]
    pic_1024_path = Path(pic_1024)
    suffix = pic_1024_path.suffix
    if suffix != '.png':
        print('Only png images are supported')
        exit(0)

    filename = pic_1024_path.stem
    if filename.startswith("1024_"):
        filename = filename[5:]
    if filename.endswith("_1024"):
        filename = filename[:-5]
    filename_512 = filename + "_512" + suffix
    image_reduce(pic_1024, filename_512, 0.5)
    filename_256 = filename + "_256" + suffix
    image_reduce(pic_1024, filename_256, 0.25)
    filename_128 = filename + "_128" + suffix
    image_reduce(pic_1024, filename_128, 0.125)
    filename_64 = filename + "_64" + suffix
    image_reduce(pic_1024, filename_64, 0.0625)
    filename_32 = filename + "_32" + suffix
    image_reduce(pic_1024, filename_32, 0.03125)
    filename_16 = filename + "_16" + suffix
    image_reduce(pic_1024, filename_16, 0.015625)
