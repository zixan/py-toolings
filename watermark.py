import argparse
from PIL import Image

def load_watermark_image(watermark_image_filename):
    watermark_image = Image.open(watermark_image_filename)
    watermark_image.putalpha(1)
    watermark_image_width = watermark_image.size[0]
    watermark_image_height = watermark_image.size[1]
    return (watermark_image, watermark_image_width, watermark_image_height)

def resize_image(image):
    current_width, current_height = image.size
    new_width = 500
    new_height = new_width*(current_height/current_width)
    return image.resize((new_width, new_height))

def watermark(image_filename, watermark_image_filename):
    watermark_image, watermark_image_width, watermark_image_height = load_watermark_image(watermark_image_filename=watermark_image_filename)
    im = Image.open(image_filename)
    im = resize_image(image=im)
    width = im.size[0]
    height = im.size[1]
    left = 10
    top = (height / 2) - (watermark_image_height / 2)
    right = watermark_image_width + 10
    bottom = top + watermark_image_height
    box = (left, top, right, bottom)
    im.paste(watermark_image, box)
    watermarked_image_filename = 'pid-{}'.format(image_filename)
    im.save(watermarked_image_filename)

def main():
    parser = argparse.ArgumentParser(
        description="watermark an image")
    parser.add_argument("--base_image", required=True,
        help="base image to be watermarked")
    parser.add_argument("--watermark_image", required=True,
        help="watermark image")
    args = parser.parse_args()

    image_filename = args.base_image
    watermark_image_filename = args.watermark_image
    watermark(image_filename=image_filename, watermark_image_filename=watermark_image_filename)

if __name__ == '__main__':
    main()
