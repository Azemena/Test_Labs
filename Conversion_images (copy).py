import os
from PIL import Image
import time

#images_imagenet = os.listdir("Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC")
images_imagenet = ["train"]
for directory in images_imagenet:  # test, train, val
    if "train" in directory:
        folders = os.listdir("Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/train")
        folders.sort()
        for folder in folders:  # n...
            images = os.listdir("Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/train/{}".format(folder))
            for image in images:
                if os.path.splitext(image)[1] == ".JPEG":
                    try:
                        im1 = Image.open(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/train/{}/{}'.format(folder, image))
                        im1.save(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/train/{}/{}.jpg'.format(folder,
                                                                                                     os.path.splitext
                                                                                                     (image)[0]))
                        os.remove(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/train/{}/{}'.format(folder, image))
                    except OSError:
                        pass
            print(folder, "done.")
    else:
        images = os.listdir("Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/{}".format(directory))
        for image in images:  # For test and val: images IDs   For train: directories
            if os.path.splitext(image)[1] == ".JPEG":
                im1 = Image.open(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/{}/{}'.format(directory, image))
                im1.save(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/{}/{}.jpg'.format(directory,
                                                                                             os.path.splitext(image)[0]))
                os.remove(r'Datasets/ImageNet_Wikipedia/ILSVRC/Data/CLS-LOC/{}/{}'.format(directory, image))
    time.sleep(10)

