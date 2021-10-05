from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()

prediction = ImageClassification()
# prediction.setModelTypeAsMobileNetV2()
prediction.setModelTypeAsInceptionV3()
# prediction.setModelPath(os.path.join(execution_path, "models/mobilenet_v2.h5"))
prediction.setModelPath(os.path.join(execution_path, "models/inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "images/monkey.jpeg"), result_count=2 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)