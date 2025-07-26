from PIL import Image, ImageEnhance
import os


i_saturation_percentage = 0
directory_to_copy = "C:/Users/jacks/AppData/Roaming/.minecraft/resourcepacks/Vanilla textures 1.21.8/assets/minecraft"
directory_to_paste = "C:/Users/jacks/AppData/Roaming/.minecraft/resourcepacks/Vanilla textures 1.21.8 saturation test 90%/assets/minecraft"


def change_color(directory, save_dir):
    img = Image.open(directory)

    img = img.convert('RGBA')
    
    desaturator = ImageEnhance.Color(img)

    desaturated_image = desaturator.enhance(i_saturation_percentage/100)

    print(directory)

    if (directory[-8:] == "sky.png"):
        desaturated_image.putpixel((0, 12), "79A6FF")

    desaturated_image.save(save_dir)



def recurse_strange_folders(directory, altered_directory):
    assets_list = os.listdir(directory)
    for asset in assets_list:
        if asset[-4:] == ".png" or asset[-4:] == ".PNG":
            change_color(f"{directory}/{asset}",f"{altered_directory}/{asset}")
        elif asset[-7:] == ".mcmeta" or asset[-11:] == ".properties":
            pass
        else:
            recurse_strange_folders(f"{directory}/{asset}",f"{altered_directory}/{asset}")
            


def __main__ ():
    altar_dir = directory_to_copy
    save_dir = directory_to_paste

    for folder in os.listdir(altar_dir):
        recurse_strange_folders(f"{altar_dir}/{folder}", f"{save_dir}/{folder}")


    


__main__()


