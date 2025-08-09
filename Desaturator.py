from PIL import Image, ImageEnhance
import os


i_saturation_percentage = 0
directory_to_copy = "C:/Users/jacks/curseforge/minecraft/Instances/FabulousSMP/resourcepacks/vanilla TexturePack/assets"
directory_to_paste = "C:/Users/jacks/curseforge/minecraft/Instances/FabulousSMP/resourcepacks/vanilla TexturePack - Copy/assets"
non_image_recursive_exceptions = ["cherry_grove.json", "colors.json"]


def change_color(directory, save_dir):
    img = Image.open(directory)

    img = img.convert('RGBA')
    
    desaturator = ImageEnhance.Color(img)

    desaturated_image = desaturator.enhance(i_saturation_percentage/100)

    print(directory)

    desaturated_image.save(save_dir)


def change_hex_color(directory, altered_directory):
    file = open(directory, 'w')

    




# used to convert non-image hexidecimal to HSV (hue, saturation, value) as to directly affect the saturation (S) using i_saturation_percentage 
def convert_hex_to_HSV(hex_str):
    #covert Hex values to ints so they can be divided
    red = int(hex_str[0:2], 16)/255
    green = int(hex_str[2:4], 16)/255
    blue = int(hex_str[4:6], 16)/255

    C_max = max(red,green,blue)
    C_min = min(red,green,blue)

    C_delta = C_max - C_min

    if C_delta == 0:
        H = 0
    elif C_max == red:
        H = 60 * (((green - blue)/C_delta) % 6)
    elif C_max == green:
        H = 60 * (((blue-red)/C_delta) + 2)
    elif C_max == blue:
        H = 60 * (((red-green)/C_delta)+4)

    if C_max == 0:
        S = 0
    else:
        S = C_delta/C_max

    V = C_max

    return H,S,V



def test_against_exception(directory):
    for word in non_image_recursive_exceptions:
        if word == directory[-1*word.len():]:
            return True
    return False


def recurse_strange_folders(directory, altered_directory):
    assets_list = os.listdir(directory)
    for asset in assets_list:
        if asset[-4:] == ".png" or asset[-4:] == ".PNG":
            change_color(f"{directory}/{asset}",f"{altered_directory}/{asset}")
        elif asset[-7:] == ".mcmeta" or asset[-11:] == ".properties" or asset[-4:] == ".log" or asset[-5:] == ".json":
            if (test_against_exception(directory)):
                change_hex_color(directory, altered_directory)
            else:
                pass
        else:
            recurse_strange_folders(f"{directory}/{asset}",f"{altered_directory}/{asset}")
            


def __main__ ():
    altar_dir = directory_to_copy
    save_dir = directory_to_paste

    for folder in os.listdir(altar_dir):
        recurse_strange_folders(f"{altar_dir}/{folder}", f"{save_dir}/{folder}")


    


__main__()


