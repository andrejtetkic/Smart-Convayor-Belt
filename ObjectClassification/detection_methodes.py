import cv2
import numpy as np 



def shapes(img, threshold_value, aprox_poly):

    # converting image into grayscale image 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # setting threshold of gray image 
    _, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY) 

    # using a findContours() function 
    contours, _ = cv2.findContours( 
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    # Set the minimum and maximum contour lengths
    min_length = 80
    max_length = 500

    # Filter contours using a lambda function
    filtered_contours = list(filter(lambda cnt: min_length <= cv2.arcLength(cnt, True) <= max_length, contours))

    # list for storing names of shapes 
    try:
        contour = max(filtered_contours, key=cv2.contourArea)
    except:
        return None, 0

    if cv2.arcLength(contour, closed=True) < 100:
        return None, 0

    # cv2.approxPloyDP() function to approximate the shape 
    approx = cv2.approxPolyDP( 
        contour, aprox_poly * cv2.arcLength(contour, True), True) 
    
    return contour, len(approx)


def color(frame, lower_color, upper_color, min_brightness):

    blur = cv2.GaussianBlur(frame, (15, 15), 2)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_color = np.array([lower_color/2, 30, min_brightness])
    upper_color = np.array([upper_color/2, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)

    _, threshold = cv2.threshold(mask, 170, 255, cv2.THRESH_BINARY) 
    contours, _ = cv2.findContours( 
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    if len(contours) > 0 and cv2.arcLength(max(contours, key=cv2.contourArea), closed=True) > 100:
        return True
    return False