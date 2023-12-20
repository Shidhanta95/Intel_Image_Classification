from extract_data import extract_data
from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os

def visualise_image():
    url = extract_data()
    url_response = requests.get(url)
    with zipfile.ZipFile(BytesIO(url_response.content)) as z:
        z.extractall('.')
    print(os.listdir())
    buildings = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/buildings"))
    forest = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/forest"))
    glacier = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/glacier"))
    mountain = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/mountain"))
    sea = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/sea"))
    street = os.listdir(os.path.join(os.getcwd(),"seg_train/seg_train/street"))
    path = pathlib.Path(os.path.join(os.getcwd(),"seg_train/seg_train"))
    def open_random_image(path):
        # Get a list of all files in the folder
        all_files = os.listdir(path)
        random_image_file = random.choice(all_files)
        image_path = os.path.join(path, random_image_file)
        image = Image.open(image_path)
        return image
    buildings_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/buildings"))
    forest_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/forest"))
    glacier_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/glacier"))
    mountain_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/mountain"))
    sea_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/sea"))
    street_image = open_random_image(os.path.join(os.getcwd(),"seg_train/seg_train/street"))
    buildings_image.save('building_image.jpg')
    forest_image.save('forest_image.jpg')
    glacier_image.save('glacier_image.jpg')
    mountain_image.save('mountain_image.jpg')
    sea_image.save('sea_image.jpg')
    street_image.save('street_image.jpg')
    return path,buildings_image,forest_image,glacier_image,mountain_image,sea_image,street_image 

visualise_image()
