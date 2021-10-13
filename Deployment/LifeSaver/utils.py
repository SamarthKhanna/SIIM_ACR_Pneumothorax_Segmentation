import tensorflow as tf
import pandas as pd
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import tensorflow_io as tfio
from tensorflow.python.ops.numpy_ops import np_config
from .apps import LifesaverConfig
np_config.enable_numpy_behavior()


def get_input_image_path(instance, filename):
    return 'input_image/{}'.format(filename)


def get_output_image_path(instance, filename):
    return 'output_image/{}'.format(filename)


def decode_image(image_path, size=256):
    # read the image from image_path
    image = tf.io.read_file(image_path)
    # convert the image into a 3D tensor
    image = tfio.image.decode_dicom_image(
        image, dtype=tf.uint8, color_dim=True, scale='preserve')
    # convert image datatype to float32
    image = tf.image.convert_image_dtype(image, tf.float32)
    # squeeze the image from shape (1,1024,1024,1) to (1024,1024,1)
    image = tf.squeeze(image, [0])
    # cons = tf.constant([1,1,3], tf.int32)
    # using tf.tile convert image shape (1024,1024,1) tp (1024,1024,3)
    # image=tf.tile(image,cons)
    image = tf.tile(image, tf.constant([1, 1, 3], tf.int32))
    # resize the image
    image = tf.image.resize(image, size=[size, size])

    return image


def predict(image_path):
    image = decode_image(image_path)
    predicted = LifesaverConfig.model.predict(image[np.newaxis, :, :, :])
    predicted = predicted[0, :, :, 0]
    mask = predicted > 0.5
    str = ""
    if mask.sum():
        str = "The patient has Pneumothorax, marked by the red region."
    else:
        str = "This patient does not have Pneumothorax!"
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow(image, cmap=plt.cm.bone)
    plt.subplot(122)
    plt.imshow(image, cmap=plt.cm.bone)
    plt.imshow(np.squeeze(mask), alpha=0.3, cmap='Reds')
    return [str, plt]
