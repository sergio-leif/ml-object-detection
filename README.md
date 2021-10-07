# ml-object-detection
Using ImageAI to detect objects

# Classification
## Download Model

Download one of the next pre-trained models and save it in the models folder.

- **[MobileNetV2](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/mobilenet_v2.h5)** _(Size = 4.82 mb, fastest prediction time and moderate accuracy)_
- **[ResNet50](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_imagenet_tf.2.0.h5)** by Microsoft Research _(Size = 98 mb, fast prediction time and high accuracy)_
 - **[InceptionV3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5)** by Google Brain team _(Size = 91.6 mb, slow prediction time and higher accuracy)_
 - **[DenseNet121](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5)** by Facebook AI Research _(Size = 31.6 mb, slower prediction time and highest accuracy)_

# Detection
## Download Model

* **[RetinaNet](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5)** _(Size = 145 mb, high performance and accuracy, with longer detection time)_
* **[YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)** _(Size = 237 mb, moderate performance and accuracy, with a moderate detection time)_
* **[TinyYOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5)** _(Size = 34 mb, optimized for speed and moderate performance, with fast detection time)_

# Output 

Once executed [detection.py](./detection.py), the console exit would be similar to:

```
person  :  89.0386700630188  :  [383, 22, 603, 367]
--------------------------------
book  :  45.14172077178955  :  [341, 159, 485, 242]
--------------------------------
tv  :  44.88099813461304  :  [600, 39, 744, 307]
--------------------------------
laptop  :  44.59174871444702  :  [108, 194, 233, 304]
--------------------------------
potted plant  :  40.599796175956726  :  [263, 35, 353, 191]
--------------------------------
tv  :  39.87395167350769  :  [82, 63, 338, 241]
--------------------------------
tv  :  33.86337757110596  :  [606, 181, 736, 372]
--------------------------------
tv  :  33.62616300582886  :  [179, 98, 332, 238]
--------------------------------
keyboard  :  33.52274298667908  :  [139, 281, 248, 316]
--------------------------------
```

And a new image will be created with the object detection of the picture.

# References

https://github.com/OlafenwaMoses/ImageAI

