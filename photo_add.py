from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data is not None:
            exif_info = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                exif_info[tag_name] = value

            return exif_info
        else:
            print("Exif information not found.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def get_datetime_and_camera(exif_info):
    datetime_original = None
    camera_name = None

    if exif_info is not None:
        if 'DateTimeOriginal' in exif_info:
            datetime_original = exif_info['DateTimeOriginal']

        if 'Make' in exif_info and 'Model' in exif_info:
            make = exif_info['Make']
            model = exif_info['Model']
            camera_name = f"{make} {model}"

    return datetime_original, camera_name

def add_text_to_image(image_path, text, position=(10, 10), font_size=20):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Specify the font and size
        font = ImageFont.load_default() if font_size is None else ImageFont.truetype("arial.ttf", font_size)

        # Add text to the image
        draw.text(position, text, fill="white", font=font)

        # Save the image
        image.save("data/12.JPG")
        print("Text added, and the image is saved.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "base_data/13.jpg"
    #途中
    exif_info = get_exif_data(image_path)
    datetime_original, camera_name = get_datetime_and_camera(exif_info)
    text = f"Shooting Date: {datetime_original}\nCamera name: {camera_name}\nPhotographer : kazuma1112"
    add_text_to_image(image_path, text, font_size=30)  # Specify the desired font size
