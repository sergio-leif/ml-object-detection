from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "models/detection/resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "images/surfers_trim.mp4"),
                                output_file_path=os.path.join(execution_path, "images/surfers_detected")
                                , frames_per_second=20, log_progress=True)
print(video_path)