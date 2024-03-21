from multiprocessing import Process
from .ObjectClassification.object_detection import RGB_and_Sides_classification

process = None

def startDetection(shape_segments, color_ranges):
    global process

    # cap = cv2.VideoCapture(0) Add this to the start of RGB_and_Sides_classification

    process = Process(target=RGB_and_Sides_classification, args=(shape_segments, color_ranges))
    process.start()
    print("Starting detection")

def stopDetection():
    global process
    if process is not None:
        process.terminate()
        process.join()
        print("Stopping detection")




if __name__ == '__main__':

    ####### SETUP ########
    # 2 options, third for unrecognized
    # use first 2 

    shape_segments = [4, 3, 0]   # 0 for any
    color_ranges = [(0, 40), (180, 240), (0, 360)]

    startDetection(shape_segments, color_ranges)


