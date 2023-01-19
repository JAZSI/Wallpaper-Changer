import ctypes
import os
import time

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
    print(f'Wallpaper set to {image_path}')

current_dir = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(current_dir, "wallpapers")

while True:
    images = os.listdir(images_folder)

    import random
    image = random.choice(images)

    set_wallpaper(os.path.join(images_folder, image))
    time.sleep(300)

