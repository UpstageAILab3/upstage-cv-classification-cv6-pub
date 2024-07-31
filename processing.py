from PIL import Image
import numpy as np
from transformers import ViTFeatureExtractor
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
from utils import rotate_preserve_size
import os
from config import SAVE_IMAGE_DIR
from loguru import logger
import datetime

def preprocess(model_name, image_path):
    if model_name in ["vit", "tag-cnn"]:
        image_size = 224
    else:
        image_size = 299

    img = Image.open(image_path)
    img = img.resize((image_size, image_size))
    img = np.array(img)
    
    if model_name == "vit":
        X_vit = [img]
        X_vit = feature_extractor(images=X_vit, return_tensors="pt")["pixel_values"]
        X_vit = np.array(X_vit)
        X = X_vit

    if model_name == "tag-cnn":
        X_vit = [img]
        X_vit = feature_extractor(images=X_vit, return_tensors="pt")["pixel_values"]
        X_vit = np.array(X_vit)

        img = np.expand_dims(img, axis=0)
        X = [X_vit, img]

    if model_name in ["efficientnetv2b2", "en", "efficientnetv2b2"]:
        img = np.expand_dims(img, axis=0)
        X = img

    return X
    

def postprocess(image_path, angle, size):
    # Load the image
    
    image = rotate_preserve_size(image_path, angle, (size, size), False)
    
    # Rotate the image by the predicted angle
    processed_image = image.rotate(angle, expand=True, fillcolor=(255, 255, 255))
    
    
    # Extract the filename and create the output path with a suffix indicating processed status
    base_name, ext = os.path.splitext(os.path.basename(image_path))
    filename = f"{base_name}_processed{ext}"
    output_path = os.path.join(SAVE_IMAGE_DIR, filename)
    
    # Save the processed image
    processed_image.save(output_path)
    
    return processed_image