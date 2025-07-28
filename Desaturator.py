from PIL import Image, ImageEnhance
import os


i_saturation_percentage = 0
directory_to_copy = "C:/Users/jacks/AppData/Roaming/.minecraft/vanilla optifine pack for now/vanilla TexturePack/assets/minecraft"
directory_to_paste = "C:/Users/jacks/AppData/Roaming/.minecraft/resourcepacks/Desat test pack/assets/minecraft"


def change_color(directory, save_dir):
    img = Image.open(directory)

    img = img.convert('RGBA')
    
    desaturator = ImageEnhance.Color(img)

    desaturated_image = desaturator.enhance(i_saturation_percentage/100)

    print(directory)

    if (directory[-8:] == "sky0.png"):
        desaturated_image.putpixel((12, 0), (121,166,255, 255))
    elif (directory[-8:] == "fog0.png"):
        desaturated_image.putpixel((12,0),(192,216, 255, 255))

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


