from PIL import Image
import json
import datetime
import os


seq_location = "C:/Users/Saxly/Python projects/ascii_sequence/input/frames/vj_loop_v02/"
# ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_characters_by_surface = " .:-=+*#%@"

time = datetime.datetime.now()
time = str(time.strftime("%H%M"))


entries = os.listdir(seq_location)

# for entry in entries:
#     print(f'{seq_location}{entry}')


def main():

    framenr = 1

    for entry in entries:

        image = Image.open(
            f'{seq_location}{entry}')
        # you can first resize the image if needed
        # image = image.resize((100, 50))
        image = image.convert('RGB')
        ascii_art = convert_to_ascii_art(image)

        print(framenr)
        print(f'{seq_location}{entry}')
        save_as_json(ascii_art, framenr)
        framenr += 1
        # print(framenr)


def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art


def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art):
    with open(f"image_{time}.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()


def save_as_json(ascii_art, framenr):
    # print(framenr)
    text = ""
    for line in ascii_art:
        text = text + line + ('\n')

    ascii_entry = {
        "frameNumber": framenr,
        "frame": ascii_art
    }

    jsonObject = json.dumps(ascii_entry, indent=4)

    with open("looped_seq.json", "r+") as jsonfile:

        # First we load existing data into a dict.
        file_data = json.load(jsonfile)
        # Join new_data with file_data inside emp_details
        file_data["animation"].append(ascii_entry)
        # Sets file's current position at offset.
        jsonfile.seek(0)
        # convert back to json.
        json.dump(file_data, jsonfile, indent=4)

        jsonfile.write(jsonObject)


if __name__ == '__main__':
    main()
