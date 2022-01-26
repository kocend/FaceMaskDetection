from tensorflow.keras.preprocessing.image import ImageDataGenerator
import keras
import os

path = os.getcwd()
path = os.path.join(path, 'dataset')
path_test_with_mask = os.path.join(path, 'test_without_mask')
imagenet = keras.models.load_model("imagenet.h5")

test_datagen = ImageDataGenerator(rescale=1.0/255.)

numberOfImages = 386

test_generator = test_datagen.flow_from_directory(path_test_with_mask,
                                                    batch_size=numberOfImages,
                                                    class_mode='binary',
                                                    target_size=(224, 224))
result = imagenet.predict(next(test_generator)[0])

noMask = 0
mask = 0

for i in result:
    if i > 0.5:
        noMask += 1
    if i <= 0.5:
        mask += 1

print("Mask: " + str(mask) + ", Without Mask: " + str(noMask) + ", ratio of true predictions: " + str((noMask / numberOfImages)))
