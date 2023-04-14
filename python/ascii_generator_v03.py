from PIL import Image
import json
import datetime
import os
import glob

seq_location = "C:/Users/Saxly/Python projects/ascii_sequence/input/frames/vj_loop_v02/"
ascii_characters_by_surface = " .:-=+*#%@"

banner = '''
                        _____                                      
 ______   _____    _____\    \  ______   _______    ____________   
|\     \ |     |  /    / |    ||\     \  \      \  /            \  
\ \     \|     | /    /  /___/| \\     \  |     /||\___/\  \\___/| 
 \ \           ||    |__ |___|/  \|     |/     //  \|____\  \___|/ 
  \ \____      ||       \         |     |_____//         |  |      
   \|___/     /||     __/ __      |     |\     \    __  /   / __   
       /     / ||\    \  /  \    /     /|\|     |  /  \/   /_/  |  
      /_____/  /| \____\/    |  /_____/ |/_____/| |____________/|  
      |     | / | |    |____/| |     | / |    | | |           | /  
      |_____|/   \|____|   | | |_____|/  |____|/  |___________|/   
                       |___|/                                      
'''

time = datetime.datetime.now()
time = str(time.strftime("%H%M"))


entries = os.listdir(seq_location)

# for entry in entries:
#     print(f'{seq_location}{entry}')

animation = {"animation": []}


def main():

    framenr = 0

    for i, entry in enumerate(entries):

        image = Image.open(
            f'{seq_location}{entry}')
        # you can first resize the image if needed
        image = image.resize((160, 90))
        image = image.convert('RGB')
        ascii_art = convert_to_ascii_art(image)

        print(i)

        print(f'{seq_location}{entry}')
        save_as_json(ascii_art, i)


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


def save_as_json(ascii_art, i):
    print(i)
    text = ""
    for line in ascii_art:
        text = text + line + ('\n')

    global animation
    animation["animation"].append(
        {"frameNumber": i, "frameContent": text})

    # Write the animation to a JSON file
    with open("json_output/looped_seq.json", "w") as f:
        json.dump(animation, f, indent=4)


if __name__ == '__main__':
    main()
