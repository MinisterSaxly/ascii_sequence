from PIL import Image
import json
import datetime

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
time = datetime.datetime.now()
time = str(time.strftime("%H%M"))


def main():
    image = Image.open(
        'https://raw.githubusercontent.com/MinisterSaxly/ascii_sequence/master/seq_0213.json')
    # you can first resize the image if needed
    image = image.resize((100, 50))
    ascii_art = convert_to_ascii_art(image)
    save_as_text(ascii_art)
    save_as_json(ascii_art)


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


def save_as_json(ascii_art):

    text = ""
    for line in ascii_art:
        text = text + line + ('<br>')

    ascii_seq = {
        "1": text
    }

    jsonObject = json.dumps(ascii_seq, indent=4)

    with open(f"seq_{time}.json", "w") as jsonfile:
        jsonfile.write(jsonObject)


if __name__ == '__main__':
    main()
