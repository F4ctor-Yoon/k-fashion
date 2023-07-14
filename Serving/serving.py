import flask
from flask_cors import CORS, cross_origin
from flask import request
import os
import numpy as np

import cv2
from PIL import ImageFile

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import Adam, AdamW
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.applications.vgg19 import VGG19

label2idx = {'레트로': 0,
'로맨틱': 1,
'리조트': 2,
'매니시': 3,
'모던': 4,
'밀리터리': 5,
'섹시': 6,
'소피스트케이티드': 7,
'스트리트': 8,
'스포티': 9,
'아방가르드': 10,
'오리엔탈': 11,
'웨스턴': 12,
'젠더리스': 13,
'컨트리': 14,
'클래식': 15,
'키치': 16,
'톰보이': 17,
'펑크': 18,
'페미닌': 19,
'프레피': 20,
'히피': 21,
'힙합': 22}

idx2label = dict(map(reversed, label2idx.items()))

test_transform = tf.keras.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.image.convert_image_dtype(x, dtype=tf.float32)),
    tf.keras.layers.Lambda(lambda x: tf.image.resize(x, size=(224, 224))),
    tf.keras.layers.Lambda(lambda x: (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225])
])
temp_img_path = "여기에 임시 폴더의 절대 경로를 입력하세요."
mean_img_path = './mean_img.jpg'
mean_img = cv2.imread(mean_img_path)
ImageFile.LOAD_TRUNCATED_IMAGES = True

app = flask.Flask(__name__)
model = tf.keras.models.load_model('./vgg19_full_freeze_dropout05.h5')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class TestDataset(tf.keras.utils.Sequence):
    def __init__(self, root, transform=None):
        self.root = root
        self.image_list = os.listdir(root)
        self.transform = transform

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, index):
        image_path = os.path.join(self.root, self.image_list[index])
        image = tf.keras.preprocessing.image.load_img(image_path)
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = self.transform(image)
        return self.image_list[index], image

@app.route("/serving", methods=["POST"])
@cross_origin()
def serving():
    data = {"success": False};
    file = request.files.get('image')
    
    file.save(os.path.join(temp_img_path, 'image.jpg'))
    
    batch_size = 1

    test_dataset = TestDataset(temp_img_path, transform=test_transform)
    test_dataloader = tf.data.Dataset.from_generator(
        lambda: test_dataset,
        output_signature=(
            tf.TensorSpec(shape=(), dtype=tf.string),
            tf.TensorSpec(shape=(224, 224, 3), dtype=tf.float32)
        )
    ).batch(batch_size)
    
    mean_img_path = './mean_img.jpg'
    mean_img = cv2.imread(mean_img_path)
    
    result = []

    for fnames, tData in test_dataloader:
        tData = tData.numpy()
        output = model.predict(tData - mean_img)
        pred = np.argmax(output, axis=1)

        for j in range(len(fnames)):
            result.append({
                'filename': fnames[j].numpy().decode('utf-8'),
                'style': pred[j]
            })
        break
    
    os.remove(os.path.join(temp_img_path, 'image.jpg'))
    
    data["answer"] = idx2label[result[0]['style']]
    data["success"] = True
    return flask.jsonify(data)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask staring server..."
        "peases wait until server has fully started"))

    app.run(host='0.0.0.0', port='8081')