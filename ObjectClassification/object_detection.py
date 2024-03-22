import cv2
from . import detection_methodes
from . import utilities
import numpy as np
from ..ServoControls import servo 


def RGB_and_Sides_classification(shape_segments: list[int], color_ranges: list[tuple]) -> int:
    """
    This function is used to classify the shapes and colors of the object in the frame and return the choice index.
    :param shape_segments: list of the number of segments in the shape; type [int, int, int]
    :param color_ranges: list of the ranges of the colors in HSV hue spectre; type [(int, int), (int, int), (int, int)]
    :return: the index of the shape and color mached
    """

    cap = cv2.VideoCapture(0)

    count = [0, 0, 0]
    ret, frame = cap.read()
    black_image = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)

    #object passing trough this rectange will be counted
    count_rect = [[int(frame.shape[0]/2), 0], [int(frame.shape[0]/2+10), frame.shape[1]]] 
    in_last = False


    while True:
        ret, frame = cap.read()

        contour, sides = detection_methodes.shapes(frame, 120, 0.02)

        if contour is not None:
            nb = black_image.copy()
            cv2.fillPoly(nb, [contour], 255)

            result = cv2.bitwise_and(frame, frame, mask=nb)

            
            for i in range(0, 3):
                if (shape_segments[i] == 0 or shape_segments[i] == sides) and \
        (color_ranges[i] == (0, 360) or detection_methodes.color(result, color_ranges[i][0], color_ranges[i][1], 50)):
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
                    
                    if count_rect[0][0] <= x <= count_rect[1][0] and count_rect[0][1] <= y <= count_rect[1][1] and not in_last:
                        utilities.predictionHandler(i)

                        count[i] += 1
                        utilities.printState(count)
                        in_last = True
                        break


        else:
            result = black_image

        cv2.rectangle(result, tuple(count_rect[0]), tuple(count_rect[1]), (0,255,0), 2)

        cv2.imshow('Object Recognition', result)


        try:
            in_last = False if x > count_rect[1][0] or y > count_rect[1][1] else in_last
        except:
            in_last = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            servo.cleanup()
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':

    ####### SETUP ########
    # 2 options, third for unrecognized
    # use first 2 

    shape_segments = [4, 3, 0]   # 0 for any
    color_ranges = [(0, 40), (180, 240), (0, 360)]

    ######################

    count = [0, 0, 0]

    cap = cv2.VideoCapture(0)  # Use 0 for default camera, change if necessary

    #####################


    RGB_and_Sides_classification(shape_segments, color_ranges, cap)