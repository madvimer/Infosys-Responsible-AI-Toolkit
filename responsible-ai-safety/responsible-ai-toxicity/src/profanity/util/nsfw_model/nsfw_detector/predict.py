#! python

import argparse
# from datetime import time
import time
import json
from os import listdir
import os
from os.path import isfile, join, exists, isdir, abspath
import shutil
import uuid

import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
from profanity.config.logger import CustomLogger
log = CustomLogger()

IMAGE_DIM = 224   # required/default image dimensionality
# IMAGE_DIM = 299



    

def load_images(image_paths, image_size, verbose=True):
    '''
    Function for loading images into numpy arrays for passing to model.predict
    inputs:
        image_paths: list of image paths to load
        image_size: size into which images should be resized
        verbose: show all of the image path and sizes loaded
    
    outputs:
        loaded_images: loaded images on which keras model can run predictions
        loaded_image_indexes: paths of images which the function is able to process
    
    '''
    loaded_images = []
    loaded_image_paths = []

    if isdir(image_paths):
        parent = abspath(image_paths)
        image_paths = [join(parent, f) for f in listdir(image_paths) if isfile(join(parent, f))]
    elif isfile(image_paths):
        image_paths = [image_paths]

    for img_path in image_paths:
        try:
            image = keras.preprocessing.image.load_img(img_path, target_size=image_size)
            image = keras.preprocessing.image.img_to_array(image)
            image /= 255
            loaded_images.append(image)
            loaded_image_paths.append(img_path)
        except Exception as ex:
            print("Image Load Failure")
    
    return np.asarray(loaded_images), loaded_image_paths


class Model:
    def load_model(model_path):
        if model_path is None or not exists(model_path):
            raise ValueError("saved_model_path must be the valid directory of a saved model to load.")
        
        model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer},compile=False)
        return model


def classify(model, input_paths, image_dim=IMAGE_DIM, predict_args={}):
    """
    Classify given a model, input paths (could be single string), and image dimensionality.
    
    Optionally, pass predict_args that will be passed to tf.keras.Model.predict().
    """
    images, image_paths = load_images(input_paths, (image_dim, image_dim))
    probs = classify_nd(model, images, predict_args)
    return dict(zip(image_paths, probs))


def classify_nd(model, nd_images, predict_args={}):
    """
    Classify given a model, image array (numpy)
    
    Optionally, pass predict_args that will be passed to tf.keras.Model.predict().
    """
    model_preds = model.predict(nd_images, **predict_args)
    # preds = np.argsort(model_preds, axis = 1).tolist()
    
    categories = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']

    probs = []
    for i, single_preds in enumerate(model_preds):
        single_probs = {}
        for j, pred in enumerate(single_preds):
            single_probs[categories[j]] = float(pred)
        probs.append(single_probs)
    return probs

model = Model.load_model('../models/nsfw.299x299.h5') 


class Detector:
    def detector( image_obj):
        
        id = uuid.uuid4().hex
        output_folder = id
        os.makedirs(output_folder, exist_ok=True)
        output_image_path = os.path.join(output_folder, "received.png")
        image_obj.save(output_image_path, format="PNG")

        # model = load_model('profanity/util/nsfw_model/nsfw.299x299.h5') 

        source = id+'/received.png'

        # opt = argparse.Namespace(image_source=source, saved_model_path='nsfw_mobilenet2.224x224.h5', image_dim=IMAGE_DIM)
        img_dim = 299
        startTime = time.time()
        image_preds = classify(model, source, img_dim)
        endTime = time.time()

        log.debug("Total Time Taken====="+str(endTime - startTime))
        # image_preds = classify(model, 'image_source', 'image_dim')
    # model = load_model('saved_model.h5')    
    # image_preds = classify(model, 'KARAN.png', (224, 224))
        
        # shutil.rmtree("temp")
        # print("Temp Folder Deleted")
        # print("imageprediction======",image_preds['temp/received.png'],'\n')
        res = id+'/received.png'
        print(json.dumps(image_preds, indent=2), '\n')
        shutil.rmtree(id)
        log.debug(str(id)+" Folder Deleted")
        return image_preds[res]

# def main(args=None):
#     parser = argparse.ArgumentParser(
#         description="""A script to perform NFSW classification of images""",
#         epilog="""
#         Launch with default model and a test image
#             python nsfw_detector/predict.py --saved_model_path mobilenet_v2_140_224 --image_source test.jpg
#     """, formatter_class=argparse.RawTextHelpFormatter)
    
#     submain = parser.add_argument_group('main execution and evaluation functionality')
#     submain.add_argument('--image_source', dest='image_source', type=str, required=True, 
#                             help='A directory of images or a single image to classify')
#     submain.add_argument('--saved_model_path', dest='saved_model_path', type=str, required=True, 
#                             help='The model to load')
#     submain.add_argument('--image_dim', dest='image_dim', type=int, default=IMAGE_DIM,
#                             help="The square dimension of the model's input shape")
#     if args is not None:
#         config = vars(parser.parse_args(args))
#     else:
#         config = vars(parser.parse_args())

#     if config['image_source'] is None or not exists(config['image_source']):
#     	raise ValueError("image_source must be a valid directory with images or a single image to classify.")
    
#     model = load_model(config['saved_model_path'])    
#     image_preds = classify(model, config['image_source'], config['image_dim'])
#     # model = load_model('saved_model.h5')    
#     # image_preds = classify(model, 'KARAN.png', (224, 224))
#     print(json.dumps(image_preds, indent=2), '\n')


# if __name__ == "__main__":
	# main()
