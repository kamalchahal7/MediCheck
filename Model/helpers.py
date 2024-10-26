from tensor_imports import *

def get_data(type:str,dtype:str):

    return image_dataset_from_directory(
        f"./data/{type}/{dtype}",
        labels="inferred",
        label_mode="categorical",
        image_size=[256,256],
        interpolation='nearest',
        batch_size=32,
        shuffle=True
    )

def convert_to_float(image, label):

    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label

def tune(ds:tf.data.Dataset):

    return (
        ds.map(convert_to_float)
        .cache()
        .prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    )