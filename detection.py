from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
# detector.setModelTypeAsYOLOv3()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "models/detection/resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "images/professional.jpeg"), output_image_path=os.path.join(execution_path , "images/object_detection.jpeg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
