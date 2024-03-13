from PIL import Image


def image_to_1024(in_file, out_file):
    image = Image.open(in_file)
    x, y = image.size
    target_x_scale = 1024 / x
    target_y_scale = 1024 / y
    new_x, new_y = int(target_x_scale * x), int(target_y_scale * y)
    new_image = image.resize((new_x, new_y))
    new_image.save(out_file)


if __name__ == '__main__':
    import sys

    from pathlib import Path

    if len(sys.argv) != 2:
        print('Usage: %s INPUT_IMAGE.png' % sys.argv[0])
        exit(0)

    pic_in = sys.argv[1]
    pic_in_path = Path(pic_in)
    suffix = pic_in_path.suffix
    if suffix != '.png':
        print('Only png images are supported')
        exit(0)

    filename = pic_in_path.stem
    filename_1024 = filename + "_1024" + suffix
    image_to_1024(pic_in_path, filename_1024)
