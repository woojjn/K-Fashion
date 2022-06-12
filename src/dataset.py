import os
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset

from utils import label_to_num, fashion_style_list


class ClothDataset(Dataset):
    def __init__(self, json_dir=r"../data/Training", data_dir=r"../data/Training"):
        """
        Arguments:
            image_dict:Dict[(image_file_name, rect_xy):fabric]
            data_dir:Image path
        """
        super().__init__()
        self.json_dir = json_dir
        self.image_dict = image_dict
        self.image_files = []

        self.setup()

    def setup(self):
        
        for fashion_style in fashion_style_list:
            for json_file in os.listdir(self.json_dir):
                json_path = os.paht.join(json_dir, json_file)

        # with open(self.json_file, "r") as f:
            


    def __getitem__(self, idx):
        file_name, xy, fabric = self.image_files[idx]

        fabric = fabric[0]
            
        x, y, w, h = map(int, xy)
        im = Image.open(file_name)
        im = transforms.ToTensor()(im)
        im = torchvision.transforms.functional.crop(im, y, x, h, w)
        im = transforms.Resize((300, 300))(im)

        fabric_label = label_to_num(fabric)
        return im, fabric_label

    def __len__(self):
        return len(self.image_files)

print(fashion_style_list)