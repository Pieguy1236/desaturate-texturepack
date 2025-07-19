from PIL import Image, ImageEnhance
import os


i_saturation_percentage = 0
directory_to_copy = "C:/Users/jacks/AppData/Roaming/.minecraft/resourcepacks/Vanilla textures 1.21.8/assets/minecraft/textures"
directory_to_paste = "C:/Users/jacks/AppData/Roaming/.minecraft/resourcepacks/Vanilla textures 1.21.8 saturation test 90%/assets/minecraft/textures"


def change_color(directory, save_dir):
    img = Image.open(directory)

    img = img.convert('RGBA')
    
    desaturator = ImageEnhance.Color(img)

    desaturated_image = desaturator.enhance(i_saturation_percentage/100)

    print(directory)

    desaturated_image.save(save_dir)



def recurse_strange_folders(directory, altered_directory):
    assets_list = os.listdir(directory)
    for asset in assets_list:
        if asset[-4:] == ".png":
            change_color(f"{directory}/{asset}",f"{altered_directory}/{asset}")
        elif asset[-7:] == ".mcmeta":
            pass
        else:
            recurse_strange_folders(f"{directory}/{asset}",f"{altered_directory}/{asset}")
            


def __main__ ():
    altar_dir = directory_to_copy
    save_dir = directory_to_paste

    textureList = os.listdir(altar_dir + "/block")

    for folder in os.listdir(altar_dir):
        recurse_strange_folders(f"{altar_dir}/{folder}", f"{save_dir}/{folder}")


        # if (folder == "effect" or folder == "font"):
        #     pass
        # elif (folder == "entity" or folder == "gui" or folder == "map" or folder == "trims"):
        #     recurse_strange_folders(f"{altar_dir}/{folder}", f"{save_dir}/{folder}")
        # else:
        #     pass
        #     textureList = os.listdir(f"{altar_dir}/{folder}")
        #     for image in textureList:
        #         if(image[-1] == 'g'):
        #             change_color(f"{altar_dir}/{folder}/{image}",f"{save_dir}/{folder}/{image}")
        

    # print(textureList)


    # desaturated_image.show()


__main__()


