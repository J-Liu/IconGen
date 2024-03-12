from PIL import Image


def image_reduce(in_file, out_file, target_scale):
    image = Image.open(in_file)
    x, y = image.size
    new_x, new_y = int(target_scale * x), int(target_scale * y)
    new_image = image.resize((new_x, new_y))
    new_image.save(out_file)
